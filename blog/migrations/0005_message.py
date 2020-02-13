# Generated by Django 3.0.2 on 2020-02-12 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_is_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
