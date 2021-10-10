from django.urls import path

from posts.views import myview

urlpatterns = [
    path('new/', myview, name="post_new"),

]
