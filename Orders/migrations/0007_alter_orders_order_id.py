# Generated by Django 4.2.4 on 2023-10-13 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0006_alter_orders_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.CharField(default='akhil_<function uuid4 at 0x7f8f25ef3760>', editable=False),
        ),
    ]