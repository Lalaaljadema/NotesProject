# Generated by Django 4.2 on 2023-04-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_likenotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]