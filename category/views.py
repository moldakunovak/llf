from django.shortcuts import render
from  rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from category.serializers import CategorySerializer
from category.models import Category


class CreateCategoryAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
