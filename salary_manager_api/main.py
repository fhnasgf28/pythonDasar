from datetime import date
from io import BytesIO
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from sqlmodel import Session, select

from database import create_db_and_tables, get_session
from models import (
    Employee,
    EmployeeCreate,
    EmployeeUpdate,
    SalaryCalculationRequest,
    SalarySlip,
)

app = FastAPI(
    title="Salary Manager API",
    description="API sederhana untuk mengelola data karyawan dan menghitung gaji bulanan.",
    version="3.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

    from database import engine

    with Session(engine) as session:
        employees = session.exec(select(Employee)).all()
        if not employees:
            session.add(
                Employee(
                    name="Farhan",
                    position="Backend Developer",
                    base_salary=8500000,
                    allowance=1500000,
                    overtime_rate=50000,
                    tax_percent=5,
                )
            )
            session.add(
                Employee(
                    name="Alya",
                    position="UI/UX Designer",
                    base_salary=7200000,
                    allowance=1200000,
                    overtime_rate=40000,
                    tax_percent=4,
                )
            )
            session.commit()


@app.get("/")
def root():
    return {
        "message": "Welcome to Salary Manager API",
        "docs": "/docs",
        "version": "3.0.0",
        "features": [
            "SQLite",
            "Persistent data",
            "CORS enabled",
            "Update & delete employee",
            "Filter slip by month",
            "Export slip to PDF",
        ],
    }


@app.get("/employees", response_model=List[Employee])
def get_employees(session: Session = Depends(get_session)):
    return session.exec(select(Employee)).all()


@app.post("/employees", response_model=Employee, status_code=201)
def create_employee(payload: EmployeeCreate, session: Session = Depends(get_session)):
    employee = Employee.model_validate(payload)
    session.add(employee)
    session.commit()
    session.refresh(employee)
    return employee


@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int, session: Session = Depends(get_session)):
    employee = session.get(Employee, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.put("/employees/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, payload: EmployeeUpdate, session: Session = Depends(get_session)):
    employee = session.get(Employee, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    update_data = payload.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(employee, key, value)

    session.add(employee)
    session.commit()
    session.refresh(employee)
    return employee


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, session: Session = Depends(get_session)):
    employee = session.get(Employee, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    session.delete(employee)
    session.commit()
    return {"message": f"Employee {employee_id} deleted successfully"}


@app.post("/salary/calculate", response_model=SalarySlip)
def calculate_salary(payload: SalaryCalculationRequest, session: Session = Depends(get_session)):
    employee = session.get(Employee, payload.employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    overtime_pay = employee.overtime_rate * payload.overtime_hours
    gross_salary = employee.base_salary + employee.allowance + overtime_pay + payload.bonus
    tax_amount = gross_salary * (employee.tax_percent / 100)
    net_salary = gross_salary - tax_amount - payload.deduction
    period = payload.period_month or date.today().strftime("%Y-%m")

    slip = SalarySlip(
        employee_id=employee.id,
        employee_name=employee.name,
        period=period,
        base_salary=employee.base_salary,
        allowance=employee.allowance,
        overtime_pay=overtime_pay,
        bonus=payload.bonus,
        gross_salary=gross_salary,
        tax_amount=tax_amount,
        deduction=payload.deduction,
        net_salary=net_salary,
    )

    session.add(slip)
    session.commit()
    session.refresh(slip)
    return slip


@app.get("/salary/slips", response_model=List[SalarySlip])
def get_salary_slips(
    month: Optional[str] = Query(default=None, description="Filter by month format YYYY-MM"),
    session: Session = Depends(get_session),
):
    slips = session.exec(select(SalarySlip)).all()
    if month:
        slips = [slip for slip in slips if slip.period == month]
    return slips


@app.get("/salary/slip/{employee_id}", response_model=SalarySlip)
def get_latest_salary_slip(employee_id: int, session: Session = Depends(get_session)):
    slips = session.exec(select(SalarySlip).where(SalarySlip.employee_id == employee_id)).all()
    if not slips:
        raise HTTPException(status_code=404, detail="Salary slip not found")
    return slips[-1]


@app.get("/salary/slip/{employee_id}/pdf")
def export_salary_slip_pdf(employee_id: int, session: Session = Depends(get_session)):
    slips = session.exec(select(SalarySlip).where(SalarySlip.employee_id == employee_id)).all()
    if not slips:
        raise HTTPException(status_code=404, detail="Salary slip not found")

    slip = slips[-1]
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, height - 50, "Salary Slip")

    pdf.setFont("Helvetica", 11)
    lines = [
        f"Employee ID   : {slip.employee_id}",
        f"Employee Name : {slip.employee_name}",
        f"Period        : {slip.period}",
        "",
        f"Base Salary   : Rp {slip.base_salary:,.0f}",
        f"Allowance     : Rp {slip.allowance:,.0f}",
        f"Overtime Pay  : Rp {slip.overtime_pay:,.0f}",
        f"Bonus         : Rp {slip.bonus:,.0f}",
        f"Gross Salary  : Rp {slip.gross_salary:,.0f}",
        f"Tax Amount    : Rp {slip.tax_amount:,.0f}",
        f"Deduction     : Rp {slip.deduction:,.0f}",
        f"Net Salary    : Rp {slip.net_salary:,.0f}",
    ]

    y = height - 90
    for line in lines:
        pdf.drawString(50, y, line)
        y -= 20

    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    filename = f"salary_slip_{slip.employee_id}_{slip.period}.pdf"
    return StreamingResponse(
        buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
