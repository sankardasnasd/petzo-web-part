# Generated by Django 3.2.24 on 2024-11-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petzo_app', '0012_comment_table_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_table',
            name='image',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
