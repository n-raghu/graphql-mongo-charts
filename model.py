from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dbeng = create_engine('sqlite:///database.sqlite3')
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
)

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    isactive = Column(BOOLEAN)
    name = Column(String)


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer)


