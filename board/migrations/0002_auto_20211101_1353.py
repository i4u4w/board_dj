# Generated by Django 3.2.8 on 2021-11-01 04:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='up',
        ),
        migrations.AddField(
            model_name='board',
            name='up',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
