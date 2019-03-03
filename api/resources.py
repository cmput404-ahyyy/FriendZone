from tastypie.resources import ModelResource
from .models import *
# delete this later. for temporary authorization 
from tastypie.authorization import Authorization

class AuthorResource(ModelResource):
    class Meta:
        queryset = Author.objects.all()
        resource_name = 'author'
        # excludes = ['firstName', 'lastName', 'hostName', 'password']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        # delete this later. for temporary authorization
        authorization = Authorization()