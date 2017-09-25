from rest_framework import generics
from ecocases.models import EcoCase
from .serializers import EcoCaseModelSerializer


class EcoCaseListAPIView(generics.ListCreateAPIView):
    queryset = EcoCase.objects.all()
    serializer_class = EcoCaseModelSerializer

    def get_queryset(self):
        return EcoCase.objects.all()
