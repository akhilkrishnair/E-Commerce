# Generated by Django 4.2.4 on 2023-09-15 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_alter_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]