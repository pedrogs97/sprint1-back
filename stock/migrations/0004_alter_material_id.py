# Generated by Django 3.2 on 2023-04-21 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_alter_material_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='id',
            field=models.BigAutoField(db_index=True, primary_key=True, serialize=False),
        ),
    ]
