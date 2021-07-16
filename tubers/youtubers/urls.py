from django.urls import path
from . import views


urlpatterns = [
     path('', views.youtubers, name="youtubers"),
     path('<int:id>', views.youtubers_detail, name="youtubers_detail"),
     path('search', views.search, name="search"),
     path('set_youtubers', views.set_youtubers, name="set_youtubers"),
    
]