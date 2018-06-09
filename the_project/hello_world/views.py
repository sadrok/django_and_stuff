from datetime import datetime

from django.shortcuts import render


# Create your views here.
def index(request):
    referrent = 'World'
    now_str = datetime.now().strftime('%A, %Y-%m-%d')
    hello_message = f"Hello {referrent}. It's <strong>{now_str}</strong>"
    q = request.GET.get('q')
    return render(request, 'hello_world/index.html', {
        'title': f'Django Hello App',
        'extra': q,
        'hello_message': hello_message
    })
