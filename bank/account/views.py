# myapp/views.py

from django.shortcuts import render
from .forms import NameForm
import random
def get_name(request):
    name = None
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dropdown=form.cleaned_data['dropdown']
            ac = random.randint(10**9, 10**18)
            
    else:
        form = NameForm()

    return render(request, 'bank/name_form.html', {'form': form, 'name': name, 'drop': dropdown,'ac':ac})
