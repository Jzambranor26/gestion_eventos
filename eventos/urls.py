from django.urls import path
from .views import (
    registro_view,
    login_view,
    logout_view,
    evento_create_view,
    evento_list_view,
    evento_detail_view,
    inscripcion_create_view,
    usuario_inscripciones_view,
    inscripcion_delete_view,
    index_view, evento_delete_view,
)

urlpatterns = [
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('evento/nuevo/', evento_create_view, name='evento_create'),
    path('eventos/', evento_list_view, name='evento_list'),
    path('evento/<int:pk>/', evento_detail_view, name='evento_detail'),
    path('evento/<int:pk>/inscribirse/', inscripcion_create_view, name='inscripcion_create'),
    path('mis-inscripciones/', usuario_inscripciones_view, name='usuario_inscripciones_view'),
    path('inscripcion/<int:pk>/eliminar/', inscripcion_delete_view, name='inscripcion_delete'),
    path('evento/<int:pk>/eliminar/', evento_delete_view, name='evento_delete'),
    path('mis-inscripciones/', usuario_inscripciones_view, name='usuario_inscripciones_view'),
    path('', index_view, name='index'),
]


