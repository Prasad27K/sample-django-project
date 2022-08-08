from .models import *
from rest_framework import serializers

class WithRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WithRelation
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    with_relation = WithRelationSerializer(many=True)
    class Meta:
        model = Student
        fields = '__all__'