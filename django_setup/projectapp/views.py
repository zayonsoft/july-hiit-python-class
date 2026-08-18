from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from projectapp.models import Post, Student
from projectapp.forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

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
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = PostForm()

    context = {"post_form": form}
    return render(request, "post_form.html", context)


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = PostForm(instance=post)

    context = {"post_form": form}
    return render(request, "post_form.html", context)


def create_user(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "User Added Successfully")
    else:
        form = UserCreationForm()

    context = {"form": form, "form_name": "User Creation Form"}
    return render(request, "create_user.html", context)


def custom_create_user(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_passwd = request.POST.get("confirm_password")

        # 1 - Check that there're no empty inputs
        if not (username and email and password and confirm_passwd):
            messages.error(request, "All fields are required")
            return redirect("custom_create_user")

        is_valid = True
        # 2 - see if the username exists
        if User.objects.filter(username__iexact=username).exists():
            messages.error(request, "Username taken")
            is_valid = False

        if User.objects.filter(email__iexact=email).exists():
            messages.error(request, "Email already taken")
            is_valid = False

        if password != confirm_passwd:
            messages.error(request, "Two passwords don't match")
            is_valid = False

        if is_valid == False:
            return redirect("custom_create_user")

        created_user = User.objects.create_user(
            username=username, email=email, password=confirm_passwd
        )
        messages.success(
            request, f"Hi {created_user.username}! Your account has been created!"
        )
        return redirect("custom_create_user")

    return render(request, "custom_create_user.html")


def create_students(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        description = request.POST.get("description")
        phone_number = request.POST.get("phone")

        if not (first_name and last_name and description and phone_number):
            messages.error(request, "All fields are required")
            return redirect("create_students")

        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            description=description,
            phone_number=phone_number,
        )

        messages.success(request, f"Student {student.first_name} added successfully")
        return redirect("student_list")
    return render(request, "students/create.html")


def student_list(request):
    students = Student.objects.all()

    context = {"students": students}
    return render(request, "students/students-table.html", context)


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        description = request.POST.get("description")
        phone_number = request.POST.get("phone")

        if not (first_name and last_name and description and phone_number):
            messages.error(request, "All fields are required")
            return redirect("edit_student", pk=pk)

        student.first_name = first_name
        student.last_name = last_name
        student.description = description
        student.phone_number = phone_number
        student.save()
        messages.success(request, "Student Updated Successfully!")
        return redirect("student_list")

    context = {"student": student}
    return render(request, "students/edit.html", context)


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted!")
        return redirect("student_list")

    context = {"student": student}
    return render(request, "students/delete-student.html", context)
