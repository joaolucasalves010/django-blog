from django.urls import path
from blog.views import index, post

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('post/<str:post_title>/<int:id>', post, name="post"),
]
