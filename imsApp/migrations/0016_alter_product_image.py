# Generated by Django 4.0.3 on 2022-07-25 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0015_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default=avater.png', upload_to='uploads'),
        ),
    ]