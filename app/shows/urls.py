from django.urls import path, include

from rest_framework.routers import DefaultRouter
from shows import views


router = DefaultRouter()
router.register("show", views.ShowViewSet)

app_name = "show"

urlpatterns = [
    path("", include(router.urls)),
]
