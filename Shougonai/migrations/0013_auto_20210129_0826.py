# Generated by Django 3.1.5 on 2021-01-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shougonai', '0012_auto_20210128_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]
