# Generated by Django 3.0.5 on 2020-05-06 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_item_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='type2',
        ),
    ]
