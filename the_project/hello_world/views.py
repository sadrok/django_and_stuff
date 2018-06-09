from datetime import datetime

from django.shortcuts import render


# Create your views here.
def index(request):
    referrent = 'World'
    now_str = datetime.now().strftime('%A, %Y-%m-%d')
    hello_message = f"Hello {referrent}. It's <strong>{now_str}</strong>"

    return render(request, 'hello_world/index.html', {
        'title': 'Django Hello App', 'hello_message': hello_message
    })
