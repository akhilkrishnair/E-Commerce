# Generated by Django 4.2.4 on 2023-09-18 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]