# Generated by Django 4.2.5 on 2023-09-26 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Apartamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("numero", models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name="Bloco",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("numero", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Morador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("eh_dono", models.BooleanField(default=True)),
                ("nome", models.CharField(max_length=90)),
                ("telefone", models.CharField(max_length=20)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "apartamento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="moradores",
                        to="condominio.apartamento",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "moradores",
            },
        ),
        migrations.CreateModel(
            name="Veículo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo",
                    models.CharField(
                        choices=[("carro", "Carro"), ("moto", "Moto")], max_length=10
                    ),
                ),
                ("placa", models.CharField(max_length=7)),
                (
                    "dono",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="veículos",
                        to="condominio.morador",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="apartamento",
            name="bloco",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="apartamentos",
                to="condominio.bloco",
            ),
        ),
    ]
