from tokenize import Triple
from portfolio.models import (
    Education,
    Projects,
    AboutMe,
    Resume,
    Skill,
    Work,
)
from rest_framework import serializers



class ProjectSerializers(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = '__all__'



class SkillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'



class AboutMeSerializers(serializers.ModelSerializer):
    skill = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = AboutMe
        fields = '__all__'
        
    def get_skill(self, obj):
        skill = obj.skill

        serializer_skill = SkillSerializers(skill, many=True)

        return serializer_skill.data



class ResumeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'




class WorkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'



class EducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
