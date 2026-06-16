from typing import Optional

from sqlmodel import Field, SQLModel


class EmployeeBase(SQLModel):
    name: str
    position: str
    base_salary: float
    allowance: float = 0
    overtime_rate: float = 0
    tax_percent: float = 5


class Employee(EmployeeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(SQLModel):
    name: Optional[str] = None
    position: Optional[str] = None
    base_salary: Optional[float] = None
    allowance: Optional[float] = None
    overtime_rate: Optional[float] = None
    tax_percent: Optional[float] = None


class SalaryCalculationRequest(SQLModel):
    employee_id: int
    overtime_hours: float = 0
    bonus: float = 0
    deduction: float = 0
    period_month: Optional[str] = None


class SalarySlip(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
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
