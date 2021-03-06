from hashlib import blake2b
from re import T
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.



class Skill(models.Model):
    skills = models.CharField(max_length=111, blank=True, null=True)
    skills_procent = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.skills

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = 'Skills'



class AboutMe(models.Model):
    fullname = models.CharField(max_length=250, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    job = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=111, blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    skill = models.ManyToManyField(Skill, blank=True)
    about_me = RichTextField(blank=True, null=True)
    def __str__(self) -> str:
        return self.fullname


    class Meta:
        verbose_name = 'AboutMe'
        verbose_name_plural = 'AboutMe'




class Projects(models.Model):
    title = models.CharField(max_length=111, null=True, blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    text = RichTextField()
    url = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'




class Work(models.Model):
    work_title = models.CharField(max_length=111, blank=True, null=True)
    work_position = models.CharField(max_length=100, blank=True, null=True)
    work_information = models.TextField(blank=True, null=True)
    date_work = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.work_title




class Education(models.Model):
    education_title = models.CharField(max_length=111, blank=True, null=True)
    education_name = models.CharField(max_length=150, blank=True, null=True)
    education_information = models.TextField(blank=True, null=True)
    date_education = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.education_title




class Resume(models.Model):
    aboutme_information = models.TextField(blank=True, null=True)
    file_resume = models.FileField(upload_to ='resume/'  ,blank=True, null=True)

    def __str__(self) -> str:
        return self.aboutme_information
    
    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resume'