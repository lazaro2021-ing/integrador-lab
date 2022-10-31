from package_classifications import ClasificationType
from package_providers import ProvidedInstrument
from package_classifications import ServiceClassification

class AbstractPackage:
    __classification:ServiceClassification
    __isComposite:bool=False

    def __init__(self,classification):
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

    @property
    def instrument(self):
        return self.__instrument

class CompositePackage(AbstractPackage):
    __children:list(AbstractService)

    def __init__(self, classification):
        super().__init__(classification)

    def addService(self,service:AbstractService):
        self.__children.append(service)

    def removeService(self,service:AbstractService):
        self.__children=[serv for serv in self.__children if serv!=service]

    @property
    def children(self):
        return self.__children