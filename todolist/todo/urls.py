from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),

    path('home/',views.home, name="home"),
    path('delete/<int:id>/',views.delete_task,name='delete_task'),
    path('todoform/',views.todoform,name='todoform'),
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
]
