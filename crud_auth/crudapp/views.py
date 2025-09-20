from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import DetailSerializer
from rest_framework.authentication import SessionAuthentication ,BasicAuthentication
from rest_framework.permissions import IsAuthenticated ,DjangoModelPermissions,IsAdminUser

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=DetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [DjangoModelPermissions]

# Create your views here.
