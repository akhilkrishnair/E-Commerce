# Generated by Django 4.2.4 on 2023-09-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='offer_while_order',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
