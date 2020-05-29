from django.urls import path, include

from blog import views

app_name = 'shop'


urlpatterns = [
    path('', views.index, name='home'),
    path('single', views.single, name='single'),
    path('cart', views.cart, name='cart'),
]