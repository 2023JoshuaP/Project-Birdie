# Generated by Django 4.1.1 on 2022-12-01 20:54

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_user_people_user_followers_delete_userfriends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=accounts.models.profile_path),
        ),
    ]
