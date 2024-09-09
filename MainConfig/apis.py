
###################################### session 认证 api #####################################################################
from ninja_extra import NinjaExtraAPI
from ninja.security.session import SessionAuth
class DjangoSessionAuth(SessionAuth):
    def authenticate(self, request, token=None):

        return super().authenticate(request,key=token)
    
api_session = NinjaExtraAPI(auth=DjangoSessionAuth(),version='0.0.0')
api_session.add_router("/flashcard", "flashcard.api.router")