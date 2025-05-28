# kittygram_plus/urls.py
from rest_framework.routers import DefaultRouter

from django.urls import include, path

from cats.views import CatViewSet, LightCatViewSet, OwnerViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'cats', CatViewSet, basename='cat')
router.register(r'owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet, basename='lightcat')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
