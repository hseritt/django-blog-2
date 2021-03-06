from django.contrib.auth.models import User
from django.db import models
from markdownx.models import MarkdownxField


class Category(models.Model):
    name = models.CharField('Category', max_length=50, unique=True)
    is_active = models.BooleanField('Active', default=True)
    description = models.TextField('Description', null=True, blank=True)
    icon = models.ImageField(
        'Icon', upload_to='static/img/%Y/%m/%d', null=True, blank=True
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Image(models.Model):
    image_file = models.ImageField(
        'Image', upload_to='static/img/%Y/%m/%d'
    )

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

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
    view_count = models.IntegerField('View Count', default=0)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return f'{self.title} - Views: {self.view_count}'


class ArticleComment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    content = models.TextField('Comment')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(
        'Your Name', max_length=30
    )
    email = models.EmailField('Email Address', null=True, blank=True)

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

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'{self.full_name} {self.email} at {self.created}'


class Component(models.Model):
    name = models.CharField('Name', max_length=50, unique=True)
    content = models.TextField('Content')
    is_visible = models.BooleanField('Visible?', default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Component'
        verbose_name_plural = 'Components'

    def __str__(self):
        return self.name


class Tweet(models.Model):
    message = models.CharField('Message', max_length=250, unique=True)
    is_enabled = models.BooleanField('Enabled', default=False)

    def __str__(self):
        return self.message
