# Generated by Django 3.2.4 on 2021-06-28 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0004_auto_20210628_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produkty',
            name='opis3_nxt',
        ),
        migrations.RemoveField(
            model_name='produkty',
            name='opis_wst',
        ),
    ]
