# Generated by Django 3.0.5 on 2020-05-06 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200506_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='charac2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='とくせい２'),
        ),
        migrations.AddField(
            model_name='item',
            name='charac3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='夢とくせい'),
        ),
    ]