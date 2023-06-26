from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path('upload-file/', views.upload_file, name='upload-file'),
]
