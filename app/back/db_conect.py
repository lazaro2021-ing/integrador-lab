from config import connection_string
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from models.models import Base
from sqlalchemy.orm import Session

connection_url = URL.create(
    "mssql+pyodbc", query={"odbc_connect": connection_string})


engine=create_engine(connection_url)

session = Session(engine)