# Generated by Django 4.1 on 2022-08-20 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_comment_is_reply_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
