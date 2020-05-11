from django.db import models
from django.core import validators


class Item(models.Model):
    name = models.CharField(
        verbose_name='名前',
        max_length=50,
    )
    no = models.IntegerField(
        verbose_name='図鑑番号',
        validators=[validators.MinValueValidator(1)],
    )
    type1 = models.CharField(
        verbose_name='タイプ１',
        max_length=50,
    )
    type2 = models.CharField(
        verbose_name='タイプ２',
        max_length=50,
        blank=True,
        null=True,
    )
    ability1 = models.CharField(
        verbose_name='とくせい１',
        max_length=50,
    )
    ability2 = models.CharField(
        verbose_name='とくせい２',
        max_length=50,
        blank=True,
        null=True,
    )
    hidden_ability = models.CharField(
        verbose_name='夢とくせい',
        max_length=50,
        blank=True,
        null=True,
    )
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )
    h = models.IntegerField(
        verbose_name='H',
        validators=[validators.MinValueValidator(1)],
    )
    a = models.IntegerField(
        verbose_name='A',
        validators=[validators.MinValueValidator(1)],
    )
    b = models.IntegerField(
        verbose_name='B',
        validators=[validators.MinValueValidator(1)],
    )
    c = models.IntegerField(
        verbose_name='C',
        validators=[validators.MinValueValidator(1)],
    )
    d = models.IntegerField(
        verbose_name='D',
        validators=[validators.MinValueValidator(1)],
    )
    s = models.IntegerField(
        verbose_name='S',
        validators=[validators.MinValueValidator(1)],
    )
    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '図鑑'
        verbose_name_plural = "図鑑"

