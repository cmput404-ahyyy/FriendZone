from django.db import models
import uuid
import datetime
from Author.models import Author

# Create your models here.
class Post(models.Model):
    PERMISSION_OPTIONS = (
        ("M", "me"),
        ("L", "permitted authors"),
        ("F", "my friends"),
        ("FF", "friends of friends"),
        ("FH", "friends on my host"),
        ("P", "public")
    )

    post_id=models.AutoField(primary_key=True)
    publicationDate=models.DateTimeField('date published')
    content=models.TextField()
    title=models.CharField(max_length=50)
    permission = models.CharField(max_length=2, choices=PERMISSION_OPTIONS, default='P')
    permitted_authors = models.TextField(null=True) # store permitted author as a JSONED python list
    author= models.ForeignKey(Author,on_delete=models.CASCADE,null=True)

class Comment(models.Model):
    comment_id=models.AutoField(primary_key=True)
    comment=models.TextField()
    author=models.ForeignKey(Author, on_delete=models.CASCADE,null=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    published=models.DateTimeField('date published')

class Image(models.Model):
    """
    1, user id
    2, post id
    3, Permission (non-public)
    """
    img_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
    compressed_img = models.TextField(null=True) # store compressed image, that is encoded by JSON