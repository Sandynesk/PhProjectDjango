from django import forms
from .banco_questoes import QUESTOES

class Av2Form(forms.Form):
    # Gerando os campos dinamicamente
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Para cada questão.
        for questao in QUESTOES:
            field_name = questao['id']
            
            # Criamos um campo de Múltipla Escolha
            self.fields[field_name] = forms.ChoiceField(
                label=questao['titulo'],
                choices=questao['opcoes'],
                widget=forms.RadioSelect(attrs={
                    'class': 'mb-2 text-gray-300 focus:ring-blue-500'
                })
            )
            # Adicionamos atributos extras para usar no HTML (Contexto e Fórmula LaTeX)
            self.fields[field_name].contexto = questao['contexto']
            self.fields[field_name].formula = questao['formula']
            self.fields[field_name].categoria = questao['categoria']