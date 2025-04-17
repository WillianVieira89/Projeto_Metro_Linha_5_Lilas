from django.urls import path
from . import views

urlpatterns = [
    path('estacoes/', views.EstacaoListView.as_view(), name='estacao_list'),
    path('estacoes/<int:pk>/', views.EstacaoDetailView.as_view(), name='estacao_detail'),
    path('cdvs/<int:pk>/', views.CDVDetailView.as_view(), name='cdv_detail'),
    path('receptores/<int:pk>/', views.ReceptorDetailView.as_view(), name='receptor_detail'),
    path('nova-estacao/', views.EstacaoCreateView.as_view(), name='estacao_create'),
    path('novo-cdv/', views.CDVCreateView.as_view(), name='cdv_create'),
    path('novo-transmissor/', views.TransmissorCreateView.as_view(), name='transmissor_create'),
    path('novo-receptor/', views.ReceptorCreateView.as_view(), name='receptor_create'),
]
