from contextlib import asynccontextmanager
from datetime import date
from io import BytesIO
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from fastapi.responses import HTMLResponse
from pathlib import Path
from string import Template
from weasyprint import HTML as WeasyHTML
from sqlmodel import Session, select

from database import create_db_and_tables, engine, get_session
from models import (
    Employee,
    EmployeeCreate,
    EmployeeUpdate,
    SalaryCalculationRequest,
    SalarySlip,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()

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

    yield


app = FastAPI(
    title="Salary Manager API",
    description="API sederhana untuk mengelola data karyawan dan menghitung gaji bulanan.",
    version="3.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    """Generate PDF by rendering the HTML template and converting with WeasyPrint."""
    slips = session.exec(select(SalarySlip).where(SalarySlip.employee_id == employee_id)).all()
    if not slips:
        raise HTTPException(status_code=404, detail="Salary slip not found")

    slip = slips[-1]

    template_path = Path(__file__).parent / "templates" / "salary_template.html"
    if not template_path.exists():
        raise HTTPException(status_code=500, detail="Template file missing")

    tpl_text = template_path.read_text(encoding="utf-8")
    t = Template(tpl_text)

    currency = lambda v: f"Rp {v:,.0f}"
    rows = []
    rows.append(f"<tr><td>Base Salary</td><td class=\"amount\">{currency(slip.base_salary)}</td></tr>")
    rows.append(f"<tr><td>Allowance</td><td class=\"amount\">{currency(slip.allowance)}</td></tr>")
    rows.append(f"<tr><td>Overtime Pay</td><td class=\"amount\">{currency(slip.overtime_pay)}</td></tr>")
    rows.append(f"<tr><td>Bonus</td><td class=\"amount\">{currency(slip.bonus)}</td></tr>")
    rows.append(f"<tr><td>Tax</td><td class=\"amount\">- {currency(slip.tax_amount)}</td></tr>")
    rows.append(f"<tr><td>Other Deductions</td><td class=\"amount\">- {currency(slip.deduction)}</td></tr>")

    status = "Paid" if slip.net_salary >= 0 else "Pending"
    badge_class = "paid" if status == "Paid" else "pending"

    rendered = t.safe_substitute(
        company_name="Salary Manager",
        company_address="Jl. Contoh No.1 · +62 812-3456-7890",
        period=slip.period,
        section_title="Salary Details",
        employee_name=slip.employee_name,
        position="-",
        employee_id=slip.employee_id,
        generated_date=date.today().isoformat(),
        rows="\n".join(rows),
        net_salary=currency(slip.net_salary),
        status=status,
        badge_class=badge_class,
    )

    pdf_bytes = WeasyHTML(string=rendered).write_pdf()
    buffer = BytesIO(pdf_bytes)
    buffer.seek(0)
    filename = f"salary_slip_{slip.employee_id}_{slip.period}.pdf"
    return StreamingResponse(buffer, media_type="application/pdf", headers={"Content-Disposition": f"attachment; filename={filename}"})


@app.get("/salary/slip/{employee_id}/html", response_class=HTMLResponse)
def render_salary_slip_html(employee_id: int, session: Session = Depends(get_session)):
    """Return an HTML version of the salary slip using an inline Tailwind-inspired stylesheet.
    The HTML template is in `templates/salary_template.html` and uses simple $-placeholders.
    This HTML can be rendered to PDF with tools like `wkhtmltopdf` or `weasyprint`.
    """
    slips = session.exec(select(SalarySlip).where(SalarySlip.employee_id == employee_id)).all()
    if not slips:
        raise HTTPException(status_code=404, detail="Salary slip not found")

    slip = slips[-1]

    template_path = Path(__file__).parent / "templates" / "salary_template.html"
    if not template_path.exists():
        raise HTTPException(status_code=500, detail="Template file missing")

    tpl_text = template_path.read_text(encoding="utf-8")
    t = Template(tpl_text)

    currency = lambda v: f"Rp {v:,.0f}"

    # build rows HTML for components
    rows = []
    rows.append(f"<tr><td>Base Salary</td><td class=\"amount\">{currency(slip.base_salary)}</td></tr>")
    rows.append(f"<tr><td>Allowance</td><td class=\"amount\">{currency(slip.allowance)}</td></tr>")
    rows.append(f"<tr><td>Overtime Pay</td><td class=\"amount\">{currency(slip.overtime_pay)}</td></tr>")
    rows.append(f"<tr><td>Bonus</td><td class=\"amount\">{currency(slip.bonus)}</td></tr>")
    rows.append(f"<tr><td>Tax</td><td class=\"amount\">- {currency(slip.tax_amount)}</td></tr>")
    rows.append(f"<tr><td>Other Deductions</td><td class=\"amount\">- {currency(slip.deduction)}</td></tr>")

    # determine status
    status = "Paid" if slip.net_salary >= 0 else "Pending"
    badge_class = "paid" if status == "Paid" else "pending"

    rendered = t.safe_substitute(
        company_name="Salary Manager",
        company_address="Jl. Contoh No.1 · +62 812-3456-7890",
        period=slip.period,
        section_title="Salary Details",
        employee_name=slip.employee_name,
        position="-",
        employee_id=slip.employee_id,
        generated_date=date.today().isoformat(),
        rows="\n".join(rows),
        net_salary=currency(slip.net_salary),
        status=status,
        badge_class=badge_class,
    )

    return HTMLResponse(content=rendered)
