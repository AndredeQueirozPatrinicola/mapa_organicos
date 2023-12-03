from rest_framework import serializers


class UserSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    username = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()


class ProdutorSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    nome_fantasia = serializers.CharField(max_length=50)
    logradouro = serializers.CharField(max_length=30)
    numero = serializers.IntegerField()
    latitude = serializers.CharField(max_length=20)
    longitude = serializers.CharField(max_length=20)
    tipo_produtor = serializers.CharField(max_length=1)

    user = UserSerializer()