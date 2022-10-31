class Country:
    def __init__(self):
        pass

class ProvidedInstrument:
    __name:str
    __price:float

    def __init__(self,name:str,price:float):
        self.__name=name
        self.__price=price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

class ServiceProvider:
    __name:str
    __country:Country
    __instrument:list(ProvidedInstrument)

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
        return self.__instrument  
        