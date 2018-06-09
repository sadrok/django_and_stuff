from django.shortcuts import render
from . import forms


# Create your views here.
def index(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            return render(request, 'hello_forms/result.html', context={
                'title': 'Django Forms - Submitted',
                'result': form.cleaned_data
            })

    context = {
        'title': 'Django Forms',
        'form': form
    }
    return render(request, 'hello_forms/index.html', context=context)
