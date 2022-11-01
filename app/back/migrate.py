from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import Column, Integer, String, Float
from models.package_classification import Base,ClassificationTypeModel,ClassificationModel,ProviderInstrumentModel,VehicleModel,TravelModel

user="lzr"
password="1522"
server="DESKTOP-02KB195\SQLEXPRESS"
database="integrador-lab-IV"
driver="{SQL Server}"
trusted_connection='yes'

connection_string = f"""DRIVER={driver};
                        SERVER={server};
                        DATABASE={database};
                        TRUSTED_CONNECTION={trusted_connection};
                        User Id={user};
                        Password={password}
                    """

connection_url = URL.create(
    "mssql+pyodbc", query={"odbc_connect": connection_string})

print(connection_url)

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

vehicle1=VehicleModel(type=1,matricula="12345")
travel1=TravelModel(vehicle=vehicle1)
pi1=ProviderInstrumentModel(name="Cataratas",price=25000,travel=travel1)


c1 = ClassificationModel(charge=1.4,clasification=first,provider_instrument=pi1)
session.add(c1)
session.commit()