# myapp/urls.py

from django.urls import path, re_path
from . import views 
urlpatterns = [
    path('',views.lobby),
   path("<str:room_name>/", views.room, name="room"),
 
]
