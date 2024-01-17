from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # path("",views.display,name="display"),
    # path("register/",views.register_page,name="register"),
    # path("login/",views.login_page,name="login"),
    # path("literature/",views.blog_list, name="literature"),
    # path("blogs/<int:pk>/",views.blog_detail, name = "blog_detail"),
    # path("blogs/new/",views.blog_edit, name ="blog_edit"),
    path("blogpage/",views.UserBlogsView.as_view()),
    path("newblog/", views.UserBlogView.as_view()),
    path("blog/<int:id>/", views.UserBlogView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)