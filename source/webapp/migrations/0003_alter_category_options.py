# Generated by Django 4.1.7 on 2023-02-17 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0002_category_created_at_category_updated_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category", options={"verbose_name_plural": "Categories"},
        ),
    ]
