from django.urls import path, include

from restaurant import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls'))
]