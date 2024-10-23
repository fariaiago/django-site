# Generated by Django 5.1 on 2024-09-25 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.SmallIntegerField(choices=[(1, 'AUDI'), (2, 'BMW'), (3, 'CHEVROLET - GM'), (4, 'FERRARI'), (5, 'FIAT'), (6, 'FORD'), (7, 'HONDA'), (8, 'HYUNDAY'), (9, 'VOLKSWAGEN')])),
                ('modelo', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('cor', models.SmallIntegerField(choices=[(1, 'BRANCO'), (2, 'AMARELO'), (3, 'AZUL'), (4, 'PRATA'), (5, 'PRETO'), (6, 'VERMELHO')])),
                ('foto', models.ImageField(blank=True, null=True, upload_to='veiculo/fotos')),
                ('combustivel', models.SmallIntegerField(choices=[(1, 'ETANOL'), (2, 'DIESEL'), (3, 'FLEX'), (4, 'GASOLINA')])),
            ],
        ),
    ]
