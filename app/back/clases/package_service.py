from package_classifications import ClasificationType,ServiceClassification
from package_providers import ProvidedInstrument,ServiceProviderBuilder,Country
from package_vehicle import Vehicle,VehicleType
from typing import List
from package_state import *
from datetime import datetime


class AbstractPackage(StatefullPackage):
    __classification:ServiceClassification
    __isComposite:bool=False

    def __init__(self,classification):
        super().__init__()
        self.__classification=classification

    @property
    def classification(self)->ServiceClassification:
        return self.__classification

    @property
    def isComposite(self)->bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self,value):
        self.__isComposite=value


class AbstractService(AbstractPackage):
    __instrument:ProvidedInstrument

    def __init__(self,classification:ClasificationType,instrument:ProvidedInstrument):
        super().__init__(classification)
        if self.classification == instrument.serviceClassification.classification:
            self.__instrument=instrument
        else:
            print("Error las clasificaciones tienen que ser iguales")

    @property
    def instrument(self):
        return self.__instrument

class CompositePackage(AbstractPackage):
    __children=[]#AbstractService

    def __init__(self, classification:ClasificationType):
        super().__init__(ServiceClassification(classification))

    def addService(self,service:AbstractService):
        if service.classification == self.classification.classification:
            self.__children.append(service)
        else:
            print("Error tienen que tener la misma clasificacion.")

    def removeService(self,service:AbstractService):
        self.__children=[serv for serv in self.__children if serv!=service]

    @property
    def children(self):
        return self.__children


if __name__ == "__main__":

    provider=ServiceProviderBuilder()
    provider.CreateServiceProvider("Balori",Country("Argentina"))
    bus=Vehicle(VehicleType.BUS,"1234567")
    service_provider=provider.BuidTravelInstrument("Cataratas",25000,bus,ClasificationType.EXECUTIVE_CLASS)
    provider_instrument=service_provider.instrument[0]
    print(provider_instrument.__dict__)

    abstract_service=AbstractService(ClasificationType.EXECUTIVE_CLASS,provider_instrument)

    composite_package=CompositePackage(ClasificationType.EXECUTIVE_CLASS)
    composite_package.addService(abstract_service)
    composite_package.children[0].changeState(Created("lzr",datetime.now()))
    composite_package.children[0].changeState(Scheduled("lzr",datetime.now(),datetime.strptime("08/05/2023", '%m/%d/%Y'),datetime.strptime("09/05/2025", '%m/%d/%Y')))
    composite_package.children[0].changeState(Canceled("lzr",datetime.now(),"no tengo dinero"))
    
    print(composite_package.states)
    print(composite_package.currentState.__class__.__name__=="Active")
