from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Veículo(models.Model):
    tipo = models.CharField(
        choices=(("carro", "Carro"), ("moto", "Moto")), max_length=10
    )
    dono = models.ForeignKey(
        "Morador", on_delete=models.CASCADE, related_name="veículos"
    )
    placa = models.CharField(max_length=7)


class Apartamento(models.Model):
    numero = models.CharField(max_length=4)
    bloco = models.ForeignKey(
        "Bloco",
        null=False,
        on_delete=models.CASCADE,
        related_name="apartamentos",
    )

    def __str__(self) -> str:
        return f"Bloco: {self.bloco} - Número: {self.numero}"


class Morador(models.Model):
    eh_dono = models.BooleanField(default=True, verbose_name="É dono?")
    nome = models.CharField(max_length=90)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, null=True, blank=True)
    apartamento = models.ForeignKey(
        "Apartamento",
        null=False,
        on_delete=models.CASCADE,
        related_name="moradores",
        related_query_name="morador",
    )

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name_plural = "moradores"


class Bloco(models.Model):
    numero = models.CharField(max_length=50)

    @property
    def moradores(self):
        apartamentos = self.apartamentos.all()
        return [ap for ap in apartamentos if ap]

    def __str__(self) -> str:
        return self.numero
