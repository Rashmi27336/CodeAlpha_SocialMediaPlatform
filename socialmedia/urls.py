from django.contrib import admin
from django.urls import path

from core.views import (
    home,
    login_view,
    logout_view,
    register_view,
    like_post,
    add_comment,
    profile_view,
    follow_user,
    users_view
)


urlpatterns = [

    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path("login/", login_view, name="login"),

    path("register/", register_view, name="register"),

    path("logout/", logout_view, name="logout"),

    path(
        "like/<int:post_id>/",
        like_post,
        name="like_post"
    ),

    path(
        "comment/<int:post_id>/",
        add_comment,
        name="add_comment"
    ),

    path(
        "profile/",
        profile_view,
        name="profile"
    ),

    path(
        "follow/<int:user_id>/",
        follow_user,
        name="follow_user"
    ),

    path(
        "users/",
        users_view,
        name="users"
    ),
]