from django.shortcuts import render
from sgpa.forms import inputform, inputform2

def home(request):
    if request.method == "POST":
        form1 = inputform(request.POST)
        form2 = inputform2(request.POST)
        #result1=0
        result2=0
       # if form1.is_valid():
           # data = form1.cleaned_data
            #n1 = data.get("input1")
            #n2 = data.get("input2")
            #n3 = data.get("input3")
           # n4 = data.get("input4")
            #n5 = data.get("input5")
           # result1 = round((n1 + n2 + n3 + n4 + n5) / 5, 2)
        if form2.is_valid():
            data = form2.cleaned_data
            n6 = data.get("input6")
            n7 = data.get("input7")
            n8 = data.get("input8")
            n9 = data.get("input9")
            n10 = data.get("input10")
            n11 = data.get("input11")
            n12 = data.get("input12")
            point1 = 30 if n6 == 100 else ((n6 // 10) + 1) * 3
            point2 = 40 if n7 == 100 else ((n7 // 10) + 1) * 4
            point3 = 40 if n8 == 100 else ((n8 // 10) + 1) * 4
            point4 = 30 if n9 == 100 else ((n9 // 10) + 1) * 3
            point5 = 20 if n10 == 100 else ((n10 // 10) + 1) * 2
            point6 = 10 if n11 == 100 else ((n11 // 10) + 1) * 1
            point7 = 10 if n12 == 100 else ((n12 // 10) + 1) * 1
            result2 = round(((point1 + point2 + point3 + point4 + point5 + point6 + point7) / 18), 2)
            return render(request, "index.html", {  'param2': result2, 'form2': form2})
    else:
     
        form2 = inputform2()
    return render(request, "index.html", { 'form2': form2})
