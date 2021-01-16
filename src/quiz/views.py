from django.shortcuts import render
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
