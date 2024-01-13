from django import forms
class inputform(forms.Form):
    num1=forms.IntegerField(min_value=1,max_value=1000000,label="Enter first number")
    num2=forms.IntegerField(min_value=1,max_value=1000000,label="Enter second number")
    num3=forms.CharField(label="Enter the operator")
    