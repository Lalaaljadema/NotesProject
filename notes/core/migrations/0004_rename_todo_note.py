# Generated by Django 4.2 on 2023-04-23 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_todo_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Note',
        ),
    ]