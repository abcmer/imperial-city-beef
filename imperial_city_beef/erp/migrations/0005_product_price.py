# Generated by Django 2.2.3 on 2019-08-01 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]