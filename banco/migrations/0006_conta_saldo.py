# Generated by Django 5.1.3 on 2024-11-20 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0005_alter_cliente_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='conta',
            name='saldo',
            field=models.FloatField(default=0.0),
        ),
    ]
