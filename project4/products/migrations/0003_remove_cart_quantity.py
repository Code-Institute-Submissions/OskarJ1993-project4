# Generated by Django 3.2.18 on 2023-05-16 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
    ]
