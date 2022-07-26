from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from deshawnapi.models import City


class CityView(ViewSet):
    pass


# TODO: Walk through the serializer
# Step 1: Create a serializer class, it should inherit from the ModelSerializer
class CitySerializer(serializers.ModelSerializer):

    # Step 2: add a Meta class nested inside the serializer
    # This will contain any configuration settings for the serializer
    class Meta:
        # Step 3: Add a model property and set it equal to the model class for the serializer
        model = City
        # Step 4: Add the fields property.
        # It should be a tuple or list of the model's fields that will be returned to the client
        fields = ('id', 'name')
