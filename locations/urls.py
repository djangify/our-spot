from django.urls import path
from .views import (
    AddLocation, Locations,
    LocationDetail, DeleteLocation,
    EditLocation
)


urlpatterns = [

    path("add/", AddLocation.as_view(), name="add_location"),
    path("", Locations.as_view(), name="locations"),
    path("<slug:pk>/", LocationDetail.as_view(), name="location_detail"),
    path("delete/<slug:pk>/", DeleteLocation.as_view(), name="delete_location"),
    path("edit/<slug:pk>/", EditLocation.as_view(), name="edit_location",)
]
