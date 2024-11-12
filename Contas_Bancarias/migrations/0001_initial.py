# Generated by Django 5.1.3 on 2024-11-12 23:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta_bancaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Número_conta', models.CharField(max_length=6)),
                ('Saldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Data_criaçao', models.DateTimeField(auto_now_add=True)),
                ('Titular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]