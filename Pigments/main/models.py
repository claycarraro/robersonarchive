from django.db import models

# Create your models here.
class Pigment(models.Model):
    id = models.IntegerField(primary_key=True)
    #label_picture = models.CharField(max_length=100)
    bottle_picture = models.ImageField(default='main/static/IMGB/defaultbottle.png', upload_to='main/static/IMGB/')
    archive_id = models.CharField(max_length=50, blank=True, null=True)
    specific_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    color = models.CharField(max_length=50)
    shade = models.CharField(max_length=50)
    stopper = models.CharField(max_length=50)
    geographical_origins = models.CharField(max_length=100, blank=True, null=True)
    date_of_production = models.CharField(max_length=100, blank=True, null=True)
    chemical_composition = models.CharField(max_length=100, blank=True, null=True)
    physical_properties = models.CharField(max_length=100)
    archive_description = models.TextField()

    def __str__(self):
        return self.specific_name 

class Material(models.Model):
    id = models.IntegerField(primary_key=True)
    archive_id = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100)
    m_pictures = models.ImageField(default='main/static/IMGM/defaultmaterial.png',upload_to='main/static/IMGM/', blank=True, null=True)
    type_of_material = models.CharField(max_length=50)
    factory = models.CharField(max_length=100, blank=True, null=True)
    geographical_origins = models.CharField(max_length=100, blank=True, null=True)
    physical_properties = models.TextField()

    def __str__(self):
        return self.name

class Transcription(models.Model):
    pagenumber = models.TextField(max_length=50)
    image = models.ImageField(upload_to='main/static/Rectos', blank=True, null=True)
    ms_number = models.CharField(max_length=50)
    transcription = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s: %s' % (self.ms_number, self.pagenumber)