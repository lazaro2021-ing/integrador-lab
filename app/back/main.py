from fastapi import FastAPI
from models.models import *
from db_conect import session
from typing import List
from schemas.schemas import *

app = FastAPI()

#classification type
@app.get("/classificationtypes/", response_model=List[ClassificationTypeD])
def get_clasification_types():
    records =session.query(ClassificationTypeModel).all()
    return records

@app.post("/classificationtypes/")
def create_classification_types(type:ClassificationTypeD):
    session.add(ClassificationTypeModel(type=type.type,charge=type.charge))
    session.commit()
    return type
   
#classification
@app.get("/classification/", response_model=List[ClassificationD])
def get_clasification():
    records =session.query(ClassificationModel).all()
    return records

@app.post("/classification/")
def create_classification_types(type:ClassificationD):
    cl=session.query(ClassificationTypeModel).filter_by(type=type.clasification.type).first()
    session.add(ClassificationModel(clasification=cl,charge=cl.charge))
    session.commit()
    return type
