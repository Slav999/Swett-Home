import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Users


# class UsersModel:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("name", "email")


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
