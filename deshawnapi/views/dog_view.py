from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from deshawnapi.models import Dog, Walker


class DogView(ViewSet):

    def retrieve(self, request, pk=None):
        dog = Dog.objects.get(pk=pk)

        serialized = DogSerializer(dog)

        return Response(serialized.data)

    def list(self, request):
        cities = Dog.objects.all()

        serialized = DogSerializer(cities, many=True)

        return Response(serialized.data)

    # TODO: Write the method to create a dog in the database


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ('id', 'name', 'walker', )
