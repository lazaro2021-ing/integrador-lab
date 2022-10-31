from enum import Enum

class VehicleType(Enum):
    PLANE:1
    CRUISE:2
    BUS:3
    TRAIN:4

class Vehicle:
    __type:VehicleType
    __matricula:str

    def __init__(self,type:VehicleType,matricula:str):
        self.__matricula=matricula
        self.__type=type

    @property
    def type(self):
        return self.__type

    @property
    def matricula(self):
        return self.__matricula
        




