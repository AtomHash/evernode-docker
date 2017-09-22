"""
    User Controller
"""
from flask import current_app
from evernode.classes import Auth, JsonResponse, Session, JWT, User
from evernode.decorators import load_middleware
from ..models import UserModel

class UserController:
    """ user route controller """

    @staticmethod
    def signin():
        """ user signin """
        signin = User().signin()
        if signin is None:
            return JsonResponse(400).create()
        return JsonResponse(200, None, signin).create()
