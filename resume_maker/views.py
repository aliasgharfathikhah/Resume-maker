from django.shortcuts import render
from rest_framework import viewsets
from resume_maker.models import About_Me, Projects, Technical_skills, Soft_skills, Languages
from resume_maker.serializers import About_MeSerializer, ProjectsSerializer


# Create your views here.
class About_MeViewsets(viewsets.ModelViewSet):
    queryset = About_Me.objects.all()
    serializer_class = About_MeSerializer

class ProjectsViewsets(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

def resume(request):
    about_me = About_Me.objects.first()
    Tskill = Technical_skills.objects.all()
    Sskills = Soft_skills.objects.all()
    projects = Projects.objects.all()
    lngs = Languages.objects.all()
    return render(request, 'blog/resume.html', {'about_me': about_me, 'Tskills': Tskill, 'projects': projects, 'Sskills': Sskills, 'lngs': lngs})

def home(request):
    return render(request, 'blog/home.html')