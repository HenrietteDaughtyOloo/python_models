# Generated by Django 3.2.12 on 2023-08-13 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_rename_vendor_product_vendor_relations'),
        ('my_cart', '0003_auto_20230812_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycart',
            name='products',
            field=models.ManyToManyField(to='inventory.Product'),
        ),
    ]
