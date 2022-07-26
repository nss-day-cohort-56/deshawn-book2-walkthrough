from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from deshawnapi.models import Walker, City


class WalkerView(ViewSet):
    pass


class WalkerSerializer(serializers.ModelSerializer):
    # TODO: Fill in the DogSerializer
    pass
