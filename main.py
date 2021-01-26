from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from core.config import setting
from api.api import api_router

#declare app
app = FastAPI()
#allow access on all routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()
app.include_router(api_router)

if __name__=="__main__":
    uvicorn.run("main:app",host = setting.HOST, port=setting.PORT)