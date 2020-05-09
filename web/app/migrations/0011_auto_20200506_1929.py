# Generated by Django 3.0.5 on 2020-05-06 10:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_item_h'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='a',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='A'),
        ),
        migrations.AddField(
            model_name='item',
            name='b',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='B'),
        ),
        migrations.AddField(
            model_name='item',
            name='c',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='C'),
        ),
        migrations.AddField(
            model_name='item',
            name='d',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='D'),
        ),
        migrations.AddField(
            model_name='item',
            name='s',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='S'),
        ),
    ]