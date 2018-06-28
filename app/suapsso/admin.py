from django.contrib. admin import register, ModelAdmin, TabularInline, StackedInline
from .models import Aplicacao, Protocolo, AplicacaoProtocolo


class AplicacaoProtocoloInline(TabularInline):
    model = AplicacaoProtocolo


@register(Protocolo)
class ProtocoloAdmin(ModelAdmin):
    pass


@register(Aplicacao)
class AplicacaoAdmin(ModelAdmin):
    inlines = (AplicacaoProtocoloInline,)


@register(AplicacaoProtocolo)
class AplicacaoProtocolo(ModelAdmin):
    list_display = ['aplicacao', 'protocolo', 'ativo', ]
    search_fields = ['aplicacao__nome', 'protocolo__nome']
    list_filter = ['ativo', 'protocolo__nome']

