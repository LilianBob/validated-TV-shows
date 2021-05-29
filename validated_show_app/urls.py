from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('new', views.new_show),
    path('add_show', views.create),
    path('back', views.back),
    path('show/<int:show_id>', views.show),
    path('edit/<int:show_id>', views.edit),
    path('update/<int:show_id>', views.update),
    path('delete/<int:show_id>', views.delete),
]