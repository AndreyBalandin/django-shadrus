from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response

# Create your views here.

def basic_one(request):
    view = 'basic_one'
    html = '<html><body>This is {}</body></html>'.format(view)
    return HttpResponse(html)

def template_two(request):
    name = 'template_two'
    html = get_template('my_template.html').render({'name': name})
    return HttpResponse(html)

def template_three(request):
    name = 'template_three'
    return render_to_response('my_template.html', {'name': name})
