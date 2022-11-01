from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData


# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='favorites')
    serializer_class = BookSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='comedy')
    serializer_class = BookSerializer

class HorrorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='horror')
    serializer_class = BookSerializer

class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='fantasy')
    serializer_class = BookSerializer

class ChildrenViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='children')
    serializer_class = BookSerializer

class LiteratureViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='american literature')
    serializer_class = BookSerializer

class TopRatedViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(rating = 10)
    serializer_class = BookSerializer

class TragedyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='tragedy')
    serializer_class = BookSerializer

class BiographyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='biography')
    serializer_class = BookSerializer

