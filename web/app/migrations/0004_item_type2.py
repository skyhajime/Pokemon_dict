# Generated by Django 3.0.5 on 2020-05-06 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200506_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='type2',
            field=models.IntegerField(choices=[(1, 'ノーマル'), (2, 'ほのお'), (3, 'みず'), (4, 'でんき'), (5, 'くさ'), (6, 'こおり'), (7, 'かくとう'), (8, 'どく'), (9, 'じめん'), (10, 'ひこう'), (11, 'エスパー'), (12, 'むし'), (13, 'いわ'), (14, 'ゴースト'), (15, 'ドラゴン'), (16, 'あく'), (17, 'はがね'), (18, 'フェアリー')], default=1, verbose_name='タイプ2'),
        ),
    ]
