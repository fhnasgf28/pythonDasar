from sqlmodel import Session,select, SQLModel, create_engine
from salary_manager_api.models import SalarySlip

DATABASE_URL = "sqlite:///./salary_manager.db"

engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        print(session.exec(select(SalarySlip)).all())
        yield session
