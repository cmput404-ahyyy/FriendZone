from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    author_id=models.AutoField(primary_key=True)
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    userName=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    hostName=models.CharField(max_length=100)
    githubUrl=models.URLField()



class FriendRequest(models.Model):
    from_author= models.ForeignKey(Author,on_delete=models.CASCADE, related_name="friend_request_sent",null=True)
    to_author=models.ForeignKey(Author,on_delete=models.CASCADE, related_name="friend_request_recieved",null=True)
    created=models.DateTimeField()
    regected=models.BooleanField(default=False)

class Friends(models.Model):
    author1=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='friend1',null=True)
    author2=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='friend2',null=True)
    date=models.DateTimeField()






