from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from deshawnapi.models import Walker, City


class WalkerView(ViewSet):

    def retrieve(self, request, pk=None):
        walker = Walker.objects.get(pk=pk)

        serialized = WalkerSerializer(walker)

        return Response(serialized.data)

    def list(self, request):
        cities = Walker.objects.all()

        serialized = WalkerSerializer(cities, many=True)

        return Response(serialized.data)

    def create(self, request):
        walker = Walker.objects.create(
            name=request.data['name'],
            email=request.data['email'],
            city=City.objects.get(pk=request.data['city'])
        )
        serializer = WalkerSerializer(walker)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        walker = Walker.objects.get(pk=pk)
        walker.name = request.data['name']
        walker.email = request.data['email']
        walker.city = City.objects.get(pk=request.data['city'])

        walker.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        walker = Walker.objects.get(pk=pk)
        walker.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    # TODO: Create a custom action that updates the walkers city
    # Decide what methods it will respond to and if it should be a detail route


class WalkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Walker
        fields = ('id', 'name', 'email', 'city', )
