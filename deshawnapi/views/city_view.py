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

    def create(self, request):
        # Step 1: Use the create method to create a new city. Add all the fields needed as arguments
        city = City.objects.create(name=request.data['name'])

        # Step 2: Serialize the newly created object
        serializer = CitySerializer(city)

        # Step 3: Send the serialized data to the client, along with the 201 (created) status
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        # Step 1: get the object that will be updated
        city = City.objects.get(pk=pk)

        # Step 2: Update the fields one by one
        city.name = request.data['name']

        # Step 3: Save the updates to the database
        city.save()

        # Step 4: Send a 204 no content response to the client
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        # Step 1: Get the city to be deleted
        city = City.objects.get(pk=pk)

        # Step 2: use the delete method to remove the city from the database
        city.delete()

        # Step 3: Send a 204 no content response to the client
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'name',)
