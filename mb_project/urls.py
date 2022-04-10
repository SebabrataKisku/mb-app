from django.contrib import admin
from django.urls import path, include

from post.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
]
