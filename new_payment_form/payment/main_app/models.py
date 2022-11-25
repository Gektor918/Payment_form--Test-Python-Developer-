from django.db import models


class Item(models.Model):
    # Save the product price in cents
    name = models.CharField(max_length=50, blank=False, verbose_name='Название товара')
    description = models.TextField(blank=False, verbose_name='Описание')
    price = models.IntegerField(blank=False, verbose_name='Цена')


    def __str__(self):
        # Displaying the product name in the Admin panel
        return 'Наименование товара: {}'.format(self.name)
    
    def display_price(self):
        # USD price display method
        return "{0:.2f}".format(self.price / 100)