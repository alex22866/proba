from rest_framework import serializers

from .models import Header,Headerdis


class HeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields ='__all__'

class HeaderdisSerializers(serializers.ModelSerializer):
    he = HeaderSerializers(read_only=True,many=True)
    class Meta:
        model = Headerdis
        fields = '__all__'
