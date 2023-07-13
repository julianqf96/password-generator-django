from django.shortcuts import render 
import random
# from django.http import HttpResponse

# Create your views here.

def about(request):
  return render(request, 'about.html')

def home(request):
  return render(request, 'home.html')

def password(request):

  characters = list('abcdefghijklmnopqrstuvwxyz')
  generate_password = ''

  length = int(request.GET.get('length'))

  if request.GET.get('uppercase'):
    characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

  if request.GET.get('special'):
    characters.extend(list('!"#$%&/()=?^'))

  if request.GET.get('numbers'):
    characters.extend(list('1234567890'))

  for x in range(length):
    generate_password += random.choice(characters)

  return render(request, 'password.html', {'password': generate_password})
