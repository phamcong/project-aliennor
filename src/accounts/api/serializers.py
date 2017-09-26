from django.contrib.auth import get_user_model
from rest_framework import serializers


from ecocases.models import EcoCase  # form ..models import EcoCase

User = get_user_model()


class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
        ]
