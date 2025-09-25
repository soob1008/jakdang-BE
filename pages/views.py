from django.shortcuts import render
from rest_framework import generics
from .models import Page
from .serializers import PageSerializer

# Create your views here.
class PageDetailBySlugView(generics.RetrieveAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = "slug"