# Generated by Django 3.1.5 on 2021-01-28 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shougonai', '0011_auto_20210128_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]