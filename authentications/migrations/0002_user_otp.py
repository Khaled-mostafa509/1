# Generated by Django 3.2.15 on 2022-09-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='OTP',
            field=models.IntegerField(blank=True, max_length=4, null=True),
        ),
    ]
