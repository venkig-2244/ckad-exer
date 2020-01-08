from flash_restful import Api
from app import flaskAppInstance
from .ProjectAPI import ProjectAPI

restServerInstance = Api(flashAppInstance)

restServerInstance.add_resource(ProjectAPI,"/")

