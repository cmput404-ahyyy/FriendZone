from django.db import models

# Create your models here.

class Author(models.Model):
    """ cols
    1, username
    2, pwd
    """
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Post(models.Model):
    """
    1, user id (foreign key)
    2, body/content
    3, Date
    4, Permission
    5, Permitted List
    """
    PERMISSION_OPTIONS = (
        ("M", "me"),
        ("L", "permitted authors"),
        ("F", "my friends"),
        ("FF", "friends of friends"),
        ("FH", "friends on my host"),
        ("P", "public")
    )

    user_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=2000)
    date = models.DateTimeField('date published')
    permission = models.models.CharField(max_length=1, choices=PERMISSION_OPTIONS)
    permitted_authors = models.TextField(null=True) # store permitted author as a JSONED python list

class Image(model.Model):
    """
    1, user id
    2, post id
    3, Permission (non-public)
    """
    img_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    compressed_img = models.TextField(null=True) # store compressed image, that is encoded by JSON

class Comments(model.Model):
    """
    1, post id
    2, user id
    3, content
    """
    cmt_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.models.CharField(max_length=500)

class Friends(models.Model):
    """
    1, author one
    2, author two
    """
    

class Nodes(model.Model):
    """
    1, IP? primary key
    2, permission
    """
