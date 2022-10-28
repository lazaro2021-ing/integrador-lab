from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
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
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def __repr__(self):
        return f'User({self.nombre}, {self.apellido})'
    def __str__(self):
        return self.nombre

user = User('lala','dadad')
session.add(user)
session.commit()