from django.urls import path
from . import views

app_name = 'oficinas'

urlpatterns = [
    path('', views.OficinaListView.as_view(), name='lista'),
    path('<int:pk>/', views.OficinaDetailView.as_view(), name='detalle'),
    path('crear/', views.oficina_crear, name='crear'),
    path('<int:pk>/editar/', views.oficina_editar, name='editar'),
    path('<int:pk>/eliminar/', views.oficina_eliminar, name='eliminar'),
    path('carga-masiva/', views.carga_masiva_oficinas, name='carga_masiva'),
]