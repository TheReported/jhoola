# Generated by Django 4.2 on 2024-05-17 13:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_alter_product_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="hotel_product_id",
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
    ]
