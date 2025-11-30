from django.db import models


class TimeStampAbstractModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField('Дата добавление', auto_now_add=True)
    updated_at = models.DateTimeField('Дата добавление', auto_now=True)


class Categories(TimeStampAbstractModel):
    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


    name = models.CharField('Название', max_length=150, unique=True)
    slug = models.SlugField('URL', max_length=200, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name



class Products(TimeStampAbstractModel):
    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id', )

    name = models.CharField('Название', max_length=150, unique=True)
    slug = models.SlugField('URL', max_length=200, unique=True, blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    images = models.ImageField('Изоброжение', upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField('Цена', default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField('Скидка в %', default=0.00, max_digits=4, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество', default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')
    is_publish = models.BooleanField('Публичность', default=True)

    def __str__(self):
        return self.name

    def display_id(self):
        return f'{self.id:05}'

    def sale(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price

    def sale_count(self):
        return self.price - self.sale()