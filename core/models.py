from django.db import models

class AlunoProva(models.Model):
    nome = models.CharField("Nome do Aluno", max_length=150)
    nota = models.FloatField("Nota Final")
    data_envio = models.DateTimeField(auto_now_add=True)
    
    # Aqui guardaremos as respostas e os desenhos (Base64) como um texto gigante
    # Ex: [{'titulo': 'Questão 1', 'desenho': 'data:image...', 'acertou': True}]
    dados_json = models.JSONField("Detalhes da Prova", default=dict)

    def __str__(self):
        return f"{self.nome} - Nota: {self.nota}"

    class Meta:
        verbose_name = "Prova Entregue"
        verbose_name_plural = "Provas Entregues"
        ordering = ['-data_envio']