from django.contrib import admin

from .models import Apartamento, Bloco, Morador, Veículo

# Register your models here.
admin.site.register(Veículo)
admin.site.register(Morador)


class MoradorInlineAdmin(admin.TabularInline):
    model = Morador


@admin.register(Apartamento)
class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ("numero", "bloco")
    inlines = (MoradorInlineAdmin,)


@admin.register(Bloco)
class BlocoAdmin(admin.ModelAdmin):
    list_display = (
        "numero",
        "moradores",
    )
