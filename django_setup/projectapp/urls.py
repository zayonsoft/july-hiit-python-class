from projectapp import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("profile/", views.profile, name="profile"),
    path("posts/", views.posts, name="posts"),
    path("posts/add/", views.add_post, name="add_post"),
    path("posts/<str:pk>/", views.post, name="post"),
    path("user/form/", views.display_form, name="user_form"),
    path("user/submit/", views.submit_form, name="submit_form"),
]
