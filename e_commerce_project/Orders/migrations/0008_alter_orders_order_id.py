# Generated by Django 4.2.4 on 2023-10-13 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0007_alter_orders_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.CharField(default='akhil_97ffbe94-fa79-42d2-ab51-c560b7937308', editable=False),
        ),
    ]