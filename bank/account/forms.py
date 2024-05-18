from django import forms

class NameForm(forms.Form):
    name=forms.CharField(label='Enter your name',max_length=100)
    choice=[
        ('Savings','Savings'),
        ('Joint account','Joint account'),
        ('Checking Account','Checking Account'),
    ]
    dropdown=forms.ChoiceField(choices=choice)
    