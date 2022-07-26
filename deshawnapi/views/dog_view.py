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

    def update(self, request, pk):
        dog = Dog.objects.get(pk=pk)

        dog.name = request.data['name']
        dog.walker = Walker.objects.get(pk=request.data['walker'])

        dog.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    # TODO: Write the method to remove a dog from the database



class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ('id', 'name', 'walker', )
