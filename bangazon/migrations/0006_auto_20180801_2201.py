# Generated by Django 2.0.7 on 2018-08-01 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangazon', '0005_auto_20180801_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shopping_cart',
        ),
        migrations.DeleteModel(
            name='ShoppingCart',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazon.Order'),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazon.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(through='bangazon.OrderProduct', to='bangazon.Product'),
        ),
    ]
