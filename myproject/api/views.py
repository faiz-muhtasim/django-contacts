from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Contact

# Allow POST requests from Postman without CSRF token
@csrf_exempt
def create_contact(request):
    if request.method == "POST":
        data = json.loads(request.body)
        contact = Contact.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone")
        )
        return JsonResponse({"id": contact.id, "message": "Contact created"}, status=201)

def get_contact(request, contact_id):
    try:
        contact = Contact.objects.get(id=contact_id)
        return JsonResponse({
            "id": contact.id,
            "name": contact.name,
            "email": contact.email,
            "phone": contact.phone
        })
    except Contact.DoesNotExist:
        return JsonResponse({"error": "Contact not found"}, status=404)

@csrf_exempt
def update_contact(request, contact_id):
    if request.method == "PUT":
        try:
            contact = Contact.objects.get(id=contact_id)
            data = json.loads(request.body)
            contact.name = data.get("name", contact.name)
            contact.email = data.get("email", contact.email)
            contact.phone = data.get("phone", contact.phone)
            contact.save()
            return JsonResponse({"message": "Contact updated"})
        except Contact.DoesNotExist:
            return JsonResponse({"error": "Contact not found"}, status=404)

@csrf_exempt
def delete_contact(request, contact_id):
    if request.method == "DELETE":
        try:
            contact = Contact.objects.get(id=contact_id)
            contact.delete()
            return JsonResponse({"message": "Contact deleted"})
        except Contact.DoesNotExist:
            return JsonResponse({"error": "Contact not found"}, status=404)
