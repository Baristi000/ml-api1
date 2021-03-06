from fastapi import APIRouter, Body
from functions import learn_01
from core.config import setting

router = APIRouter()

@router.post('/train_bin')
def train_bin(
    data:list  = Body(...),
    label:list = Body(...),
    name:str   = Body(...),
    percent:float = Body(...)
):
    return learn_01.train_bin(data,label,name, percent)

@router.post('/predict_bin')
def predict_bin(
    data:list  = Body(...),
    name:str  = Body(...)
):
    return learn_01.predict_bin(data, name)

@router.get('/agents_list')
def agents_list():
    agent_name = []
    for name,value in setting.var_learn1.items():
        agent_name.append(name)
    return{'agents':agent_name}

@router.post('/delete_agent')
def delete_agent(name:str = Body(...)):
    try:
        del setting.var_learn1[name]
    except:
        return{'status':'error'}
    return{'status':'successed'}