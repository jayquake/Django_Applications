# Generated by Django 3.0.4 on 2020-07-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='description',
            field=models.CharField(default='This is a Class', max_length=100),
        ),
    ]
