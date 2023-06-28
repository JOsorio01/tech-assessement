from django.urls import path, include

from rest_framework.routers import DefaultRouter
from shows import views


router = DefaultRouter()
router.register("shows", views.ShowViewSet)
router.register("directors", views.DirectorViewSet)
router.register("actors", views.ActorViewSet)
router.register("categories", views.CategoryViewSet)

app_name = "show"

urlpatterns = [
    path("", include(router.urls)),
]
