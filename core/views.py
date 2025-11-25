# core/views.py
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

            # Loop para corrigir cada questão
            for questao in QUESTOES:
                id_q = questao['id']
                resposta_usuario = form.cleaned_data.get(id_q)
                resposta_certa = questao['correta']
                
                acertou = (resposta_usuario == resposta_certa)
                if acertou:
                    acertos += 1
                
                # Guarda o detalhe para mostrar quais errou/acertou
                respostas_detalhadas.append({
                    'titulo': questao['titulo'],
                    'acertou': acertou,
                    'formula': questao['formula']
                })

            nota_final = (acertos / total) * 10
            
            # Define cor e mensagem baseada na nota
            if nota_final >= 7:
                cor, msg = "bg-green-600", "Aprovado! Mandou bem no Cálculo. 📐"
            elif nota_final >= 4:
                cor, msg = "bg-yellow-600", "Na trave! Precisa revisar derivadas. 📚"
            else:
                cor, msg = "bg-red-600", "Reprovado. Vejo você na final. 😢"

            resultado = {
                'nota': f"{nota_final:.1f}",
                'texto': msg,
                'cor': cor,
                'detalhes': respostas_detalhadas
            }
            
            # Retorna com o resultado e um formulário limpo
            return render(request, 'index.html', {'form': Av2Form(), 'resultado': resultado})

    return render(request, 'index.html', {'form': form})