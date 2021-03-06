from django.db import models


class Dimension(models.Model):
    h = models.FloatField(default=0.0)
    l = models.FloatField(default=0.0)
    d = models.FloatField(default=0.0)

    def __str__(self):
        return 'L=' + str(self.l) + ',' + 'H=' + str(self.h) + ',' + 'D=' + str(self.d)


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=20)
    perishable = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - prerishable:' + str(self.perishable)

class Product(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=0)
    info = models.TextField(null=True, blank=True)
    specs = models.TextField(null=True, blank=True)
    production_date = models.DateField(null=True, blank=True)
    serial_number = models.CharField(max_length=30, null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    arriving_date = models.DateField(auto_now_add=True)
    dimensions = models.ForeignKey(
        Dimension, on_delete=models.DO_NOTHING, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        permissions = (("can_put_on_sale", "Put product on sale"),
                       ("can_lower_price", "Lower the price of a product"),)
