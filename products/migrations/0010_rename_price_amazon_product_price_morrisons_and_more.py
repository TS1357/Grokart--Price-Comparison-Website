# Generated by Django 4.1.1 on 2022-11-10 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_rename_price_morrisons_product_price_amazon_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price_amazon',
            new_name='price_morrisons',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price_bigbasket',
            new_name='price_sainsburys',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price_dmart',
            new_name='price_tesco',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='url_amazon',
            new_name='url_morrisons',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='url_bigbasket',
            new_name='url_sainsburys',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='url_dmart',
            new_name='url_tesco',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price_flipkart',
        ),
        migrations.RemoveField(
            model_name='product',
            name='url_flipkart',
        ),
    ]
