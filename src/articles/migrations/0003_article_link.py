# Generated by Django 3.2.14 on 2022-07-17 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.TextField(default='null'),
        ),
    ]
