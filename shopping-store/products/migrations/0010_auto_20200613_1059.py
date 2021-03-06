# Generated by Django 3.0.7 on 2020-06-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='perishable',
            field=models.BooleanField(default=False),
        ),
    ]
