# Generated by Django 3.1.5 on 2021-02-05 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210205_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributorprofile',
            name='uploaded_images',
        ),
    ]
