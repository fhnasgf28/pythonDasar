from datetime import date
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from database import create_db_and_tables, get_session
from models import Employee, EmployeeCreate, SalaryCalculationRequest, SalarySlip

app = FastAPI(
    title="Salary Manager API",
    description="API sederhana untuk mengelola data karyawan dan menghitung gaji bulanan.",
    version="2.0.0",
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

    from sqlmodel import Session

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
        "version": "2.0.0",
        "features": ["SQLite", "Persistent data", "CORS enabled"],
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


@app.post("/salary/calculate", response_model=SalarySlip)
def calculate_salary(payload: SalaryCalculationRequest, session: Session = Depends(get_session)):
    employee = session.get(Employee, payload.employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    overtime_pay = employee.overtime_rate * payload.overtime_hours
    gross_salary = employee.base_salary + employee.allowance + overtime_pay + payload.bonus
    tax_amount = gross_salary * (employee.tax_percent / 100)
    net_salary = gross_salary - tax_amount - payload.deduction

    slip = SalarySlip(
        employee_id=employee.id,
        employee_name=employee.name,
        period=date.today().strftime("%B %Y"),
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
def get_salary_slips(session: Session = Depends(get_session)):
    return session.exec(select(SalarySlip)).all()


@app.get("/salary/slip/{employee_id}", response_model=SalarySlip)
def get_latest_salary_slip(employee_id: int, session: Session = Depends(get_session)):
    slips = session.exec(select(SalarySlip).where(SalarySlip.employee_id == employee_id)).all()
    if not slips:
        raise HTTPException(status_code=404, detail="Salary slip not found")
    return slips[-1]
