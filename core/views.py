from django.shortcuts import render
from .forms import Av2Form
from .banco_questoes import QUESTOES

def home(request):
    form = Av2Form()
    resultado = None

    if request.method == 'POST':
        form = Av2Form(request.POST)
        
        if form.is_valid():
            acertos = 0
            total = len(QUESTOES)
            respostas_detalhadas = []

            for questao in QUESTOES:
                q_id = questao['id']
                resposta_usuario = form.cleaned_data.get(q_id)
                
                # Pega o rascunho específico desta questão
                desenho_usuario = form.cleaned_data.get(f'rascunho_{q_id}')
                
                acertou = (resposta_usuario == questao['correta'])
                if acertou:
                    acertos += 1
                
                respostas_detalhadas.append({
                    'titulo': questao['titulo'],
                    'acertou': acertou,
                    'formula': questao['formula'],
                    'desenho': desenho_usuario  # Guardamos o desenho no detalhe da questão
                })

            nota_final = (acertos / total) * 10
            
            # Definição da mensagem/cor
            if nota_final >= 7:
                cor, msg = "bg-green-600", "Aprovado! 📐"
            elif nota_final >= 4:
                cor, msg = "bg-yellow-600", "Na trave! 📚"
            else:
                cor, msg = "bg-red-600", "Reprovado. 😢"

            resultado = {
                'nota': f"{nota_final:.1f}",
                'texto': msg,
                'cor': cor,
                'detalhes': respostas_detalhadas
            }
            
            return render(request, 'index.html', {'form': Av2Form(), 'resultado': resultado})

    return render(request, 'index.html', {'form': form})