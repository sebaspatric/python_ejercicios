# Generated by Django 4.2 on 2023-04-22 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sinopsis', models.TextField(help_text='resumen de la pelicula', max_length=1000)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.director')),
            ],
        ),
    ]
