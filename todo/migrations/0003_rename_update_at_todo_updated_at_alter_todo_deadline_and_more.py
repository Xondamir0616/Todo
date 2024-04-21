# Generated by Django 5.0.4 on 2024-04-13 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_created_at_todo_update_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
