from .views import posts_list, post_details_view, add_post, edit_post, delete_post, user_login_view

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',posts_list,name='home_path'),
    path('post/<int:passed_id>/',post_details_view,name='details_path'),
    path('account/',add_post,name='add_post'),
    path('account/edit_post/<int:passed_id>/',edit_post,name='edit_post'),
    path('account/delete_post/<int:post_id>/',delete_post,name='delete_post'),
    path('login/',user_login_view,name='login')
]