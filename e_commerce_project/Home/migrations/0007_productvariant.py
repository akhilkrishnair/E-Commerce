# Generated by Django 4.2.4 on 2023-09-18 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_productcolorvariant'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('stock', models.PositiveSmallIntegerField()),
                ('product_color_variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.productcolorvariant')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.size')),
            ],
        ),
    ]
