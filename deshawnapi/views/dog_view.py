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

    def create(self, request):
        dog = Dog.objects.create(
            name=request.data['name'],
            walker=Walker.objects.get(pk=request.data['walker'])
        )
        serializer = DogSerializer(dog)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # TODO: Write the method to update a dog in the database


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ('id', 'name', 'walker', )
