# Generated by Django 4.0.4 on 2022-05-31 19:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=250, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('job', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=111, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('skills', models.CharField(blank=True, max_length=111, null=True)),
                ('skills_procent', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=111, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('text', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
