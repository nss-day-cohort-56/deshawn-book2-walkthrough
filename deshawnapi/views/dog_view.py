from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from deshawnapi.models import Dog, Walker


class DogView(ViewSet):
    # TODO: Write the list and retrieve methods for the dog view
    pass


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ('id', 'name', 'walker', )
