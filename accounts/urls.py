from django.urls import path

from .views import profile_view

urlpatterns = [
	path("profile_view/<username>", profile_view, name='profile_view'),

]
