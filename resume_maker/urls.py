from rest_framework import routers
from django.urls import path
from resume_maker import views
from resume_maker.views import About_MeViewsets, ProjectsViewsets


router = routers.DefaultRouter()
router.register('about', About_MeViewsets)
router.register('project', ProjectsViewsets)
urlpatterns = [
    path('', views.home, name='home'),
    path('my_resume/', views.resume, name='resume'),
]

urlpatterns += router.urls