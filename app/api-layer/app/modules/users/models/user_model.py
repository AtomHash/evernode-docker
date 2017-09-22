"""
    User Model
"""

from evernode.models import UserModel as EverNodeUserModel

class UserModel(EverNodeUserModel):
    """ user db model """

    def __repr__(self, exclude_list=None):
        #exclude_list = ['password', 'created_at']
        return super().__repr__(exclude_list)
