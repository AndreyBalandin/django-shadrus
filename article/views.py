from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.views.decorators.http import require_POST
from django.contrib import auth

from article.models import Article, Comment
from article.forms import CommentForm

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
    return render(request, 'articles.html', {
        'articles': Article.objects.all(),
        'username': auth.get_user(request).username,
        })

def article(request, id=1):
    article = get_object_or_404(Article, id=id)
    return render(request, 'article.html', {
        'article': article,
        'comments': article.comment_set.all(),
        'form': CommentForm(),
        'username': auth.get_user(request).username,
        })

def addlike(request, id):
    likes_article_id = list(eval(request.COOKIES.get('likes_article_id', '[]')))
    if id in likes_article_id:  # если статью уже лайкали, то не прибавлять лайк
        return redirect('/')
    article = get_object_or_404(Article, id=id)
    article.likes += 1
    article.save()
    # поставить куку с нажатым лайком
    response = redirect('/')
    response.set_cookie('likes_article_id', likes_article_id + [id])
    return response

@require_POST
def addcomment(request, id):
    if 'pause' not in request.session:
        article = get_object_or_404(Article, id=id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            request.session.set_expiry(60)  # кука с сессией будет актуальна 1 минуту
            request.session['pause'] = True # дополнительное значение в сессии
    return redirect('/articles/get/{}/'.format(id))
