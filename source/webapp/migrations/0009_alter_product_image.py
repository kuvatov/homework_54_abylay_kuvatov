# Generated by Django 4.1.7 on 2023-02-19 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0008_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to="static/media/uploads/"),
        ),
    ]
