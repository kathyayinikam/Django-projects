from django.shortcuts import render
from .sort import sort as ff

def home(request):
    sort = ff()
    return render(request,'index.html',{'param1':sort})

# Create your views here.
