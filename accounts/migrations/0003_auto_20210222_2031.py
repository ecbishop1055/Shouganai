# Generated by Django 3.1.6 on 2021-02-22 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='github',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_background',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]
