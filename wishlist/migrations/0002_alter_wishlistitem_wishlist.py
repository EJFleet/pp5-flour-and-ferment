# Generated by Django 5.1.6 on 2025-02-20 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistitem',
            name='wishlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist_items', to='wishlist.wishlist'),
        ),
    ]
