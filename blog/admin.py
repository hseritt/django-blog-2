from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import (
    Article, ArticleComment, Category, Image, Message, Component
)


class ArticleModelAdmin(MarkdownxModelAdmin):
    """Admin model including markdown field for textarea."""
    prepopulated_fields = {'slugged_title': ('title',)}


admin.site.register(Article, ArticleModelAdmin)
admin.site.register(ArticleComment)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Message)
admin.site.register(Component)
