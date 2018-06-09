from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Django Forms'
    }
    return render(request, 'hello_forms/index.html', context=context)