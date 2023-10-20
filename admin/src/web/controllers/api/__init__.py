from flask import Blueprint
from src.web.controllers.api.logged_user import api_logged_user
from src.web.controllers.api.service import api_services
from src.web.controllers.api.institution import api_institutions
from src.web.controllers.api.auth import api_auth

api_blueprint = Blueprint("api", __name__, url_prefix="/api")

api_blueprint.register_blueprint(api_logged_user)
api_blueprint.register_blueprint(api_services)
api_blueprint.register_blueprint(api_institutions)
api_blueprint.register_blueprint(api_auth)