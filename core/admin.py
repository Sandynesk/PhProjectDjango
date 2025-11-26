from django.contrib import admin
from django.utils.html import mark_safe
from .models import AlunoProva

@admin.register(AlunoProva)
class ProvaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nota_formatada', 'status', 'data_envio')
    list_filter = ('data_envio',)
    search_fields = ('nome',)
    
    # Deixa a visualização apenas leitura (para ninguém alterar a nota na maldade)
    readonly_fields = ('visualizar_prova',)
    exclude = ('dados_json',) # Esconde o JSON bruto feio

    def nota_formatada(self, obj):
        return f"{obj.nota:.1f}"
    nota_formatada.short_description = "Nota"

    def status(self, obj):
        if obj.nota >= 7:
            return mark_safe('<span style="color:green; font-weight:bold;">APROVADO</span>')
        return mark_safe('<span style="color:red; font-weight:bold;">REPROVADO</span>')

    # Essa função gera o HTML para ver os desenhos dentro do painel admin
    def visualizar_prova(self, obj):
        html = '<div style="background:#f0f2f5; padding:15px; border-radius:10px;">'
        
        detalhes = obj.dados_json.get('detalhes', [])
        
        for item in detalhes:
            cor_borda = "green" if item.get('acertou') else "red"
            status_icon = "✅" if item.get('acertou') else "❌"
            
            html += f'''
            <div style="background:white; border-left: 5px solid {cor_borda}; padding: 15px; margin-bottom: 10px; border-radius: 5px;">
                <h3 style="margin:0 0 10px 0;">{item['titulo']} {status_icon}</h3>
                <p><strong>Fórmula:</strong> $${item['formula']}$$</p>
            '''
            
            if item.get('desenho'):
                html += f'''
                <div style="margin-top:10px; border:1px dashed #ccc; padding:5px; text-align:center;">
                    <small>Rascunho do Aluno:</small><br>
                    <img src="{item['desenho']}" style="max-width:100%; height:auto; border:1px solid #ddd;">
                </div>
                '''
            else:
                html += '<p style="color:#999;"><i>Sem rascunho.</i></p>'
                
            html += '</div>'
            
        html += '</div>'
        return mark_safe(html)

    visualizar_prova.short_description = "Gabarito e Rascunhos"