"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from django.contrib.auth.models import User
from accounting.models import CustomUserModel
from rest_framework import serializers, viewsets, routers


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['age', 'national_code', ]


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUserModel.objects.all()
    serializer_class = CustomUserSerializer


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounting.urls')),
    path('', include('book.urls')),
    path('', include('extra.urls')),
    path('', include('author.urls')),
    path('', include('loan.urls')),
    
    # rest routes
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
