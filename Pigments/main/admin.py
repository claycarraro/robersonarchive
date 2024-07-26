from django.contrib import admin
from .models import (
	Pigment, 
	Material, 
	Transcription
	)
 #clay numero20


# Register your models here.
admin.site.register(Pigment)
admin.site.register(Material)
admin.site.register(Transcription)
