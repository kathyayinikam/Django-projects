from django.urls import path
from chess1.views import home
urlpatterns = [path('', home),]