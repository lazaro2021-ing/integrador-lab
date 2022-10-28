from turtle import back
from flask import Flask
from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import Column, Integer, String, Float


user="lzr"
password="1522"
server="DESKTOP-02KB195\SQLEXPRESS"
database="integrador-lab-IV"
driver="{SQL Server}"
trusted_connection='yes'

connection_string = f""" DRIVER={driver};
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
con=engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'user_test'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    direccion = relationship("Direccion")
    #fk_direccion = Column(Integer, ForeignKey("direccion_test.id"))
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def __repr__(self):
        return f'User({self.nombre}, {self.apellido})'
    def __str__(self):
        return self.nombre

class Direccion(Base):
    __tablename__ = 'direccion_test'
    id = Column(Integer, primary_key=True)
    calle = Column(String(50), nullable=False)
    numero = Column(Integer, nullable=False)
    fk_user = Column(Integer, ForeignKey("user_test.id"))
    #user = relationship("User")
    
    def __init__(self, calle, numero):
        self.calle = calle
        self.numero = numero
    def __repr__(self):
        return f'User({self.calle}, {self.numero})'
    def __str__(self):
        return self.calle

user = User('lala','dadad')
session.add(user)
session.commit()

ob = session.query(User).get(1)
print(ob.__dict__)

ob = session.query( Direccion).get(1)
print(ob.__dict__)

ob = session.query(User).filter_by(nombre='lazar').first()
print(ob.direccion)