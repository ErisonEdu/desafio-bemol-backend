# Generated by Django 4.1 on 2022-08-26 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_customer_house_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='adress_complement',
            new_name='address_complement',
        ),
    ]
