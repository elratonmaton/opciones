from django.urls import path
from .views import CompanyView

urlpatterns = [
    path('<slug:url>/', CompanyView.as_view(), name='company'),
]
