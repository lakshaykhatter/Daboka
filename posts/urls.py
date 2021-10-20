from django.urls import path

from posts.views import post_create_view, post_detail_view, post_update_view, PostDeleteView

urlpatterns = [
    path('new/', post_create_view, name="post_new"),
    path('<slug:urlhash>/', post_detail_view, name="post_detail"),
    path('<slug:urlhash>/edit/', post_update_view, name="post_update"),
    path('<slug:urlhash>/delete/', PostDeleteView.as_view(), name="post_delete"),


]
