# Generated by Django 4.0.4 on 2022-06-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_aboutme_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutme_information', models.TextField(blank=True, null=True)),
                ('work_title', models.CharField(blank=True, max_length=111, null=True)),
                ('work_information', models.TextField(blank=True, null=True)),
                ('date_work', models.DateField(blank=True, null=True)),
                ('education_title', models.CharField(blank=True, max_length=111, null=True)),
                ('education_information', models.TextField(blank=True, null=True)),
                ('date_education', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
