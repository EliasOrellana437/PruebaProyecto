from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login'),
    path('menu/', views.menu_view, name='menu'),
path('retos-diarios/', views.retos_diarios_view, name='retos_diarios'),

path('frases/', views.frases_utiles, name='frases'),
    path('frases/<slug:slug>/', views.frase_detalle, name='frase_detalle'),

path('mini-juego/', views.mini_juego, name='mini_juego'),

# URL del índice (Lista A-Z)
    path('alfabeto/', views.alfabeto_view, name='alfabeto'), 
    
    # URL de detalle (Muestra la imagen)
    # <str:letra> captura la letra de la A a la Z
    path('alfabeto/<str:letra>/', views.detalle_seña_view, name='detalle_seña'),


 # Números
    path('numeros/', views.numeros_view, name='numeros'),
    path('numeros/<int:numero>/', views.numeros_senal_view, name='numeros_senal'),
]