# Generated by Django 4.2 on 2023-04-23 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_alter_cart_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='size',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
