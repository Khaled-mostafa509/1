# Generated by Django 4.2.1 on 2023-07-09 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0004_alter_user_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
