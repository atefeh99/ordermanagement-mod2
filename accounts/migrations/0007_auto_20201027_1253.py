# Generated by Django 3.1 on 2020-10-27 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201027_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='tag',
            new_name='tags',
        ),
    ]
