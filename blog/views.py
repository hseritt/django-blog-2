from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .config import COMMON_CONTEXT
from .models import Article, Message, Component


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

    def get(self, request, slugged_title):
        view_context = {
            'article': Article.objects.get(slugged_title=slugged_title),
        }
        view_context.update(COMMON_CONTEXT)
        return render(request, self.TEMPLATE, view_context)
