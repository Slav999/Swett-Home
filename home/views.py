from django.shortcuts import render, redirect
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model, logout
from django.conf import settings
from datetime import datetime
from django.utils.timezone import make_aware
from django.contrib.auth import login as auth_login
import requests

from .models import Users, Product, Brand, Category
from .serializers import UsersSerializer


def product(request):
    products = Product.objects.all().order_by('?')
    brands = Brand.objects.all()
    categories = Category.objects.all().prefetch_related('products')
    context = {
        'products': products,
        'brands': brands,
        'categories': categories,
    }
    return render(request, 'home/home.html', context)


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')

        User = get_user_model()
        user = User.objects.create_user(email=email, name=name, password=password)
        return redirect('/login')
    return render(request, 'home/register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        response = requests.post(settings.DJOSER_TOKEN_ENDPOINT, data={'email': email, 'password': password})
        if response.status_code == 200:
            token = response.json().get('token')
            user = Users.objects.get(email=email)
            user.last_login = make_aware(datetime.now())
            user.save()
            auth_login(request, user)
            redirect_response = redirect('/')
            redirect_response.set_cookie('jwt_token', token)
            return redirect_response
        else:
            return render(request, 'home/login.html', {'error': 'Invalid credentials'})
    return render(request, 'home/login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Users.objects.all()[:5]

        return Users.objects.filter(pk=pk)

# class UsersAPIList(generics.ListCreateAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UsersSerializer
#
#
# class UserAPIUpdate(generics.UpdateAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UsersSerializer
#
#
# class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UsersSerializer


# class UsersAPIView(APIView):
#     def get(self, request):
#         u = Users.objects.all()
#         return Response({'users': UsersSerializer(u, many=True).data})
#
#     def post(self, request):
#         serializer = UsersSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'user': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Users.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = UsersSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, pk):
#         try:
#             instance = Users.objects.get(pk=pk)
#             instance.delete()
#             return Response({"User deleted"})
#         except:
#             return Response({"error": "User does not exists"})
