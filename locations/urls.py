from django.urls import path
from .views import (
    AddLocation,
    Locations,
    LocationDetail,
    DeleteLocation,
    EditLocation,
    LocationImage,
    LikeLocationView,
    Index,
)
from . import views

urlpatterns = [
    path("", Index.as_view(), name="home"),
    path("locations/", Locations.as_view(), name="locations"),
    path("add/", AddLocation.as_view(), name="add_location"),
    path("delete/<slug:slug>/", DeleteLocation.as_view(),
         name="delete_location"),
    path("edit/<slug:slug>/", EditLocation.as_view(), name="edit_location"),
    path("account/dashboard/", LocationImage.as_view(), name="dashboard"),
    path("like/<slug:slug>/", views.LikeLocationView.as_view(),
         name="like_location"),
    path("location/<slug:slug>/add_comment/", views.add_comment,
         name="add_comment"),
    path("edit_comment/<int:comment_id>/", views.edit_comment,
         name="edit_comment"),
    path("delete_comment/<int:comment_id>/", views.delete_comment,
         name="delete_comment"
         ),
    path("<slug:slug>/", views.LocationDetail.as_view(),
         name="location_detail"),
]
