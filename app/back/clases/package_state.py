from datetime import datetime
from typing import List

class PackageState:
    __name:str
    __date:datetime
    #__package:StatefullPackage

    def __init__(self,name:str,date:datetime):
        self.__name=name
        self.__date=date

class StatefullPackage:
    __states=[]#PackageState

    @property
    def states(self):
        return self.__states

    @property
    def wasReschuduled(self):
        pass

    @property
    def currentState(self):
        return self.__states[-1]

    @currentState.setter
    def currentState(self,value:PackageState):
        self.__states.append(value)

    def changeState(self,state:PackageState):
        dict_state={'Created':[Scheduled.__class__.__name__,Canceled.__class__.__name__],
                    'Scheduled':[Holded.__class__.__name__,Active.__class__.__name__],
                    'Holded':[Scheduled.__class__.__name__,Canceled.__class__.__name__],
                    'Canceled':[],
                    'Active':[Completed.__class__.__name__,Canceled.__class__.__name__],
                    'Completed':[],
                    }
        if len(self.__states)>0:
            if  state in dict_state[self.__states[-1].__class__.__name__]:
                self.__states.append(state)
            else:
                print(f"Error no se puede cambiar el estado a {state} estando en {self.__states[-1]} ")
        else:
            if state.__class__.__name__=="Created":
                self.__states.append(state)

class Created(PackageState):
    def __init__(self, name: str, date: datetime):
        super().__init__(name, date)

class Active(PackageState):
    def __init__(self, name: str, date: datetime):
        super().__init__(name, date)

class Completed(PackageState):
    def __init__(self, name: str, date: datetime):
        super().__init__(name, date)

class Canceled(PackageState):
    __cause:str

    def __init__(self,name: str, date: datetime,cause:str):
        super().__init__(name, date)
        self.__cause=cause

class Holded(PackageState):
    __cause:str

    def __init__(self,name: str, date: datetime,cause:str):
        super().__init__(name, date)
        self.__cause=cause

class Scheduled(PackageState):
    __start:datetime
    __end:datetime

    def __init__(self,name: str, date: datetime,start:datetime,end:datetime):
        super().__init__(name, date)
        self.__start=start
        self.__end=end

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end
