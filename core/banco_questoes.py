# core/banco_questoes.py

# Lista de dicionários com todas as suas questões
QUESTOES = [
    # --- LIMITES ---
    {
        'id': 'lim_a',
        'categoria': 'Limites',
        'titulo': 'Substituição simples por fatoração',
        'contexto': 'Uma fábrica de embalagens mede o desperdício de material...',
        'formula': r'\lim_{x \to 3} \frac{x^2 - 9}{x - 3}',
        'opcoes': [('6', '6'), ('0', '0'), ('9', '9'), ('Indeterminado', 'Indeterminado')],
        'correta': '6'
    },
    {
        'id': 'lim_b',
        'categoria': 'Limites',
        'titulo': 'Racionalização',
        'contexto': 'Durante um teste de precisão, um operador compara o tempo...',
        'formula': r'\lim_{x\to 4} \frac{\sqrt{x} - 2}{x - 4}',
        'opcoes': [('0.25', '1/4'), ('0.5', '1/2'), ('0', '0'), ('1', '1')],
        'correta': '0.25'
    },
    {
        'id': 'lim_c',
        'categoria': 'Limites',
        'titulo': 'Trigonométrico Fundamental',
        'contexto': 'Uma antena vibra com pequenos ângulos devido ao vento...',
        'formula': r'\lim_{x\to 0} \frac{\sin(5x)}{x}',
        'opcoes': [('5', '5'), ('1', '1'), ('0', '0'), ('Infinite', 'Infinito')],
        'correta': '5'
    },
    {
        'id': 'lim_d',
        'categoria': 'Limites',
        'titulo': "L'Hôpital",
        'contexto': 'Um sistema mede a variação de entropia ao se aproximar do estado perfeito...',
        'formula': r'\lim_{x\to 1} \frac{\ln x}{x-1}',
        'opcoes': [('1', '1'), ('0', '0'), ('e', 'e'), ('-1', '-1')],
        'correta': '1'
    },
    {
        'id': 'lim_e',
        'categoria': 'Limites',
        'titulo': 'Infinito Positivo',
        'contexto': 'Uma empresa de logística analisa o crescimento do custo...',
        'formula': r'\lim_{x\to +\infty} \frac{3x^2 - 5}{x^2 + 7}',
        'opcoes': [('3', '3'), ('0', '0'), ('Infinite', 'Infinito'), ('-5/7', '-5/7')],
        'correta': '3'
    },
    
    # --- DERIVADAS (Exemplos selecionados para não ficar gigante, você pode adicionar o resto seguindo o padrão) ---
    {
        'id': 'der_a',
        'categoria': 'Derivadas',
        'titulo': 'Regra da Potência',
        'contexto': 'Um programador analisa o tempo que um algoritmo leva para rodar...',
        'formula': r'f(x)=7x^5 - 3x^2 + 8',
        'opcoes': [('35x^4 - 6x', '35x⁴ - 6x'), ('7x^4 - 3x', '7x⁴ - 3x'), ('35x^5 - 6x^2', '35x⁵ - 6x²'), ('5x^4', '5x⁴')],
        'correta': '35x^4 - 6x'
    },
    {
        'id': 'der_f',
        'categoria': 'Derivadas',
        'titulo': 'Seno (Cadeia)',
        'contexto': 'Um braço robótico oscila seguindo a função:',
        'formula': r'f(x)=6\sin(4x)',
        'opcoes': [('24cos(4x)', '24cos(4x)'), ('6cos(4x)', '6cos(4x)'), ('-24sin(4x)', '-24sin(4x)'), ('24sin(x)', '24sin(x)')],
        'correta': '24cos(4x)'
    },

    # --- INTEGRAIS ---
    {
        'id': 'int_a',
        'categoria': 'Integrais',
        'titulo': 'Integral Polinomial',
        'contexto': 'O total de gasto energético de um equipamento...',
        'formula': r'\int (3x^2 + 4x - 7) dx',
        'opcoes': [('x^3 + 2x^2 - 7x + C', 'x³ + 2x² - 7x + C'), ('6x + 4', '6x + 4'), ('x^3 + x^2 - 7x', 'x³ + x² - 7x'), ('3x^3 + 4x^2', '3x³ + 4x²')],
        'correta': 'x^3 + 2x^2 - 7x + C'
    },
]