# Generated by Django 3.2.24 on 2024-11-26 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petzo_app', '0014_remove_user_table_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='petshop_rating_table',
        ),
    ]