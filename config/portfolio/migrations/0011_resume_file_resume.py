# Generated by Django 4.0.4 on 2022-06-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_resume_education_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='file_resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
