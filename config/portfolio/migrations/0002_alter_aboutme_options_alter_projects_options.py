# Generated by Django 4.0.4 on 2022-05-31 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutme',
            options={'verbose_name': 'AboutMe', 'verbose_name_plural': 'AboutMe'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
    ]
