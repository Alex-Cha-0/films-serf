from rest_framework import serializers
from .models import Contact


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'message')
