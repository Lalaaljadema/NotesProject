# Generated by Django 4.2 on 2023-04-23 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_newtodo_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
