import csv
from django.http import HttpResponse
from .models import Receptor
from django.contrib.auth.decorators import login_required

@login_required
def exportar_receptores_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="receptores.csv"'

    writer = csv.writer(response)
    writer.writerow(['Tipo', 'CDV', 'ITH', 'IAV', 'Relação'])

    for r in Receptor.objects.all():
        writer.writerow([r.tipo, r.cdv, r.ith, r.iav, r.relacao_ith_iav()])

    return response
