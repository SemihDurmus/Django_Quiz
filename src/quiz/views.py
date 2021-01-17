from django.shortcuts import render
from rest_framework import generics
from .models import Category, Quiz, Question
from .serializers import CategorySerializer, CategoryDetailSerializer, QuestionSerializer
# from .pagination import MyPagination (for Custom Pagination)


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


class QuizDetail(generics.ListAPIView):
    serializer_class = QuestionSerializer
    # pagination_class = MyPagination (for Custom Pagination)
    # pagination_class = [Pa] (for Global Pagination)

    def get_queryset(self):
        queryset = Question.objects.all()
        title = self.kwargs["title"]
        queryset = queryset.filter(quiz__title=title)
        return queryset
