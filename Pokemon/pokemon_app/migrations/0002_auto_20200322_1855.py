# Generated by Django 3.0.4 on 2020-03-22 18:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0003_credit'),
        ('pokemon_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='attribute',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cards', models.ManyToManyField(to='pokemon_app.Card')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account_app.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='CardSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_app.Card')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_app.Profile')),
            ],
        ),
    ]
