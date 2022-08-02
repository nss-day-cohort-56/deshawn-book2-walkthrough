from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from deshawnapi.models import City


class CityView(ViewSet):
    pass



class CitySerializer(serializers.ModelSerializer):
    pass
