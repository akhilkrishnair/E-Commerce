# Generated by Django 4.2.4 on 2024-03-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0019_alter_orders_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Pending', 'Pending'), ('Packed', 'Packed'), ('Shipped', 'Shipped'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered')], default='Pending', max_length=50),
        ),
    ]
