from rest_framework import serializers

from ecocases.models import EcoCase  # form ..models import EcoCase


class EcoCaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcoCase
        fields = [
            'ecocase_title',
            'ecocase_description',
            'ecocase_characters',
        ]
