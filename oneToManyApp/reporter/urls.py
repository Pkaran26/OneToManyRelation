from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('reporterform', views.reporterform, name="index"),
    path('articleform', views.articleform, name="index"),
    path('addreporter', views.addreporter, name="addreporter"),
    path('addarticle', views.addarticle, name="addarticle"),
    path('viewreporter', views.viewreporter, name="viewreporter"),
    path('<int:id>/viewarticle', views.viewarticle, name="viewarticle"),
]