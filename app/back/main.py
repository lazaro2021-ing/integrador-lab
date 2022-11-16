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
def create_classification(type:ClassificationD):
    cl_type=session.query(ClassificationTypeModel).filter_by(type=type.clasification.type).first()
    cl=ClassificationModel(clasification=cl_type,charge=cl_type.charge)
    session.add(cl)
    session.flush()
    return cl

#county
@app.get("/country/", response_model=List[CountryD])
def get_country():
    records =session.query(CountryModel).all()
    return records

@app.post("/country/")
def create_country(country:CountryD):
    country=CountryModel(nombre=country.nombre)
    session.add(country)
    session.flush()
    return country

#serviceProvider(seria la agencia que brinda los servicios)
@app.get("/serviceprovider/", response_model=List[ServiceProviderD])
def get_service_provider():
    records =session.query(ServiceProviderModel).all()
    return records

@app.post("/serviceprovider/")
def create_service_provider(s_p:ServiceProviderD):
    country=session.query(CountryModel).filter_by(nombre=s_p.country.nombre).first()
    service_provider=ServiceProviderModel(nombre=s_p.nombre,country=country)
    session.add(service_provider)
    session.flush()
    return service_provider


#PROVIDER INSTRUMENT
@app.get("/providerinstrument/", response_model=List[ProviderInstrumentD])
def get_provider_instrument():
    records =session.query(ProviderInstrumentModel).all()
    return records


@app.post("/providerinstrument/")
def create_provider_instrument(p_i:ProviderInstrumentD):
    cl_type=session.query(ClassificationTypeModel).filter_by(type=p_i.clasification.clasification.type).first()
    service_provider=session.query(ServiceProviderModel).filter_by(nombre=p_i.service_provider.nombre).first()

    cl=ClassificationModel(clasification=cl_type,charge=cl_type.charge)
    session.add(cl)
    session.flush()

    country=session.query(CountryModel).filter_by(nombre=p_i.service_provider.country.nombre).first()
    if country==None:
        country=CountryModel(nombre=p_i.service_provider.country.nombre)
        session.add(country)
        session.flush()

    service_provider=session.query(ServiceProviderModel).filter_by(nombre=p_i.service_provider.nombre,country=country).first()
    if service_provider==None:
        service_provider=ServiceProviderModel(nombre=p_i.service_provider.nombre,country=country)
        session.add(service_provider)
        session.flush()

    provider_instrument=ProviderInstrumentModel(name=p_i.name,price=p_i.price,clasification=cl,service_provider=service_provider) 
    session.add(provider_instrument)
    session.flush()

    if p_i.hotel!=None:
        hotel=session.query(HotelModel).filter_by(calle=p_i.hotel.calle,numero=p_i.hotel.numero).first()
        if hotel ==None:
            hotel=HotelModel(calle=p_i.hotel.calle,numero=p_i.hotel.numero)
            session.add(hotel)
            session.flush()

        hpi=HotelProviderInstrumentModel(provider_instrument=provider_instrument,hotel=hotel)
        session.add(hpi)
        session.flush()

    if p_i.travel!=None:
        vh=session.query(VehicleModel).filter_by(matricula=p_i.travel.vehicle.matricula).first()
        if vh==None:
            vh=VehicleModel(type=p_i.travel.vehicle.type,matricula=p_i.travel.vehicle.matricula)
            session.add(vh)
            session.flush()
        
        travel=TravelModel(vehicle=vh)
        session.add(travel)
        session.flush()

        travel_pi=TravelProviderInstrumentModel(provider_instrument=provider_instrument,travel=travel)
        session.add(travel_pi)
        session.flush()

    if p_i.excursion!=None:
        guia=session.query(ExcursionModel).filter_by(legajo=p_i.excursion.legajo).first()
        if guia==None:
            guia=ExcursionModel(nombre=p_i.excursion.nombre,legajo=p_i.excursion.legajo,telefono=p_i.excursion.telefono)
            session.add(guia)
            session.flush()

        excursion_pi=ExcursionProviderInstrumentModel(provider_instrument=provider_instrument,excursion=guia)
        session.add(excursion_pi)
        session.flush()

    return provider_instrument

#hotel
@app.get("/hotel/", response_model=List[HotelD])
def get_hotel():
    try:
        records =session.query(HotelModel).all()
        return records
    except:
        session.rollback()
        return {"errorCode":400,"message":"No se pudo crear el Hotel"}

@app.post("/hotel/")
def create_hotel(hotel:HotelD):
    try:
        hotel=HotelModel(calle=hotel.calle,numero=hotel.numero)
        session.add(hotel)
        session.flush()
        return hotel
    except:
        session.rollback()
        return {"errorCode":400,"message":"No se pudo crear el Hotel"}


#travel
@app.get("/travel/", response_model=List[TravelD])
def get_travel():
    try:
        records =session.query(TravelModel).all()
        return records
    except:
        session.rollback()
        return {"errorCode":400,"message":"No se pudo obtener el listado"}

@app.post("/travel/")
def create_travel(travel:TravelD):
    try:
        vh=VehicleModel(type=travel.vehicle.type,matricula=travel.vehicle.matricula)
        session.add(vh)
        session.flush()

        travel=TravelModel(vehicle=vh)
        session.add(travel)
        session.flush()
        return travel
    except:
        session.rollback()
        return {"errorCode":400,"message":"No se pudo crear el Travel"}

#travel
@app.get("/excursion/", response_model=List[ExcursionD])
def get_travel():
    try:
        records =session.query(ExcursionModel).all()
        return records
    except:
        session.rollback()
        return {"errorCode":400,"message":"No se pudo obtener el listado"}