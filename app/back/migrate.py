from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from models.models import *
from config import connection_string
from datetime import datetime

connection_url = URL.create(
    "mssql+pyodbc", query={"odbc_connect": connection_string})

engine=create_engine(connection_url)
Base.metadata.create_all(engine)

con=engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

#ClassificationTypeModel
first = ClassificationTypeModel(type='FIRST_CLASS',charge=1.45)
executive = ClassificationTypeModel(type='EXECUTIVE_CLASS',charge=1.15)
econimic = ClassificationTypeModel(type='ECONOMY_CLASS',charge=1.05)

session.add(first)
session.commit()
session.add(executive)
session.commit()
session.add(econimic)
session.commit()


states={}
for state_name in ["Created","Active","Completed","Canceled","Holded","Scheduled"]: 
    states[state_name]=StateTypeModel(name=state_name)
    session.add(states[state_name])
    session.commit()
