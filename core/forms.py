from django import forms
from .banco_questoes import QUESTOES

class Av2Form(forms.Form):
    # Campo de nome obrigatório
    nome_aluno = forms.CharField(
        label="Seu Nome Completo",
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full bg-gray-700 text-white border border-gray-600 rounded p-3 focus:outline-none focus:border-blue-500 font-bold',
            'placeholder': 'Digite seu nome aqui...'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for questao in QUESTOES:
            q_id = questao['id']
            
            self.fields[q_id] = forms.ChoiceField(
                label=questao['titulo'],
                choices=questao['opcoes'],
                required=False,
                widget=forms.RadioSelect(attrs={
                    'class': 'mb-2 text-gray-300 focus:ring-blue-500'
                })
            )
            self.fields[q_id].contexto = questao['contexto']
            self.fields[q_id].formula = questao['formula']
            self.fields[q_id].categoria = questao['categoria']

            self.fields[f'rascunho_{q_id}'] = forms.CharField(
                required=False, 
                widget=forms.HiddenInput()
            )