from django.contrib import admin

from article.models import Article, Comment

# Register your models here.
class ArticleInline(admin.StackedInline):
    model = Comment
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'text','date']
    inlines = [ArticleInline]
    list_filter = ['date']


admin.site.register(Article, ArticleAdmin)
