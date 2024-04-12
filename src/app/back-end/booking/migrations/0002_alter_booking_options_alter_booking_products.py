# Generated by Django 4.2 on 2024-04-11 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
        ("booking", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="booking",
            options={"ordering": ["timestamp"]},
        ),
        migrations.AlterField(
            model_name="booking",
            name="products",
            field=models.ManyToManyField(
                related_name="booking_products", to="product.product"
            ),
        ),
    ]