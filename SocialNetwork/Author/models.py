from django.db import models

# Create your models here.
class Author(models.Model):
    author_id=models.AutoField(primary_key=True)
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    userName=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    hostName=models.TextField()
    githubUrl=models.TextField()



class FriendRequest(models.Model):
    from_author= models.ForeignKey(Author,on_delete=models.CASCADE, related_name="friend_request_sent")
    to_author=models.ForeignKey(Author,on_delete=models.CASCADE, related_name="friend_request_recieved")
    created=models.DateTimeField()
    regected=models.BooleanField(default=False)

class Friends(models.Model):
    author1=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='friend1')
    author2=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='friend2')
    date=models.DateTimeField()






