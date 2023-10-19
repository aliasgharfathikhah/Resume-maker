from rest_framework.serializers import ModelSerializer
from resume_maker.models import About_Me, Projects

class About_MeSerializer(ModelSerializer):
    class Meta:
        model = About_Me
        fields = '__all__'

class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
