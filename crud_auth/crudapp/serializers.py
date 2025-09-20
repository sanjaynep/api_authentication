from rest_framework import serializers
from .models import Student

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id', 'name', 'age', 'email']