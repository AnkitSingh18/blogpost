# Generated by Django 2.2.1 on 2019-07-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190727_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bg_pic',
            field=models.ImageField(default='', upload_to='blog/bg_pics'),
        ),
    ]
