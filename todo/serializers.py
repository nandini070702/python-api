from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):          #Convert Task model objects into json format and vice versa

    class Meta:              #Meta is used to configure the serializer.
        model = Task
        fields = '__all__'           #include all fields of task model in serializer