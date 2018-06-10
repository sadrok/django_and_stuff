from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'hello_world/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Django Hello'
        })
        return context

    # def get(self, request):
    #     referrent = 'World'
    #     now_str = datetime.now().strftime('%A, %Y-%m-%d')
    #     hello_message = f"Hello {referrent}. It's <strong>{now_str}</strong>"
    #     return {
    #         'title': f'Django Hello App',
    #         'extra': now_str,
    #         'message': hello_message
    #     }
