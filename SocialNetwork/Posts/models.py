from django.db import models
import uuid
import datetime
from Author.models import Author

# Create your models here.
class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    publicationDate=models.DateTimeField('date published')
    content=models.TextField()
    title=models.CharField(max_length=50)
    visibility=models.CharField(max_length=50)
    author= models.ForeignKey(Author,on_delete=models.CASCADE)
