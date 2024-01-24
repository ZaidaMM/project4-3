
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("compose", views.compose, name="compose"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("edit/<int:post_id>", views.edit, name="edit"),
    path("compose", views.compose, name="compose"),
    path("add_like/<int:post_id>", views.add_like, name="add_like"),
    path("add_unlike/<int:post_id>", views.add_unlike, name="add_unlike"),
    path("follow_unfollow/<int:user_id>", views.follow_unfollow, name="follow_unfollow"),
    path("following", views.following, name="following"),
    
    
]
