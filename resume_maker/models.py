from django.db import models

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=256)
    link = models.TextField()
    def __str__(self):
        return f'[ {self.name} ]'

class About_Me(models.Model):
    name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    year_of_Birth = models.IntegerField()
    your_emile = models.CharField(max_length=256)
    your_phone_number = models.CharField(max_length=11)
    your_picture = models.ImageField(upload_to='user/picture/', blank=True, null=True)
    biography = models.TextField()
    your_home_address = models.CharField(max_length=50)

    def __str__(self):
        return f'[ {self.name} {self.last_name} ]'
    
class Technical_skills(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_level = models.IntegerField()

    def __str__(self):
        return f'[ {self.skill_name} {self.skill_level}% ]'
    
class Soft_skills(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_level = models.IntegerField()

    def __str__(self):
        return f'[ {self.skill_name} {self.skill_level}% ]'
    
class Languages(models.Model):
    language_name = models.CharField(max_length=50)
    language_level = models.IntegerField()

    def __str__(self):
        return f'[ {self.language_name} {self.language_level}% ]'
