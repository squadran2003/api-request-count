from .models import ApiRequest
from django.utils import timezone

def requestCount(func):
    def run(view,request,**kwargs):
        write_to_db(request.user,func.__doc__)
        return func(view,request,**kwargs)
    return run

def write_to_db(*args):
    user,view_name = args
    view_name.strip()
    # find request where user and view name match

    ApiRequest.objects.create(user=user,view_name=view_name)
    