# Generated by Django 3.1.5 on 2021-02-09 13:59

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('picture_app', '0002_commentonpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]