from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Users
from .serializers import UsersSerializer


def index(request):
    users = Users.objects.all()
    return render(request, 'home/home.html', {'users': users})


class UsersAPIView(APIView):
    def get(self, request):
        u = Users.objects.all()
        return Response({'users': UsersSerializer(u, many=True).data})

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'user': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Users.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = UsersSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, pk):
        try:
            instance = Users.objects.get(pk=pk)
            instance.delete()
            return Response({"User deleted"})
        except:
            return Response({"error": "User does not exists"})

# class UsersAPIView(generics.ListAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UsersSerializer
