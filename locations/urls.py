from django.urls import path
from .views import (
    AddLocation,
    Locations,
    LocationDetail,
    DeleteLocation,
    EditLocation,
    LocationImage,
    LikeLocationView,
)
from . import views

urlpatterns = [
    path("", Locations.as_view(), name="locations"),
    path("add/", AddLocation.as_view(), name="add_location"),
    path('<slug:slug>/', views.LocationDetail.as_view(), name='location_detail'),
    path("delete/<slug:pk>/", DeleteLocation.as_view(), name="delete_location"),
    path("edit/<slug:pk>/", EditLocation.as_view(), name="edit_location",),
    path("account/dashboard/", LocationImage.as_view(), name="dashboard"),
    path('like/<int:pk>/', views.LikeLocationView.as_view(), name='like_location'),
]
