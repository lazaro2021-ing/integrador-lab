from typing import List
from package_classifications import ClasificationType
from package_vehicle import VehicleType
from package_vehicle import Vehicle
from package_classifications import ServiceClassification

#preguntar las propiedades
class Country:
    __name:str
    def __init__(self,name:str):
        self.__name=name

class ProvidedInstrument:
    __name:str
    __price:float
    __service_classification:ServiceClassification

    def __init__(self,name:str,price:float):
        self.__name=name
        self.__price=price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def serviceClassification(self):
        return self.__service_classification
        
    @serviceClassification.setter
    def serviceClassification(self,value:ServiceClassification):
        self.__service_classification=value


class ServiceProvider:
    __name:str
    __country:Country
    __instruments:list[ProvidedInstrument]=[]

    def __init__(self,name,country:Country):
        self.__name=name
        self.__country=country

    @property
    def name(self):
        return self.__name  

    @property
    def country(self):
        return self.__country  

    @property
    def instrument(self):
        return self.__instruments 

    def addInstrument(self,instrument:ProvidedInstrument):
        self.__instruments.append(instrument)

class Travel(ProvidedInstrument):
    __vehicle:Vehicle

    def __init__(self, name: str, price: float):
        super().__init__(name, price)

    @property
    def vehicle(self):
        return self.__vehicle

    @vehicle.setter
    def vehicle(self,value:vehicle):
        self.__vehicle=value

   

class Excursion(ProvidedInstrument):
    __nombre:str
    __legajo:str
    __telefono:str

    def __init__(self, name: str, price: float):
        super().__init__(name, price)

    def setExcursion(self,nombre:str,legajo:str,telefono:str):
        self.__nombre=nombre
        self.__legajo=legajo
        self.__telefono=telefono

    @property
    def nombre(self):
        return self.__nombre

    @property
    def legajo(self):
        return self.__legajo

    @property
    def telefono(self):
        return self.__telefono

class Hotel(ProvidedInstrument):
    __direccion:dict()={"calle":"","numero":""}

    def __init__(self, name: str, price: float):
        super().__init__(name, price)

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self,direccion:dict()):
        self.__direccion=direccion

class ServiceProviderBuilder:

    __service_provider:ServiceProvider

    def CreateServiceProvider(self,name:str,country:Country)->ServiceProvider:
        self.__service_provider=ServiceProvider(name,country)
        return  self.__service_provider

    def BuilLodgingInstrument(self,name:str,price:float)->ServiceProvider:
        hotel=Hotel(name,price)
        self.__service_provider.addInstrument(hotel)
        return self.__service_provider

    def BuildExcursionIntrument(self,name:str,price:float)->ServiceProvider:
        excursion=Excursion(name,price)
        self.__service_provider.addInstrument(excursion)
        return self.__service_provider

    def BuidTravelInstrument(self,name:str,price:float)->ServiceProvider:
        travel=Travel(name,price)
        self.__service_provider.addInstrument(travel)
        return self.__service_provider

    def Build():
        pass

if __name__ == "__main__":
    service_classification=ServiceClassification(ClasificationType.EXECUTIVE_CLASS)
    travel_cataratas=Travel("Cataratas",50000)
    travel_cataratas.serviceClassification=service_classification
    bus=Vehicle(VehicleType.BUS,"1234567")
    travel_cataratas.vehicle=bus
    provider_balori=ServiceProvider("Balori",Country("Argentina"))
    provider_balori.addInstrument(travel_cataratas)

    provider=ServiceProviderBuilder()
    provider.CreateServiceProvider("Balori",Country("Argentina"))
    provider.BuidTravelInstrument("Cataratas",50000)
    print(provider.__dict__)


