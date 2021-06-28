# Generated by Django 3.2.4 on 2021-06-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0006_auto_20210628_1315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paramrodz',
            options={'verbose_name': 'Rodzaj Parametru', 'verbose_name_plural': 'Rodzaje Parametrów'},
        ),
        migrations.RenameField(
            model_name='produkty',
            old_name='opis',
            new_name='opis_1',
        ),
        migrations.AddField(
            model_name='produkty',
            name='opis_2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='produkty',
            name='opis_3',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='paramrodz',
            name='rodzaj',
            field=models.CharField(max_length=30),
        ),
    ]