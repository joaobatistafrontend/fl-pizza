# Generated by Django 5.0 on 2023-12-05 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_produto_imagem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='nome',
            new_name='nome_produto',
        ),
    ]
