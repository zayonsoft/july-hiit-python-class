from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from projectapp.models import Post
from projectapp.forms import PostForm

# Create your views here.


def home(request):
    return render(request, "index.html")


def about(request):
    about_message = "This is a message for the about page from the backend"

    best_players = ["Ororo", "Neymar", "Mbappe", "Dembele"]
    GOAT = "Messi"

    context = {
        "taofeek": about_message,
        "programmer_name": "ZayonSoft",
        "age": 43,
        "best_players": best_players,
        "GOAT": GOAT,
    }
    print(context)

    return render(request, "about.html", context)


def profile(request):
    my_profile = {
        "name": "Favour",
        "class": "Python",
        "age": 54,
    }
    return JsonResponse(my_profile)


def posts(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "posts.html", context)


def post(request, pk):
    # the_post = Post.objects.get(pk=pk)
    the_post = get_object_or_404(Post, pk=pk)
    context = {"post": the_post}
    return render(request, "post.html", context)


def display_form(request):
    return render(request, "user_form.html")


def submit_form(request):
    if request.method == "POST":
        name = request.POST.get("username")
        dept = request.POST.get("department")

        values = {"name": name, "department": dept}
        return JsonResponse(values)

    return redirect("user_form")


def add_post(request):
    form = PostForm()

    context = {"post_form": form}
    return render(request, "post_form.html", context)
