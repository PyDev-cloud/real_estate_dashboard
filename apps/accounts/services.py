from .models import *

def create_user(username,email,password,user_type="investor"):
    user=User(username=username,email=email,user_type=user_type)
    user.set_password(password)
    user.save()
    return user


def user_update(user_id,**data):
    user=User.objects.get(id=user_id)
    for key, value in data.items():
        setattr(user,key,value)
    user.save()
    return user


def user_delete(user_id):
    user=User.objects.get(id=user_id)
    user.delete()