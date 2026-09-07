from django.shortcuts import render
from restapp.serializers import MenuSerializer, CategorySerializer, SendEmailSerializer
from restapp.models import Menu, Category
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from django.conf import settings

# from typing import Dict
from django.core.mail import send_mail

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
        # fetching if category_id is in the query_params e.g /categories/?category_id=1
        category_id = request.query_params.get("category_id")
        menus = Menu.objects.all().select_related("category")
        # Only run the filter if the category_id is in the params
        if category_id:
            menus = menus.filter(category=category_id)
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


"""
class SendEmailView(APIView):
    def post(self, request):
        serializer = SendEmailSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        assert isinstance(serializer, SendEmailSerializer)
        serializer.is_valid(raise_exception=True)
        serializer.send_email()
        return Response({"detail": "Email Sent"})
"""


class SendMailView(APIView):
    def post(self, request):
        serializer = SendEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = request.data.get("email")
        subject = request.data.get("subject")
        body = request.data.get("body")
        sender_email = f"ZayonSoft_Hiit<{settings.DEFAULT_FROM_EMAIL}>"

        try:

            send_mail(
                subject=subject,
                from_email=sender_email,
                message=body,
                recipient_list=[email],
            )

            return Response({"detail": "Everywhere semo"})

        except:
            return Response(
                {"detail": "Something Went Wrong"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
