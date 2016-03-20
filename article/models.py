from django.db import models

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
    text = models.TextField(verbose_name='Текст комментария')
    article = models.ForeignKey(Article)

    class Meta:
        db_table = 'comments'
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

