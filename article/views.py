from django.shortcuts import render, render_to_response, get_object_or_404
from django.http.response import HttpResponse
from django.template.loader import get_template
from article.models import Article, Comment

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

def articles(request):
    return render_to_response('articles.html',
        {'articles': Article.objects.all()})

def article(request, id=1):
    article = get_object_or_404(Article, id=id)
    return render_to_response('article.html',
        {'article': article,
         'comments': article.comment_set.all(),
        })

