from django.urls import path

from .views import profile_view, edit_profile_view

urlpatterns = [
	path("profile/<username>", profile_view, name='profile_view'),
	path("profile/<username>/edit", edit_profile_view, name="edit_profile_view")
]
