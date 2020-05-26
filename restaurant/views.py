from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'pages/home-classic.html')

# M : Definir le schéma de nos données
# V : Transmition des données et logique de l'application
# T : Logique d'affichage
