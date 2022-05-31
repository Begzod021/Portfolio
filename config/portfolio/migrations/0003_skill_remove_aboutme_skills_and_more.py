# Generated by Django 4.0.4 on 2022-05-31 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_aboutme_options_alter_projects_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(blank=True, max_length=111, null=True)),
                ('skills_procent', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='skills_procent',
        ),
    ]