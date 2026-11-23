from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('records/', views.training_list, name='training_list'),

    path('records/add/', views.training_create, name='training_create'),

    path(
        'records/<int:pk>/edit/',
        views.training_update,
        name='training_update'
    ),

    path(
        'records/<int:pk>/delete/',
        views.training_delete,
        name='training_delete'
    ),
]