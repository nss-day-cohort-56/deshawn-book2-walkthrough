from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from deshawnapi.models import Dog, Walker


class DogView(ViewSet):
    pass


class DogSerializer(serializers.ModelSerializer):
    # TODO: Fill in the DogSerializer
    pass
