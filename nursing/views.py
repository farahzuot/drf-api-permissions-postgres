from django.shortcuts import render
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .serializer import ServiceSerializer
from .models import Service
from .permissions import PermissionsControler
# Create your views here.

class ServiceListView(ListAPIView, CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (PermissionsControler,)



class ServiceDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (PermissionsControler,)

