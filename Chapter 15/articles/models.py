from django.db import models
from django.contrib.auth import get_user_model
"""Used for importing custom user model
"""
from django.urls import reverse


class ArticleModel(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail_url", kwargs={"pk": self.id})


class CommentModel(models.Model):
    body = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        #  Tell Django to use `CustomUser` as foreign key
        on_delete=models.DO_NOTHING)
    article = models.ForeignKey(
        ArticleModel,
        # Tell Django to use `ArticleModel` as foreign key
        on_delete=models.CASCADE,
        related_name='comments'
        # While template rendering use 'comments' as context object name
    )

    def __str__(self):
        return self.body[:10]

    def get_absolute_url(self):
        return reverse("article_detail_url", kwargs={"pk": self.article.id})
