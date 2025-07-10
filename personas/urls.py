from django.urls import path
from . import views

app_name = 'personas'

urlpatterns = [
    path('', views.PersonaListView.as_view(), name='lista'),
    path('<int:pk>/', views.PersonaDetailView.as_view(), name='detalle'),
    path('crear/', views.persona_crear, name='crear'),
    path('<int:pk>/editar/', views.persona_editar, name='editar'),
    path('<int:pk>/eliminar/', views.persona_eliminar, name='eliminar'),
    path('carga-masiva/', views.carga_masiva_personas, name='carga_masiva'),
]