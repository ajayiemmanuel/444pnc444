# Generated by Django 5.1.1 on 2024-09-17 12:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0039_alter_transfer_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wiretransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('bankname', models.CharField(default='-', max_length=200)),
                ('country', models.CharField(default='-', max_length=200)),
                ('swiftcode', models.TextField(default='-', max_length=200)),
                ('accountnumber', models.CharField(default='-', max_length=200)),
                ('accountname', models.CharField(default='-', max_length=200)),
                ('currency', models.CharField(default='Pending...', max_length=200)),
                ('note', models.TextField(default='-', max_length=200)),
                ('charge', models.CharField(default='-10', max_length=200)),
                ('amount', models.CharField(default='-', max_length=200)),
                ('time', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
