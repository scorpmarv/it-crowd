from rest_framework import serializers
from .models import Backscratcher


class BackscratcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backscratcher
        fields = '__all__'
