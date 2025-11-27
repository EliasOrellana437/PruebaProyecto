from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('menu/', views.menu_view, name='menu'),
path('retos-diarios/', views.retos_diarios_view, name='retos_diarios'),

path('frases/', views.frases_utiles, name='frases'),
    path('frases/<slug:slug>/', views.frase_detalle, name='frase_detalle'),
]