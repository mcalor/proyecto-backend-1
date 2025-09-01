from django.urls import path
from .views import (
     NotaListView, NotaDetailView,
    NotaCreateView, NotaUpdateView, NotaDeleteView
)

urlpatterns = [
 path('', NotaListView.as_view(), name='lista-notas'),
 path('nota/<int:id>/', NotaDetailView.as_view(), name='detalle-nota'),
 path('nota/nueva/', NotaCreateView.as_view(), name='crearnota'),
 path('nota/<int:id>/editar/', NotaUpdateView.as_view(),name='editar-nota'),
 path('nota/<int:id>/eliminar/', NotaDeleteView.as_view(),name='eliminar-nota'),
]