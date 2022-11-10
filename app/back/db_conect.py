from config import connection_string
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from models.models import Base

connection_url = URL.create(
    "mssql+pyodbc", query={"odbc_connect": connection_string})


engine=create_engine(connection_url)
Base.metadata.create_all(engine)

con=engine.connect()

Session = sessionmaker(bind=engine)
session = Session()