from django.shortcuts import render
from restapp.serializers import MenuSerializer, CategorySerializer
from restapp.models import Menu, Category
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

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


class CategoriesView(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({"detail": "Category added successfully"})

    def get(self, request):
        categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryView(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)

        serializer = CategorySerializer(category)
        return Response(serializer.data)

    # for partial updates
    def patch(self, request, pk):
        # Get the category that needs update
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"detail": "Category updated"})

    # for complete updates
    def put(self, request, pk):
        # Get the category that needs update
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"detail": "Category updated"})

    def delete(self, request, pk):
        # Get the category that needs to be deleted
        category = get_object_or_404(Category, pk=pk)
        category.delete()

        return Response({"detail": "Category deleted"})


class MenusView(APIView):
    def get(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"detail": "Menu Added Successfully"})


class MenuView(APIView):
    def get(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        serializer = MenuSerializer(menu)
        return Response(serializer.data)

    def delete(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        menu.delete()
        return Response({"detail": "Menu deleted"})

    def patch(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)

        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"detail": "Menu Updated", "menu": serializer.data})
