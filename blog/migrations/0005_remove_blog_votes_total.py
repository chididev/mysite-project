# Generated by Django 3.2.4 on 2021-06-18 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_votes_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='votes_total',
        ),
    ]
