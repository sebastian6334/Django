# Generated by Django 3.2.4 on 2021-06-29 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0012_auto_20210629_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='zdj',
            name='film',
            field=models.TextField(blank=True),
        ),
    ]
