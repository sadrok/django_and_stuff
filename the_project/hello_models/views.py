from django.shortcuts import render

# Create your views here.
from hello_models.models import AccessRecord


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    context = {
        'title': 'Django Models', 'access_records': webpages_list,
    }
    return render(request, 'hello_models/index.html', context)
