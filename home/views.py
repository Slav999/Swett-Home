from django.shortcuts import render

from home.models import Users


def index(request):
    users = Users.objects.all()
    return render(request, 'home/home.html', {'users': users})
