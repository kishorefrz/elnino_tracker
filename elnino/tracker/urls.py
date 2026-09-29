from django.urls import path
from . import views

urlpatterns = [
    path("api/nino34/", views.nino34_data, name="nino34_data"),
    path("", views.dashboard, name="dashboard"),
]