from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, Like, Comment, Profile, Follow


# =========================
# REGISTER
# =========================

def register_view(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            # Create profile automatically
            Profile.objects.create(user=user)

            login(request, user)

            return redirect("home")

    else:
        form = UserCreationForm()

    return render(request, "register.html", {
        "form": form
    })


# =========================
# LOGIN
# =========================

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("home")

        return render(request, "login.html", {
            "error": "Invalid username or password"
        })

    return render(request, "login.html")


# =========================
# LOGOUT
# =========================

def logout_view(request):

    logout(request)

    return redirect("login")


# =========================
# HOME
# =========================

@login_required(login_url="/login/")
def home(request):

    if request.method == "POST":

        content = request.POST.get("content")

        if content:

            Post.objects.create(
                user=request.user,
                content=content
            )

        return redirect("home")

    posts = Post.objects.all().order_by("-created_at")

    return render(request, "home.html", {
        "posts": posts
    })


# =========================
# LIKE
# =========================

@login_required(login_url="/login/")
def like_post(request, post_id):

    post = Post.objects.get(id=post_id)

    like, created = Like.objects.get_or_create(
        post=post,
        user=request.user
    )

    if not created:
        like.delete()

    return redirect("home")


# =========================
# COMMENT
# =========================

@login_required(login_url="/login/")
def add_comment(request, post_id):

    post = Post.objects.get(id=post_id)

    if request.method == "POST":

        content = request.POST.get("content")

        if content:

            Comment.objects.create(
                post=post,
                user=request.user,
                content=content
            )

    return redirect("home")


# =========================
# PROFILE
# =========================

@login_required(login_url="/login/")
def profile_view(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    return render(request, "profile.html", {
        "profile": profile
    })


# =========================
# FOLLOW / UNFOLLOW
# =========================

@login_required(login_url="/login/")
def follow_user(request, user_id):

    user_to_follow = User.objects.get(id=user_id)

    if user_to_follow != request.user:

        follow, created = Follow.objects.get_or_create(
            follower=request.user,
            following=user_to_follow
        )

        if not created:
            follow.delete()

    return redirect("profile")


# =========================
# PEOPLE
# =========================

@login_required(login_url="/login/")
def users_view(request):

    users = User.objects.exclude(
        id=request.user.id
    )

    return render(request, "users.html", {
        "users": users
    })