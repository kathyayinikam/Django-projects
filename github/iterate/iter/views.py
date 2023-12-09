# views.py
from django.shortcuts import render

def rep():
    list1 = []
    set1 = set()
    for i in range(7):
        list1.append(i)
        set1.add(tuple(list1))
    return set1

def repc():
    list2 = []
    set2 = set()
    for j in range(50//7):
        list2.append(j)
        set2.add(tuple(list2))
    return set2
def days():
    set3=set()
    list3=[" ","Mon","  ","Wedn","  ","Fri","  "]
    set3.add(tuple(list3))
    return list3
def home(request):
    res = rep()
    res2 = repc()
    day=days()
    return render(request, 'index.html', {'param1': res, 'param2': res2,'param3':day})
