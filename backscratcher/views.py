from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from rest_framework import generics

from .models import Backscratcher
from .serializers import BackscratcherSerializer


class BackscratcherList(generics.ListCreateAPIView):
    queryset = Backscratcher.objects.all()
    serializer_class = BackscratcherSerializer


class BackscratcherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Backscratcher.objects.all()
    serializer_class = BackscratcherSerializer


class BackscratcherListView(ListView):
    model = Backscratcher


class BackscratcherDetailView(DetailView):
    model = Backscratcher
