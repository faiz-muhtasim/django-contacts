from django.urls import path
from . import views

urlpatterns = [
    path("contact/create/", views.create_contact),
    path("contact/<int:contact_id>/", views.get_contact),
    path("contact/<int:contact_id>/update/", views.update_contact),
    path("contact/<int:contact_id>/delete/", views.delete_contact),
]