from fastapi import APIRouter

from api import learn_bin_api

api_router = APIRouter()

api_router.include_router(learn_bin_api.router,prefix='/BinaryAPI',tags=['Binary'])
