from rest_framework import serializers

from app.models.client import Client

class CLientSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Client
        exclude = ('state','create_date','modified_date','delete_date')


class ClientRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Client
        exclude = ('state','create_date','modified_date','delete_date') 