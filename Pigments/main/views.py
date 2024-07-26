from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
import os
from .models import (
	Pigment, 
	Material, 
	Transcription
	)
# from .models import CarouselItem

from django.views.generic import(
	ListView,
	DetailView
	)

def home(response):
    return render(response, 'main/home.html')

def project(response):
    return render(response, 'main/project.html')

def database(response):
    return render(response, 'main/database.html')
    
def contacts(response):
    return render(response, 'main/contacts.html')

def curiosities(response):
    return render(response, 'main/curiosities.html')

def Digitaled(response):
    return render(response, 'main/Digitaled.html')

def cataloguede(response):

	return render(response, 'main/cataloguede.html')

class TranscriptionListView(ListView):
	model = Transcription
	context_object_name='transcription'
	ordering=['id']
	paginate_by = 1

	transcription = Transcription.objects.all()

	global no_of_entries
	no_of_entries = len(transcription)

	def get_context_data(self, **kwargs):
		context = super(TranscriptionListView, self).get_context_data(**kwargs)
		context['no_of_entries'] = no_of_entries
		return context

class PigmentListView(ListView):
	model = Pigment
	context_object_name='pigment'
	ordering=['id']
	paginate_by = 9

	pigments = Pigment.objects.all()

	global no_of_entries
	no_of_entries = len(pigments)

	def get_context_data(self, **kwargs):
		context = super(PigmentListView, self).get_context_data(**kwargs)
		context['no_of_entries'] = no_of_entries
		return context

class MaterialListView(ListView):
	model = Material
	context_object_name='material'
	ordering=['id']
	paginate_by = 8

	materials = Material.objects.all()

	global no_of_entries
	no_of_entries = len(materials)

	def get_context_data(self, **kwargs):
		context = super(MaterialListView, self).get_context_data(**kwargs)
		context['no_of_entries'] = no_of_entries
		return context

