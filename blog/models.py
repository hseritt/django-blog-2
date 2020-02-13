from django.contrib.auth.models import User
from django.db import models
from markdownx.models import MarkdownxField


class Category(models.Model):
    name = models.CharField('Category', max_length=50, unique=True)
    description = models.TextField('Description', null=True, blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image_file = models.ImageField(
        'Image', upload_to='static/img/%Y/%m/%d'
    )

    def __str__(self):
        return self.image_file.url


class Article(models.Model):
    title = models.CharField('Title', max_length=100, unique=True)
    content = MarkdownxField('Content')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    published = models.DateTimeField()
    tweet_article = models.BooleanField(default=False)
    categories = models.ManyToManyField('Category')
    images = models.ManyToManyField('Image', blank=True)
    slugged_title = models.SlugField(max_length=100, unique=True)
    needs_updating = models.BooleanField(default=False)
    update_description = models.TextField(null=True, blank=True)
    is_updated = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Article Comment'
        verbose_name_plural = 'Article Comments'

    def __str__(self):
        return f'{self.article.title}: comment at {self.created}'


class Message(models.Model):
    full_name = models.CharField('Full Name', max_length=30)
    email = models.EmailField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} {self.email}'
