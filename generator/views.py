from random import random
from subprocess import list2cmdline
from tarfile import LENGTH_LINK
from django.shortcuts import render
import random 
""" from django.http import HttpResponse """

# Create your views here.
def about(request):
    return render(request , 'generator/about.html')

def home(request):
    return render(request , 'generator/home.html')

def password(request):
    character =list('abcdefghijklmnñopqrstuvwxyz')
    generater_password = ''
    n =int(request.GET.get('length')) 
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNÑOPRSTUVWXYZ'))
    if request.GET.get('special'):
        character.extend(list('!"#$%&/()=?¡¿'))
    if request.GET.get('numbers'):
        character.extend(list('123456789'))
    for x in range(n):
        generater_password += random.choice(character)

    return render(request , 'generator/password.html',{'password': generater_password})