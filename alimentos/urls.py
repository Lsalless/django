from django.urls import path
from . import views

urlpatterns = [
    path('', views.alimento_list, name='alimento_list'),
    path('novo/', views.alimento_create, name='alimento_create'),
    path('editar/<int:pk>/', views.alimento_update, name='alimento_update'),
    path('deletar/<int:pk>/', views.alimento_delete, name='alimento_delete'),
]
