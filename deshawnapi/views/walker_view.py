from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from deshawnapi.models import Walker, City


class WalkerView(ViewSet):
    # TODO: Write the list and retrieve methods for the walker view
    pass


class WalkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Walker
        fields = ('id', 'name', 'email', 'city', )
