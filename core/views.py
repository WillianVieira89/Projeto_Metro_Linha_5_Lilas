from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView
from .models import Estacao, CDV, Transmissor, Receptor
from .forms import EstacaoForm, CDVForm, TransmissorForm, ReceptorForm

@method_decorator(login_required, name='dispatch')
class EstacaoListView(ListView):
    model = Estacao
    template_name = 'core/estacao_list.html'

@method_decorator(login_required, name='dispatch')
class EstacaoDetailView(DetailView):
    model = Estacao
    template_name = 'core/estacao_detail.html'

@method_decorator(login_required, name='dispatch')
class CDVDetailView(DetailView):
    model = CDV
    template_name = 'core/cdv_detail.html'

@method_decorator(login_required, name='dispatch')
class ReceptorDetailView(DetailView):
    model = Receptor
    template_name = 'core/receptor_detail.html'

@method_decorator(login_required, name='dispatch')
class EstacaoCreateView(CreateView):
    model = Estacao
    form_class = EstacaoForm
    template_name = 'core/form.html'

@method_decorator(login_required, name='dispatch')
class CDVCreateView(CreateView):
    model = CDV
    form_class = CDVForm
    template_name = 'core/form.html'

@method_decorator(login_required, name='dispatch')
class TransmissorCreateView(CreateView):
    model = Transmissor
    form_class = TransmissorForm
    template_name = 'core/form.html'

@method_decorator(login_required, name='dispatch')
class ReceptorCreateView(CreateView):
    model = Receptor
    form_class = ReceptorForm
    template_name = 'core/form.html'
