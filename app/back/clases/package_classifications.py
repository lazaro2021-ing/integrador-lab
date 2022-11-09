from enum import Enum

class ClasificationType(Enum):
    FIRST_CLASS=1
    EXECUTIVE_CLASS=2
    ECONOMY_CLASS=3

class ServiceClassification:
    __charge:float
    __classification:ClasificationType
    __classification_to_charge={ClasificationType.FIRST_CLASS    :1.45,
                                ClasificationType.EXECUTIVE_CLASS:1.15,
                                ClasificationType.ECONOMY_CLASS  :1.05}

    def __init__(self,classification:ClasificationType):
        self.__charge=self.__classification_to_charge[classification]
        self.__classification=classification

    @property
    def charge(self):
        return self.__charge

    @property
    def classification(self):
        return self.__classification
    
