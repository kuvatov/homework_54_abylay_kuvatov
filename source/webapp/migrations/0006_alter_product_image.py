# Generated by Django 4.1.7 on 2023-02-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0005_alter_category_description_alter_product_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to="static/media/"),
        ),
    ]