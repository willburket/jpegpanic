# Generated by Django 4.1 on 2022-08-20 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_alter_article_author_alter_article_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.TextField(max_length=150),
        ),
    ]
