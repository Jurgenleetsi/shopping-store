# Generated by Django 3.0.7 on 2020-06-20 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20200613_1116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': (('can_put_on_sale', 'Put product on sale'),)},
        ),
    ]
