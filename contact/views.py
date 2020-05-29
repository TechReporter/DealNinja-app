from typing import re

from contact.models import Contact, Notes
from rest_framework.decorators import api_view
from contact.serializers import ContactSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

# def contact_home(request):
# return HttpResponse("Hello, world. You're at the polls index.")


contactForm = modelform_factory(Contact, exclude=[])
notesForm = modelform_factory(Notes, exclude=[])


def create_contract(request):
    form = contactForm()
    return render(request, "contact/add_contact.html", {'contact_form': form})


def create_notes(request):
    form = notesForm()
    return render(request, "contact/notes.html", {'notes_form': form})


@api_view(['GET', 'POST', 'DELETE'])
def contact_list(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        contact_serializer = ContactSerializer(contacts, many=True)
        return JsonResponse(contact_serializer.data, safe=False)
    elif request.method == 'POST':
        contact_serializer = ContactSerializer(data=request.data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse(contact_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Contact.objects.all().delete()
        return JsonResponse({'message': '{} Contact were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def contact_update(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return JsonResponse({'message': 'The contact does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        contact_serializer = ContactSerializer(contact)
        return JsonResponse(contact_serializer.data)
    elif request.method == 'PUT':
        contact_details = JSONParser().parse(request)
        contact_serializer = ContactSerializer(contact, data=contact_details)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse(contact_serializer.data)
        return JsonResponse(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        contact.delete()
        return JsonResponse({'message': 'Contact was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def contact_lists_by_type(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        first_name = request.GET.get('f_name', None)
        if first_name is not None:
            contacts = contacts.filter(f_name__icontains=first_name)
            contacts_serializer = ContactSerializer(contacts, many=True)
            return JsonResponse(contacts_serializer.data, safe=False)
