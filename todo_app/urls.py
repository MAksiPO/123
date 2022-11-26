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
    path('todo_app/mark_complete/<int:todo_id>', views.mark_complete, name="mark_complete"),
    path('todo_app/mark_close/<int:todo_id>', views.mark_close, name="mark_close"),
    path('todo_app/mark_incomplete/<int:todo_id>', views.mark_incomplete, name="mark_incomplete"),
    path("todo_app/create_form", views.create_todo, name="create"),
]