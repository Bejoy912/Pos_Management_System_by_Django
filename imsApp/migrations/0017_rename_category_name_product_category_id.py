# Generated by Django 4.0.3 on 2022-08-02 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0016_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category_id',
        ),
    ]