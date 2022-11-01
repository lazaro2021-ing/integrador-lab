from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey

Base = declarative_base()

class ClassificationTypeModel(Base):
    __tablename__ = 'ServiceClassificationType'
    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)
    charge=Column(Float)
    
  

class ClassificationModel(Base):
    __tablename__ = 'ServiceClassification'
    id = Column(Integer, primary_key=True)
    charge=Column(Float)
    fk_classification_type = Column(Integer, ForeignKey("ServiceClassificationType.id"))
    fk_provider_instrument = Column(Integer, ForeignKey("ProviderInstrument.id"))
    clasification = relationship("ClassificationTypeModel")
    provider_instrument = relationship("ProviderInstrumentModel")

class ProviderInstrumentModel(Base):
    __tablename__ = 'ProviderInstrument'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    price=Column(Float)
    fk_travel = Column(Integer, ForeignKey("Travel.id"))
    travel=relationship("TravelModel")

class VehicleModel(Base):
    __tablename__ = 'Vehicle'
    id = Column(Integer, primary_key=True)
    type = Column(Integer, nullable=False)
    matricula = Column(String(50), nullable=False)

class TravelModel(Base):
    __tablename__ = 'Travel'
    id = Column(Integer, primary_key=True)
    fk_vehicle = Column(Integer, ForeignKey("Vehicle.id"))
    vehicle=relationship("VehicleModel")



