from django.urls import path
from blog.views import index, post, register, login_view, logout_view

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('post/<str:post_author>/<int:id>', post, name="post"),
    path('register', register, name="register"),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
]
