from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from deshawnapi.models import City


class CityView(ViewSet):

    def retrieve(self, request, pk=None):

        # Step 1: Get a single city based on the primary key in the request URL
        city = City.objects.get(pk=pk)

        # Step 2: Serialize the city record as JSON
        serialized = CitySerializer(city)

        # Step 3: Send JSON response to client with 200 status code
        return Response(serialized.data)

    def list(self, request):
        # Step 1: Get all city data from the database
        cities = City.objects.all()

        # Step 2: Serialize the data with to send only the fields the client wants
        serialized = CitySerializer(cities, many=True)

        # Step 3: Send the serialized data to the client
        return Response(serialized.data)

    # TODO: Walk through this create method
    def create(self, request):
        # Step 1: Use the create method to create a new city. Add all the fields needed as arguments
        city = City.objects.create(name=request.data['name'])

        # Step 2: Serialize the newly created object
        serializer = CitySerializer(city)

        # Step 3: Send the serialized data to the client, along with the 201 (created) status
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'name',)
