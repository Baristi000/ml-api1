from fastapi import APIRouter, Body
from functions import learn_01
from core.config import setting

router = APIRouter()

@router.post('/train_bin')
def train_bin(
    data:list  = Body(...),
    label:list = Body(...),
    name:str   = Body(...),
    epochs:int = Body(...)
):
    return learn_01.train_bin(data,label,name, epochs)

@router.post('/predict_bin')
def predict_bin(
    data:list  = Body(...),
    name:str  = Body(...)
):
    return learn_01.predict_bin(data, name)

@router.get('/agents_number')
def agents_number():
    agent_name = []
    for name,value in setting.var_learn1.items():
        agent_name.append(name)
    return{'agents':agent_name}