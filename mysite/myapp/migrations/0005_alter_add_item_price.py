# Generated by Django 4.0.2 on 2022-02-10 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_add_item_delete_register_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_item',
            name='price',
            field=models.IntegerField(),
        ),
    ]
