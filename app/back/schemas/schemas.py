from pydantic import BaseModel
from typing import ForwardRef, List, Optional
from datetime import datetime

class ClassificationTypeD(BaseModel):
    id:Optional[int]
    type:str
    charge:Optional[float]
    class Config:
        orm_mode = True

class ClassificationD(BaseModel):
    id:Optional[int]
    charge:Optional[float]
    clasification:ClassificationTypeD=None
    class Config:
        orm_mode = True

class CountryD(BaseModel):
    id:Optional[int]
    nombre:str
    class Config:
        orm_mode = True

class ServiceProviderD(BaseModel):
    id:Optional[int]
    nombre:str
    country:CountryD=None
    class Config:
        orm_mode = True

class HotelD(BaseModel):
    id:Optional[int]
    calle:str
    numero:int
    class Config:
        orm_mode = True

class VehiculoD(BaseModel):
    id:Optional[int]
    type:int
    matricula:str
    class Config:
        orm_mode = True

class TravelD(BaseModel):
    id:Optional[int]
    vehicle:VehiculoD
    class Config:
        orm_mode = True

class ExcursionD(BaseModel):
    id:Optional[int]
    nombre:str
    legajo:str
    telefono:str
    class Config:
        orm_mode = True

class ProviderInstrumentD(BaseModel):
    id:Optional[int]
    name:str
    price:float
    clasification:ClassificationD=None
    service_provider:ServiceProviderD=None
    hotel:Optional[HotelD]=None
    travel:Optional[TravelD]=None
    excursion:Optional[ExcursionD]=None
    class Config:
        orm_mode = True

class HotelProviderInstrumentD(BaseModel):
    id:Optional[int]
    provider_instrument:ProviderInstrumentD=None
    hotel:HotelD=None
    class Config:
        orm_mode = True

class TravelProviderInstrumentD(BaseModel):
    id:Optional[int]
    provider_instrument:ProviderInstrumentD=None
    travel:TravelD=None
    class Config:
        orm_mode = True

class ExcursionProviderInstrumentD(BaseModel):
    id:Optional[int]
    provider_instrument:ProviderInstrumentD=None
    excursion:ExcursionD=None
    class Config:
        orm_mode = True

class StateTypeModelD(BaseModel):
    id:Optional[int]
    name:str
    class Config:
        orm_mode = True  

class PackageModelD(BaseModel):
    id:Optional[int]
    is_composite:bool
    clasification:ClassificationD=None
    class Config:
        orm_mode = True

class PackageModelDTO(BaseModel):
    id:Optional[int]
    is_composite:bool
    clasification:ClassificationD=None
    provider_instruments:List[ProviderInstrumentD]
    class Config:
        orm_mode = True

class PackageProviderInstrumentModelD(BaseModel):
    id:Optional[int]
    id_provider_instrument:int
    id_package:int
    class Config:
        orm_mode = True

class StateModelD(BaseModel):
    id:Optional[int]
    state:StateTypeModelD=None
    name:str
    date:datetime
    couses:Optional[str]
    date_begin:Optional[datetime]
    date_end:Optional[datetime]
    package_provider_instrument:PackageProviderInstrumentModelD=None
    class Config:
        orm_mode = True


