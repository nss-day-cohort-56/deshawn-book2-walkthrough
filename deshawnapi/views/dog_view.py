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

    def destroy(self, request, pk):

        dog = Dog.objects.get(pk=pk)
        dog.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    # Step 1: Add the action decorator above the method definition
    # Step 2: Decide which HTTP methods the action will respond to, this one takes PUT requests
    # Step 3: Decide if the action needs a pk in the url.
    #         Will this action affect a single object (needs a pk) or multiple (does not need a pk)?
    @action(methods=['PUT'], detail=True)
    def signup_to_walk(self, request, pk):
        # Step 4: Add the code to complete the action
        #         This action will update the walker on the dog
        #         Then save that change to the database
        dog = Dog.objects.get(pk=pk)

        dog.walker = Walker.objects.get(pk=request.data['walker'])

        dog.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)




class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ('id', 'name', 'walker', )
