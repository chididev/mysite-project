# Generated by Django 3.2.4 on 2021-06-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_blogger'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='votes_total',
            field=models.IntegerField(default=1, null=True),
        ),
    ]