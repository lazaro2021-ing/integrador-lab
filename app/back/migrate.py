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

c1 = ClassificationModel(charge=1.4,clasification=first)
session.add(c1)
session.commit()

arg=CountryModel(nombre="Argentina")
session.add(arg)
session.commit()

states={}
for state_name in ["Created","Active","Completed","Canceled","Holded","Scheduled"]: 
    states[state_name]=StateTypeModel(name=state_name)
    session.add(states[state_name])
    session.commit()


'''
vehicle1=VehicleModel(type=1,matricula="12345")
session.add(vehicle1)
session.commit()

travel1=TravelModel(vehicle=vehicle1,provider=pi1)
session.add(travel1)
session.commit()

exc1=ExcursionModel(nombre="Bariloche cerro tronador",legajo="1234",telefono="12165465")
session.add(exc1)
session.commit()

h1=HotelModel(calle="9 de julio",numero=1234,provider=pi1)
session.add(h1)
session.commit()


cl=session.query(ClassificationTypeModel).filter_by(type="FIRST_CLASS").first()
print(cl)
'''


p=session.query(CountryModel).filter_by(nombre="lala").first()
print(p)