from django.shortcuts import render # type: ignore

from django.template import loader
from django.http import HttpResponse

def menu(request):
    template = loader.get_template('management/menu.html')
    return HttpResponse(template.render())
    return render(request, 'menu.html')
