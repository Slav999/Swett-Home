import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Users


# class UsersModel:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email


class UsersSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    email = serializers.EmailField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.time_create = validated_data.get("time_create", instance.time_create)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.save()
        return instance


# def encode():
#     model = UsersModel('Slav', 'email: kvg-1999@mail.ru')
#     model_sr = UsersSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"name": "Kirill", "email": "kirill1234@mail.ru"}')
#     data = JSONParser().parse(stream)
#     serializer = UsersSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
