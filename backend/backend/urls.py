"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from .views import get_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion.urls')),
    path('livre/<int:livre_id>/emprunter/', views.emprunter_livre, name='emprunter_livre'),
    path('livre/<int:livre_id>/reserver/', views.reserver_livre, name='reserver_livre'),
    path('notifications/', views.mes_notifications, name='mes_notifications'),
    path('emprunt/<int:emprunt_id>/retourner/', views.retourner_livre, name='retourner_livre'),
    path('', views.liste_livres, name='liste_livres'),
    path('api/books/', get_books),
]
