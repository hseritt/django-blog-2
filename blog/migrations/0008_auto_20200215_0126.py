# Generated by Django 3.0.3 on 2020-02-15 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200213_1554'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address'),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='full_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Your Name'),
        ),
        migrations.AlterField(
            model_name='articlecomment',
            name='content',
            field=models.TextField(verbose_name='Comment'),
        ),
    ]
