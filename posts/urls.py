from django.urls import path

from posts.views import post_create_view, post_detail_view, post_update_view

urlpatterns = [
    path('new/', post_create_view, name="post_new"),
    path('<int:id>/', post_detail_view, name="post_detail"),
    path('<int:id>/edit', post_update_view, name="post_update")

]
