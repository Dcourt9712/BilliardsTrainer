from django.urls import path
from . import views

app_name = "map_view"

urlpatterns = [
  path('', views.route, name="route"),
  path('map', views.map, name="map"),
]
