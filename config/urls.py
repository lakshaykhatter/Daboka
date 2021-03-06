from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from accounts.views import LoginView	

urlpatterns = [
    path('admindashboard/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name="account_login"),
    path('posts/', include("posts.urls")),
    path('accounts/', include('allauth.urls')),
    path("accounts/", include("accounts.urls")),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
