# Generated by Django 2.0.7 on 2018-07-31 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bangazon', '0002_auto_20180730_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='paymenttype',
            new_name='payment_type',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='shoppingCart',
            new_name='shopping_cart',
        ),
        migrations.RenameField(
            model_name='paymenttype',
            old_name='paytype',
            new_name='pay_type',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='producttype',
            new_name='product_type',
        ),
    ]
