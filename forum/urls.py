from django.urls import path
from . import views


urlpatterns = [
    path('nuova-sezione', views.CreaSezione.as_view(), name='crea_sezione'),
    path('sezione/<int:pk>', views.visualizza_sezione, name='sezione'),
    path('sezione/<int:pk>/crea-discussione/', views.crea_discussione,          name='crea_discussione'),
    path('discussione/<int:pk>', views.visualizza_discussione, name='discussione'),
    path('discussione/<int:pk>/rispondi/>', views.aggiungi_risposta, name='rispondi_discussione'),
]