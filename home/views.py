from django.shortcuts import render
from accounts.models import *

# Create your views here.


def home(request):
    produtores = Produtor.objects.all()
    
    return render(request, 'home.html', {'produtores' : produtores})