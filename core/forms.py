from django import forms
from .models import Estacao, CDV, Transmissor, Receptor

class EstacaoForm(forms.ModelForm):
    class Meta:
        model = Estacao
        fields = '__all__'

class CDVForm(forms.ModelForm):
    class Meta:
        model = CDV
        fields = '__all__'

class TransmissorForm(forms.ModelForm):
    class Meta:
        model = Transmissor
        fields = '__all__'

class ReceptorForm(forms.ModelForm):
    class Meta:
        model = Receptor
        fields = '__all__'
