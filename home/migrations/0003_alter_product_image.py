# Generated by Django 5.0.3 on 2024-04-07 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]