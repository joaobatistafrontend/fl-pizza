# Generated by Django 5.0 on 2023-12-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_valormassa_valorrefrisucos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoValor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
