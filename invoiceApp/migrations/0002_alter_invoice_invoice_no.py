# Generated by Django 4.2.3 on 2023-07-14 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_no',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
