from django.contrib import admin
from .models import ArticleModel, CommentModel

admin.site.register(ArticleModel)
admin.site.register(CommentModel)
