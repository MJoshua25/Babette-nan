from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'pages/home-classic.html')


def menu(request):
    return render(request, 'pages/menu-board.html')


def gallery(request):
    return render(request, 'pages/gallery-grid.html')


def faq(request):
    return render(request, 'pages/faqs.html')


def reservation(request):
    return render(request, 'pages/reservation.html')
# M : Definir le schéma de nos données
# V : Transmition des données et logique de l'application
# T : Logique d'affichage
