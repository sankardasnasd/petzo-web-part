# Generated by Django 3.2.24 on 2024-11-25 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petzo_app', '0009_post_table_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_table',
            name='type',
        ),
    ]
