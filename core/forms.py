from django import forms
from .banco_questoes import QUESTOES

class Av2Form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for questao in QUESTOES:
            q_id = questao['id']
            
            # 1. Campo da Pergunta (Radio)
            self.fields[q_id] = forms.ChoiceField(
                label=questao['titulo'],
                choices=questao['opcoes'],
                widget=forms.RadioSelect(attrs={
                    'class': 'mb-2 text-gray-300 focus:ring-blue-500'
                })
            )
            # Metadados para o HTML
            self.fields[q_id].contexto = questao['contexto']
            self.fields[q_id].formula = questao['formula']
            self.fields[q_id].categoria = questao['categoria']

            # 2. Campo do Rascunho (Escondido, exclusivo para essa questão)
            # Nome será tipo: rascunho_lim_a, rascunho_der_b...
            self.fields[f'rascunho_{q_id}'] = forms.CharField(
                required=False, 
                widget=forms.HiddenInput()
            )