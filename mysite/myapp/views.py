from email import message
import email
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import add_item
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

isLogged = False

# Create your views here.
def index(request):
    return render(request, 'index.html')

def v1(request):
    query = add_item.objects.all()
    return render(request, 'mart.html', {'query':query})

def lol(request):
    return render(request, "lol.html")

def add(request):
    if request.method == 'POST':
        iname = request.POST['name']
        prc = request.POST['Price']
        Link = request.POST['link']

        items = add_item(item = iname, price = prc, link = Link)

        items.save()
    #, {"messages":query}
    return render(request, "add.html")
    