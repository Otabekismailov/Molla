# Generated by Django 4.2 on 2023-04-22 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_cart_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.SmallIntegerField(default=0),
        ),
    ]