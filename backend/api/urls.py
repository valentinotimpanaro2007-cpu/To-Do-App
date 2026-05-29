from django.urls import path
from . import views

# API-Routen der Todo-App
urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note_list"),                # GET (alle) + POST
    path("notes/<int:pk>/", views.NoteRetrieveUpdateDestroy.as_view(), name="note_detail"), # GET/PUT/PATCH/DELETE (eine)
]