# Generated by Django 4.2.4 on 2023-09-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_productvariant'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]