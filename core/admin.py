from django.contrib import admin
from .models import Estacao, CDV, Transmissor, Receptor

@admin.register(Estacao)
class EstacaoAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'nome')
    search_fields = ('sigla', 'nome')

@admin.register(CDV)
class CDVAdmin(admin.ModelAdmin):
    list_display = ('numero', 'estacao')
    list_filter = ('estacao',)
    search_fields = ('numero',)

@admin.register(Transmissor)
class TransmissorAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'cdv')
    list_filter = ('cdv',)

@admin.register(Receptor)
class ReceptorAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'cdv', 'ith', 'iav')
    list_filter = ('cdv',)
