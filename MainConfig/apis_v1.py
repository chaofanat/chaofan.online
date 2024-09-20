#ninjia api
from typing import Any
from django.http import HttpRequest
from ninja.security import HttpBearer
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTBaseAuthentication
from ninja_extra import NinjaExtraAPI


############################################jwt 认证api##############################
#jwt 认证器
from django.contrib.auth import get_user_model
class JWTTokenUser(HttpBearer,JWTBaseAuthentication):
    def __init__(self) -> None:
        super().__init__()
        self.user_model = get_user_model()
    def authenticate(self, request: HttpRequest, token: str) -> Any | None:
        return super().jwt_authenticate(request, token)
        
    





api = NinjaExtraAPI(auth=JWTTokenUser(),csrf=False,version='1.0.0') 
api.register_controllers(NinjaJWTDefaultController)




####################################   测试api    ###################################################################
@api.post("/bearer")
def bearer(request):
    return {'message': 'hello'}

# @api.get("/add")
# def add(request, a: int, b: int):
#     return {"result": a + b}

#####################################################################################################################
# 注册路由,应用api转发
api.add_router("/appindex", "appIndex.apis.router")
api.add_router("/flashcard", "flashcard.api_v1.router")
api.add_router("/objectstorage", "appObjectStorage.apis.router")



