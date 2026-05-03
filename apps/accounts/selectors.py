from .models import *

def get_user_all():
    return User.objects.all()


def get_user_by_id(user_id):
    return User.objects.get(id=user_id)

def get_user_investor():
    return User.objects.filter(user_type="investor")