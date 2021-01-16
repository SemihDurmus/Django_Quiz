from django.shortcuts import render
from rest_framework import generics
from .models import Category, Quiz
from .serializers import CategorySerializer, CategoryDetailSerializer


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetail(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        queryset = Quiz.objects.all()
        category = self.kwargs["category"]  # backend or frontend
        # category__ is to reach a field from a parent
        queryset = queryset.filter(category__name=category)
        return queryset

# Quiz.objects.filter(category__name="backend")
