from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Receptor

@login_required
def grafico_receptores(request):
    labels = []
    dados = []
    for r in Receptor.objects.all():
        if r.relacao_ith_iav():
            labels.append(f"{r.tipo} ({r.pk})")
            dados.append(r.relacao_ith_iav())
    return render(request, 'core/grafico.html', {'labels': labels, 'dados': dados})
