from django.urls import path
from django.db import router
from django.urls.conf import include
from .views import InfoViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('obj_info', InfoViewset, basename='obj_info')

urlpatterns = [
    path("rest/",include(router.urls)),
    path("rest/<int:pk>/", include(router.urls)),
    
]
