# Generated by Django 5.1.4 on 2025-03-20 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_product_created_at_product_discount_product_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
