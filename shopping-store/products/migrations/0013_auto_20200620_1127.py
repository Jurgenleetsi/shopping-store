# Generated by Django 3.0.7 on 2020-06-20 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20200620_1011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': (('can_put_on_sale', 'Put product on sale'), ('can_lower_price', 'Lower the price of a product'))},
        ),
    ]
