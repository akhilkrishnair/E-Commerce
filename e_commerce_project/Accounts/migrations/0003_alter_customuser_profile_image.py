# Generated by Django 4.2.4 on 2023-10-15 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_customuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(default='profile/default/default.jpg', null=True, upload_to='profile/profile_images'),
        ),
    ]
