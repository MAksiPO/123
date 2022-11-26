from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', home_page, name="home"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', login_user, name='logout'),
    path('todo_app/', Todo, name='index'),
    path('todo_app/delete/<int:todo_id>', views.delete, name='delete'),
]