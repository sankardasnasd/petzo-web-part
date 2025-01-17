# Generated by Django 3.2.25 on 2024-10-19 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hospital_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
                ('district', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='login_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='pet_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petshop', models.CharField(max_length=100)),
                ('petname', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='petshop_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
                ('post', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('license', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petzo_app.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='vaccinedetails_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccinename', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('dateupto', models.DateField()),
                ('uploadeddate', models.DateField()),
                ('HOSPITAL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petzo_app.hospital_table')),
            ],
        ),
        migrations.CreateModel(
            name='user_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('place', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petzo_app.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='services_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicename', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('PETSHOP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petzo_app.petshop_table')),
            ],
        ),
        migrations.CreateModel(
            name='request_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('SERVICES', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petzo_app.services_table')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petzo_app.user_table')),
            ],
        ),
        migrations.CreateModel(
            name='rating_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('HOSPITAL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petzo_app.hospital_table')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petzo_app.user_table')),
            ],
        ),
        migrations.CreateModel(
            name='petshoprequest_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pettype', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('details', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('PETSHOP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petzo_app.petshop_table')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petzo_app.user_table')),
            ],
        ),
        migrations.CreateModel(
            name='petshop_rating_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('PETSHOP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petzo_app.petshop_table')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petzo_app.user_table')),
            ],
        ),
        migrations.AddField(
            model_name='hospital_table',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petzo_app.login_table'),
        ),
        migrations.CreateModel(
            name='complaints_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaints', models.CharField(max_length=100)),
                ('reply', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petzo_app.user_table')),
            ],
        ),
    ]
