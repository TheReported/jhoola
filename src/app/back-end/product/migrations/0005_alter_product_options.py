# Generated by Django 4.2 on 2024-05-20 13:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0004_product_hotel_product_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ["hotel_product_id"]},
        ),
    ]