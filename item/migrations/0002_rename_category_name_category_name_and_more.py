# Generated by Django 4.2.4 on 2023-08-17 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Category_Name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='items',
            old_name='Item_Name',
            new_name='Name',
        ),
    ]
