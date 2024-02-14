from django.shortcuts import render
import chess1.modchess2 as mc
import os

def home(request):
    html_content = [1,2,3,4]
    coins=["&#9820","&#9820","&#9822","&#9821","&#9819","&#9818","&#9821","&#9822","&#9820"]
    return render(request, 'index.html', {'param1': html_content,'param2':coins})

# Create your views here.