from django.contrib import admin
from django.urls import path,include

from .views import ServiceListView, ServiceDetailsView
urlpatterns = [
    path('', ServiceListView.as_view(), name = 'services'),
    path('<int:pk>', ServiceDetailsView.as_view(), name = 'details'),
]
