from django.shortcuts import render
from .add import add as ad
def home(request):
    res=ad()
    return render(request,'base.html',{'param':ad})
# Create your views here.
