from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from models.models import Base,ClassificationTypeModel,ClassificationModel,ProviderInstrumentModel,VehicleModel,TravelModel,ExcursionModel,HotelModel
from config import connection_string


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

pi1=ProviderInstrumentModel(name="Cataratas",price=25000,clasification=c1)
session.add(pi1)
session.commit()

vehicle1=VehicleModel(type=1,matricula="12345")
session.add(vehicle1)
session.commit()

travel1=TravelModel(vehicle=vehicle1,provider=pi1)
session.add(travel1)
session.commit()

exc1=ExcursionModel(nombre="Bariloche cerro tronador",legajo="1234",telefono="12165465",provider=pi1)
session.add(exc1)
session.commit()

h1=HotelModel(calle="9 de julio",numero=1234,provider=pi1)
session.add(h1)
session.commit()