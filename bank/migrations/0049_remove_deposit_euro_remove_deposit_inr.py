# Generated by Django 5.1.1 on 2024-09-17 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0048_alter_banktransfer_status_alter_transfer_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='euro',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='inr',
        ),
    ]
