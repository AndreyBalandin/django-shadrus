from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)

    class Meta:
        db_table = 'articles'
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title


class Comment(models.Model):
    date = models.DateTimeField()  # (blank=True, null=True)
    text = models.TextField(verbose_name='Текст комментария')
    article = models.ForeignKey(Article)
    author  = models.ForeignKey(User)

    class Meta:
        db_table = 'comments'
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

