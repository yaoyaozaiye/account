from rest_framework import serializers
from .models import Statement

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
        fields = '__all__'
