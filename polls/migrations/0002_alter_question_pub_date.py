# Generated by Django 5.1.4 on 2025-03-20 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="pub_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
