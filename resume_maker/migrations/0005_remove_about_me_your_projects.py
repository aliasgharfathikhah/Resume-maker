# Generated by Django 3.2.20 on 2023-10-19 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_maker', '0004_languages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about_me',
            name='your_projects',
        ),
    ]
