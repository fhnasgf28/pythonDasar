from datetime import date
from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="Salary Manager API",
    description="API sederhana untuk mengelola data karyawan dan menghitung gaji bulanan.",
    version="1.0.0",
)


class EmployeeCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    position: str = Field(..., min_length=2, max_length=100)
    base_salary: float = Field(..., gt=0)
    allowance: float = Field(0, ge=0)
    overtime_rate: float = Field(0, ge=0)
    tax_percent: float = Field(5, ge=0, le=100)


class Employee(EmployeeCreate):
    id: int


class SalaryCalculationRequest(BaseModel):
    employee_id: int
    overtime_hours: float = Field(0, ge=0)
    bonus: float = Field(0, ge=0)
    deduction: float = Field(0, ge=0)


class SalarySlip(BaseModel):
    employee_id: int
    employee_name: str
    period: str
    base_salary: float
    allowance: float
    overtime_pay: float
    bonus: float
    gross_salary: float
    tax_amount: float
    deduction: float
    net_salary: float


employees: Dict[int, Employee] = {
    1: Employee(
        id=1,
        name="Farhan",
        position="Backend Developer",
        base_salary=8500000,
        allowance=1500000,
        overtime_rate=50000,
        tax_percent=5,
    ),
    2: Employee(
        id=2,
        name="Alya",
        position="UI/UX Designer",
        base_salary=7200000,
        allowance=1200000,
        overtime_rate=40000,
        tax_percent=4,
    ),
}

salary_slips: List[SalarySlip] = []


@app.get("/")
def root():
    return {
        "message": "Welcome to Salary Manager API",
        "docs": "/docs",
        "available_endpoints": [
            "GET /employees",
            "POST /employees",
            "GET /employees/{employee_id}",
            "POST /salary/calculate",
            "GET /salary/slips",
            "GET /salary/slip/{employee_id}",
        ],
    }


@app.get("/employees", response_model=List[Employee])
def get_employees():
    return list(employees.values())


@app.post("/employees", response_model=Employee, status_code=201)
def create_employee(payload: EmployeeCreate):
    new_id = max(employees.keys(), default=0) + 1
    employee = Employee(id=new_id, **payload.model_dump())
    employees[new_id] = employee
    return employee


@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int):
    employee = employees.get(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.post("/salary/calculate", response_model=SalarySlip)
def calculate_salary(payload: SalaryCalculationRequest):
    employee = employees.get(payload.employee_id)
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

    salary_slips.append(slip)
    return slip


@app.get("/salary/slips", response_model=List[SalarySlip])
def get_salary_slips():
    return salary_slips


@app.get("/salary/slip/{employee_id}", response_model=Optional[SalarySlip])
def get_latest_salary_slip(employee_id: int):
    for slip in reversed(salary_slips):
        if slip.employee_id == employee_id:
            return slip
    raise HTTPException(status_code=404, detail="Salary slip not found")
