from rest_framework import serializers
from tinymce.widgets import TinyMCE
from ecocases.models import EcoCase  # form ..models import EcoCase
from accounts.api.serializers import UserDisplaySerializer


class EcoCaseModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer()

    class Meta:
        model = EcoCase
        fields = [
            'user',
            'ecocase_title',
            'ecocase_description',
            'ecocase_characters',
            'ecocase_images',
        ]
