from django.forms import ModelForm
from .models import ArticleComment


class ArticleCommentForm(ModelForm):

    class Meta:
        model = ArticleComment
        fields = 'full_name', 'email', 'content'
