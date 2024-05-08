from django import forms 

class inputform(forms.Form):
    input1=forms.FloatField(min_value=1, max_value=10, label="1st sem SGPA")
    input2=forms.FloatField(min_value=1, max_value=10, label="2nd sem SGPA")
    input3=forms.FloatField(min_value=1, max_value=10, label="3rd sem SGPA")
    input4=forms.FloatField(min_value=1, max_value=10, label="4th sem SGPA")
    input5=forms.FloatField(min_value=1, max_value=10, label="5th sem SGPA")

class inputform2(forms.Form):  
    input6=forms.FloatField(min_value=1, max_value=100, label="ATC(21CS51)")
    input7=forms.FloatField(min_value=1, max_value=100, label="CN(21CS52)")
    input8=forms.FloatField(min_value=1, max_value=100, label="DBMS(21CS53)")
    input9=forms.FloatField(min_value=1, max_value=100, label="AIML(21CS54)")
    input10=forms.FloatField(min_value=1, max_value=100, label="RMIPR(21CS55)")
    input11=forms.FloatField(min_value=1, max_value=100, label="CIV(21CS56)")
    input12=forms.FloatField(min_value=1, max_value=100, label="C#(21CSL582)")
