from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Avg
from .forms import Av2Form
from .banco_questoes import QUESTOES
from .models import AlunoProva

# 1. VIEW DA PROVA (HOME)
def home(request):
    # --- PARTE A: Verifica se o aluno já fez a prova (Persistência) ---
    prova_id = request.session.get('prova_id_av2')
    
    if prova_id:
        try:
            prova_anterior = AlunoProva.objects.get(id=prova_id)
            resultado = {
                'nota': f"{prova_anterior.nota:.1f}",
                'texto': "Prova Recuperada (Você já enviou)",
                'cor': "bg-blue-600" if prova_anterior.nota >= 7 else "bg-gray-600",
                'detalhes': prova_anterior.dados_json.get('detalhes', [])
            }
            return render(request, 'index.html', {'resultado': resultado})
        except AlunoProva.DoesNotExist:
            del request.session['prova_id_av2']

    # --- PARTE B: Processa o envio da prova ---
    form = Av2Form()
    if request.method == 'POST':
        form = Av2Form(request.POST)
        
        if form.is_valid():
            nome = form.cleaned_data['nome_aluno']
            acertos = 0
            total = len(QUESTOES)
            respostas_detalhadas = []

            for questao in QUESTOES:
                q_id = questao['id']
                resposta_usuario = form.cleaned_data.get(q_id)
                desenho_usuario = form.cleaned_data.get(f'rascunho_{q_id}')
                
                if not resposta_usuario:
                    status = "nao_respondeu"
                    acertou = False
                elif resposta_usuario == questao['correta']:
                    status = "acertou"
                    acertou = True
                    acertos += 1
                else:
                    status = "errou"
                    acertou = False
                
                respostas_detalhadas.append({
                    'id': q_id,
                    'titulo': questao['titulo'],
                    'acertou': acertou,
                    'status': status,
                    'formula': questao['formula'],
                    'desenho': desenho_usuario
                })

            nota_final = (acertos / total) * 10
            
            if nota_final >= 7:
                cor, msg = "bg-green-600", f"Parabéns {nome}! Aprovado. 📐"
            elif nota_final >= 4:
                cor, msg = "bg-yellow-600", f"{nome}, foi na trave! 📚"
            else:
                cor, msg = "bg-red-600", f"{nome}, reprovado. 😢"

            # Salva no Banco de Dados
            nova_prova = AlunoProva.objects.create(
                nome=nome,
                nota=nota_final,
                dados_json={'detalhes': respostas_detalhadas}
            )
            
            # Salva o ID na sessão para bloquear novas tentativas
            request.session['prova_id_av2'] = nova_prova.id

            resultado = {
                'nota': f"{nota_final:.1f}",
                'texto': msg,
                'cor': cor,
                'detalhes': respostas_detalhadas
            }
            
            return render(request, 'index.html', {'form': Av2Form(), 'resultado': resultado})

    return render(request, 'index.html', {'form': form})


# 2. VIEW PARA REINICIAR (NOVA TENTATIVA)
def reiniciar_prova(request):
    # Limpa a "memória" de que o aluno já fez a prova
    if 'prova_id_av2' in request.session:
        del request.session['prova_id_av2']
    return redirect('/')


# 3. VIEW DE RELATÓRIOS (PAINEL DO PROFESSOR)
@staff_member_required
def relatorios(request):
    provas = AlunoProva.objects.all()
    total_alunos = provas.count()
    
    # Calcula média geral (se não tiver aluno, é 0)
    media_agregada = provas.aggregate(Avg('nota'))['nota__avg']
    media_geral = f"{media_agregada:.1f}" if media_agregada is not None else "0.0"
    
    # Estrutura para contar acertos e erros por questão
    stats_questoes = {}
    # Inicializa o contador
    for q in QUESTOES:
        stats_questoes[q['id']] = {'titulo': q['titulo'], 'acertos': 0, 'erros': 0}

    # Percorre todas as provas no banco para somar as estatísticas
    for prova in provas:
        detalhes = prova.dados_json.get('detalhes', [])
        for item in detalhes:
            q_id = item.get('id')
            
            # Fallback: se for prova antiga sem ID, tenta achar pelo título
            if not q_id: 
                for q_ref in QUESTOES:
                    if q_ref['titulo'] == item.get('titulo'):
                        q_id = q_ref['id']
                        break
            
            if q_id and q_id in stats_questoes:
                if item.get('acertou'):
                    stats_questoes[q_id]['acertos'] += 1
                else:
                    stats_questoes[q_id]['erros'] += 1

    # Prepara listas simples para o gráfico (Chart.js gosta de listas)
    labels = [q['titulo'] for q in QUESTOES]
    data_acertos = [stats_questoes[q['id']]['acertos'] for q in QUESTOES]
    data_erros = [stats_questoes[q['id']]['erros'] for q in QUESTOES]

    context = {
        'total_alunos': total_alunos,
        'media_geral': media_geral,
        'labels': labels,
        'data_acertos': data_acertos,
        'data_erros': data_erros,
    }
    
    # Precisamos garantir que existe o template 'relatorios.html'
    return render(request, 'relatorios.html', context)