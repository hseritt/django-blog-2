from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .config import COMMON_CONTEXT
from .forms import ArticleCommentForm
from .models import (
    Article, Message, Component, ArticleComment, Category
)


class IndexView(View):
    TEMPLATE = 'blog/index.html'

    def get(self, request):
        view_context = {

            'article_list': Article.objects.filter(
                is_published=True
            ).order_by('-published')[:10],

            'updated_article_list': Article.objects.filter(
                is_updated=True
            ).order_by('-modified')[:10],

            'all_article_list': Article.objects.all(),

            'bio': Component.objects.get(name='bio'),

            'intro': Component.objects.get(name='intro'),

            'categories': Category.objects.filter(
                is_active=True).order_by('name'),
        }
        view_context.update(COMMON_CONTEXT)
        return render(request, self.TEMPLATE, view_context)

    def post(self, request):
        full_name = request.POST['full_name']
        email = request.POST['email']
        comment = request.POST['comment']
        Message.objects.create(
            full_name=full_name, email=email, comment=comment
        )
        return HttpResponseRedirect('/#')


class ArticleView(View):
    TEMPLATE = 'blog/article.html'

    def increment_view_count(self, article):
        article.view_count += 1
        article.save()

    def get(self, request, slugged_title):
        article = Article.objects.get(slugged_title=slugged_title)
        self.increment_view_count(article)
        comment_form = ArticleCommentForm()
        view_context = {
            'article': article,
            'comments': ArticleComment.objects.filter(article=article),
            'comment_form': comment_form,
        }
        view_context.update(COMMON_CONTEXT)
        return render(request, self.TEMPLATE, view_context)
