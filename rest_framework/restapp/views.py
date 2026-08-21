from django.shortcuts import render
from restapp.serializers import MenuSerializer, CategorySerializer
from restapp.models import Menu, Category
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


@api_view(["POST", "GET"])
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"detail": "Category Added Successfully"},
                status=status.HTTP_201_CREATED,
            )
