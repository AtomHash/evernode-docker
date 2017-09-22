"""
    Routes
"""

from .controllers import UserController

routes = [
    #User Routes
        {
            'url': '/user/signin',
            'name': 'user_signin',
            'methods': ['POST'],
            'function': UserController.signin
        }
]
