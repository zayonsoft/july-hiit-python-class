from django.urls import path
from . import views

urlpatterns = [
    path("categories1/", views.category_list, name="categories"),
    path("categories/", views.CategoriesView.as_view()),
    path("categories/<str:pk>/", views.CategoryView.as_view(), name="category"),
    path("menu/", views.MenusView.as_view(), name="menus"),
    path("menu/<str:pk>", views.MenuView.as_view(), name="menu"),
]
