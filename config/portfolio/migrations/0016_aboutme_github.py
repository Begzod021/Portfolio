# Generated by Django 4.0.4 on 2022-06-06 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_projects_url_alter_resume_file_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
    ]
