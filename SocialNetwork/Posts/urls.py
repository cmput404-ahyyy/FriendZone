from django.urls import path 
from . import views


urlpatterns= [
   path('',views.public, name='public_posts'),
   path('<int:auth_id>/posts/',views.authorPost, name='view_authPosts'),
   path('posts',views.home, name='homefeed'),
   path('posts/<int:post_id>/',views.post, name='view_post'),
   path('posts/<int:post_id>/comments/',views.postComments, name='view_comments')
]