from django.db import models

CATEGORY_CHOICES = [
    ('other', 'Разное'),
    ('monitor', 'Мониторы'),
    ('hdd', 'Жесткие диски'),
    ('keyboard', 'Клавиатуры'),
    ('mouse', 'Мышки'),
    ('cpu', 'Центральные процессоры')
]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=2000, verbose_name='Описание')
    category = models.CharField(max_length=50, null=False, blank=False, default=CATEGORY_CHOICES[0][0],
                                choices=CATEGORY_CHOICES, verbose_name='Категория')
    remain = models.PositiveIntegerField(verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость')

    def __str__(self):
        return self.name
