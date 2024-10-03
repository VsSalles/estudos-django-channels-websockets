from django.db import models
from datetime import datetime

class Sala(models.Model):
    nome = models.CharField(max_length=10)
    senha = models.CharField(max_length=10)
    mensagens = models.TextField(null=True, blank=True)
    mensagem_data = models.DateTimeField(default=datetime.now(), null=True, blank=True)
    
    def __str__(self) -> str:
        return self.nome