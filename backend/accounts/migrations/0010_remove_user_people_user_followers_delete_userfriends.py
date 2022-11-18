# Generated by Django 4.1.1 on 2022-11-18 01:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_userfriends_follower_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='people',
        ),
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserFriends',
        ),
    ]