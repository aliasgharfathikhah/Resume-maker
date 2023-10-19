from django.contrib import admin
from resume_maker.models import About_Me, Projects, Technical_skills, Soft_skills, Languages

# Register your models here.
admin.site.register(About_Me)
admin.site.register(Projects)
admin.site.register(Technical_skills)
admin.site.register(Soft_skills)
admin.site.register(Languages)