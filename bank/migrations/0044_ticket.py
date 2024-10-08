# Generated by Django 5.1.1 on 2024-09-17 16:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0043_remove_fixed_returnamount'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField(max_length=200)),
                ('attachment', models.ImageField(blank=True, null=True, upload_to='')),
                ('status', models.CharField(default='Pending...', max_length=200)),
                ('time', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
