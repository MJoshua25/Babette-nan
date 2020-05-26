from django.urls import path, include

from restaurant import views


urlpatterns = [
    path('', views.index, name='home'),
    path('menu', views.menu, name='menu'),
    path('gallery', views.gallery, name='gallery'),
    path('faq', views.faq, name='faq'),
    path('reservation', views.reservation, name='reservation'),
]