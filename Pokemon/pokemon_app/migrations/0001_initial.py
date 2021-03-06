# Generated by Django 3.0.4 on 2020-03-18 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('attack', models.IntegerField(default=0)),
                ('move', models.CharField(default='head kick', max_length=60)),
                ('attribute', models.CharField(max_length=100)),
                ('weight', models.IntegerField(default=0)),
                ('image', models.ImageField(default='default.jpg', upload_to='pokemon_pics')),
            ],
        ),
    ]
