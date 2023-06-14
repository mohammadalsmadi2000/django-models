from django.contrib import admin
from django.urls import path
from .views import HomePageView,AboutPageView,SnackListView,SnackDetailView
urlpatterns = [
    path('snack_list/',SnackListView.as_view(), name="snack_list"),
    path('<int:pk>/',SnackDetailView.as_view(), name="snack_detail")
]
