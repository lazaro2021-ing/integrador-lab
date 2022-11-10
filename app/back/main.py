from fastapi import FastAPI
from models.models import *
from db_conect import session
from typing import List
from schemas.schemas import *

app = FastAPI()

#classification type
@app.get("/classificationtypes/", response_model=List[ClassificationTypeD])
def get_clasification_types():
    records =session.query(ClassificationTypeModel).all()
    return records

@app.post("/classificationtypes/")
def create_classification_types(type:ClassificationTypeD):
    cl_type=ClassificationTypeModel(type=type.type,charge=type.charge)
    session.add(cl_type)
    session.flush()
    return cl_type
   
#classification
@app.get("/classification/", response_model=List[ClassificationD])
def get_clasification():
    records =session.query(ClassificationModel).all()
    return records

@app.post("/classification/")
def create_classification_types(type:ClassificationD):
    cl_type=session.query(ClassificationTypeModel).filter_by(type=type.clasification.type).first()
    cl=ClassificationModel(clasification=cl_type,charge=cl_type.charge)
    session.add(cl)
    session.flush()
    return cl

#county
@app.get("/country/", response_model=List[CountryD])
def get_clasification():
    records =session.query(CountryModel).all()
    return records

@app.post("/country/")
def create_classification_types(country:CountryD):
    country=CountryModel(nombre=country.nombre)
    session.add(country)
    session.flush()
    return country

#serviceProvider(seria la agencia que brinda los servicios)
@app.get("/serviceprovider/", response_model=List[ServiceProviderD])
def get_clasification():
    records =session.query(ServiceProviderModel).all()
    return records

@app.post("/serviceprovider/")
def create_classification_types(s_p:ServiceProviderD):
    country=session.query(CountryModel).filter_by(nombre=s_p.country.nombre).first()
    service_provider=ServiceProviderModel(nombre=s_p.nombre,country=country)
    session.add(service_provider)
    session.flush()
    return service_provider