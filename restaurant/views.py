from django.shortcuts import render
from . import models


# Create your views here.

def index(request):
    return render(request, 'pages/home-classic.html')


# ORM filter, all
def menu(request):
    data = {
        'categories': models.MenuCategory.objects.filter(status=True),
        'plats': models.Plat.objects.filter(status=True)
    }
    return render(request, 'pages/menu-board.html', data)


def gallery(request):
    return render(request, 'pages/gallery-grid.html')


def faq(request):
    return render(request, 'pages/faqs.html')


def reservation(request):
    return render(request, 'pages/reservation.html')
# M : Definir le schéma de nos données
# V : Transmition des données et logique de l'application
# T : Logique d'affichage
