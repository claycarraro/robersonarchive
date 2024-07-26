from django.urls import path
from .import views
# from .views import (
# 	PigmentListView)

urlpatterns = [
path("", views.home, name ="home"),
path("project/", views.project, name="project"),
path("database/", views.database, name="database"),
path("contacts/", views.contacts, name="contacts"),
path("curiosities/", views.curiosities, name="curiosities"),
path("Digitaled/", views.Digitaled, name="Digitaled"),
path('pigments/', views.PigmentListView.as_view(), name='pigment_list'),
path('materials/', views.MaterialListView.as_view(), name='material_list'),
path("transcription/", views.TranscriptionListView.as_view(), name="transcription"),
path("cataloguede/", views.cataloguede, name="cataloguede"),
]
