from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),	
    path('dashboard', views.dashboard),
    path('login', views.login),	
    path('logout', views.logout),
    path('createpie', views.create_pie),
    path('edit/<int:num>', views.edit),
    path('edit', views.edit_pie),
    path('delete/<int:ip>', views.delete_pie),
    path('pies', views.display_all_pies),
    path('show/<int:ic>', views.show),
    path('vote', views.voting),
    
    
]
