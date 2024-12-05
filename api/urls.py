from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'programmer', views.programmerViewSet)
router.register(r'students', views.studentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]