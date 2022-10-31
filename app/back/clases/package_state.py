from importlib.resources import Package
from datetime import datetime

class Created:
    def __init__(self,package:Package):
        pass

class Active:
    def __init__(self,package:Package):
        pass

class Completed:
    def __init__(self,package:Package):
        pass

class Canceled:
    __cause:str

    def __init__(self,package:Package,cause:str):
        self.__cause=cause

class Holded:
    __cause:str

    def __init__(self,package:Package,cause:str):
        self.__cause=cause

class Scheduled:
    __start:datetime
    __end:datetime

    def __init__(self,package:Package,start:datetime,end:datetime):
        self.__start=start
        self.__end=end

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

class PackageState:
    __name:str
    __date:datetime

    def __init__(self):
        pass