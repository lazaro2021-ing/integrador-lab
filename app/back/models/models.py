from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import Column, Integer, String, Float,Boolean,DateTime
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
    clasification = relationship("ClassificationTypeModel")

class ProviderInstrumentModel(Base):
    __tablename__ = 'ProviderInstrument'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    price=Column(Float)

    fk_classification_type = Column(Integer, ForeignKey("ServiceClassification.id"))
    clasification = relationship("ClassificationModel")

    fk_service_provider = Column(Integer, ForeignKey("ServiceProvider.id"))
    service_provider=relationship("ServiceProviderModel")

class StateTypeModel(Base):
    __tablename__ = 'StateType'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)



class PackageModel(Base):
    __tablename__ = 'Package'
    id = Column(Integer, primary_key=True)
    is_composite = Column(Boolean, nullable=False)
    fk_classification_type = Column(Integer, ForeignKey("ServiceClassification.id"))
    clasification = relationship("ClassificationModel")

class PackageProviderInstrumentModel(Base):
    __tablename__ = 'PackageProviderInstrument'
    id = Column(Integer, primary_key=True)

    fk_provider = Column(Integer, ForeignKey("ProviderInstrument.id"))
    provider_instrument=relationship("ProviderInstrumentModel")

    fk_package = Column(Integer, ForeignKey("Package.id"))
    package=relationship("PackageModel")

class StateModel(Base):
    __tablename__ = 'State'
    id = Column(Integer, primary_key=True)
    fk_state_type = Column(Integer, ForeignKey("StateType.id"))
    state = relationship("StateTypeModel")
    name = Column(String(50), nullable=False)
    date = Column(DateTime, nullable=False)
    couses = Column(String(200), nullable=True)
    date_begin = Column(DateTime, nullable=True)
    date_end = Column(DateTime, nullable=True)
    fk_package_provider_instrument= Column(Integer, ForeignKey("PackageProviderInstrument.id"))
    package_provider_instrument = relationship("PackageProviderInstrumentModel")



   
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

    fk_provider = Column(Integer, ForeignKey("ProviderInstrument.id"))
    provider=relationship("ProviderInstrumentModel")

class ExcursionModel(Base):
    __tablename__ = 'Excursion'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    legajo = Column(String(50), nullable=False)
    telefono = Column(String(50), nullable=False)

    fk_provider = Column(Integer, ForeignKey("ProviderInstrument.id"))
    provider=relationship("ProviderInstrumentModel")

class HotelModel(Base):
    __tablename__ = 'Hotel'
    id = Column(Integer, primary_key=True)
    calle = Column(String(50), nullable=False)
    numero = Column(Integer, nullable=False)

    fk_provider = Column(Integer, ForeignKey("ProviderInstrument.id"))
    provider=relationship("ProviderInstrumentModel")

class CountryModel(Base):
    __tablename__ = 'Country'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)


class ServiceProviderModel(Base):
    __tablename__ = 'ServiceProvider'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)

    fk_country = Column(Integer, ForeignKey("Country.id"))
    country=relationship("CountryModel")