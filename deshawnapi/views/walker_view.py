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

    # TODO: Write the method to create a walker in the database


class WalkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Walker
        fields = ('id', 'name', 'email', 'city', )
