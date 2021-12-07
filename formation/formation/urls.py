"""formation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import debug_toolbar
from django.contrib import admin
from django.urls import path
from django.urls import include
from country.views import test, front
from country.viewset import CountryViewSet, ListCountry, ListCountryGeneric
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'country', CountryViewSet)

urlpatterns = [
    path('test/', test),
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    
    path('country-apiview/', ListCountry.as_view()),
    path('country-genericview/', ListCountryGeneric.as_view()),

    path('front/', front),

    path('', include(router.urls)),
]