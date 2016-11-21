from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
    year = models.CharField(max_length=4)
    title = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    # -1 is for individual contributor role
    teamsize= models.IntegerField()
    company = models.CharField(max_length=50)
    desc = models.TextField()
    pics = models.BooleanField(default=False)

class Tech(models.Model):
    tech = models.CharField(max_length=20)
    project = models.ForeignKey(Project)

jpg=re.compile(r'[.]jpg$')
jpeg=re.compile(r'[.]jpeg$')
png=re.compile(r'[.]png$')

def isjpg(f):
    if jpg.search(f) or jpeg.search(f):
        return True
    return False

def ispng(f):
    if png.search(f):
        return True
    return False


def pic_directory_path(instance, filename):
    if isjpg(filename):
        return "pics/project_{0}/{1}/pic.jpg".format(instance.project.id,instance.seq)
    elif ispng(filename):
        return "pics/project_{0}/{1}/pic.png".format(instance.project.id,instance.seq)
    else:
        return "pics/project_{0}/{1}/pic.bin".format(instance.project.id,instance.seq)

class Pics(models.Model):
    url = models.CharField(max_length=300)
    project = models.ForeignKey(Project)
    seq = models.IntegerField()
    image=models.FileField(upload_to=pic_directory_path)
    caption = models.CharField(max_length=50)

