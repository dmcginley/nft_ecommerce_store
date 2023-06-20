# Generated by Django 4.2.1 on 2023-06-17 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0005_remove_product_price_product_stripe_product_id_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store_app.category'),
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
