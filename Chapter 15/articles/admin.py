from django.contrib import admin
from .models import ArticleModel, CommentModel


class CommentInline(admin.StackedInline):
    """Show `CommentModel` on related 
        objects, by foreign key reference
    """
    model = CommentModel
    extra = 0
    """Show only exsisting objects
    """


class CommentTabular(admin.TabularInline):
    """Show `CommentModel` on related 
        objects, by foreign key reference
    """
    model = CommentModel
    extra = 0
    """Show only exsisting objects
    """


class ArticleAdmin(admin.ModelAdmin):
    """Add capability to admin portal 
    """
    inlines = [
        CommentTabular,
    ]


admin.site.register(ArticleModel, ArticleAdmin)
"""Register capability to ArticleModel
"""
admin.site.register(CommentModel)
