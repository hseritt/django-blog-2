from django.urls import path
from .views import IndexView, ArticleView

urlpatterns = [
    path('', IndexView.as_view()),
    path('article/<str:slugged_title>/', ArticleView.as_view()),
]
