from functools import partial
from django.db.models import query
from django.db.models.expressions import Value
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status, request, filters, generics, pagination
from .models import *
from .serializer import *

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.filter()
    serializer_class = StudentSerializer
    filter_fields = ["student_id"]

    def create(self, request):
        payload = request.data
        queryset = Student.objects.filter(pk=payload["student_id"]).first()
        instance = None
        if queryset is not None:
            instance = StudentSerializer(queryset, data=payload, partial=True)
        else:
            instance = StudentSerializer(data=payload)
        if not instance.is_valid():
            errors =instance.errors
            return Response(errors)
        instance.save()
        return Response(instance.data)
