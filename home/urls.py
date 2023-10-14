from django.urls import path
from .views import Index
from .views import HomePageImage


urlpatterns = [
    path("", Index.as_view(), name="home"),
    path("", HomePageImage.as_view(), name="home"),
]
