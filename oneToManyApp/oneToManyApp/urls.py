from django.contrib import admin
from django.urls import path, include
from reporter import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("reporter.urls")),
]
