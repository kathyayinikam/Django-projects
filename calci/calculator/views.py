from django.shortcuts import render
from calculator.forms import inputform
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("num1")
            n2=data.get("num2")
            n3=data.get("num3")
            if(n3=='+'):
                    result=n1+n2
            elif(n3=='-'):
                result=n1-n2
            elif(n3=='*'):
                result=n1*n2
            elif(n3=='/'):
                if(n2==0):
                    result=n1/n2
                
            
            return render(request,'index.html',{'param4':result,'param3':n2,'param1':n1,'param2':n3,'form':form1})
    else:
        form1=inputform()
    return render(request,'index.html',{'form':form1})
