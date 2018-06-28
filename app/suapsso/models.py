from django.db.models import Model, CharField, BooleanField, ForeignKey as OriginalForeignKey


class ForeignKey(OriginalForeignKey):

    def __init__(self, verbose_name, to, on_delete=None, related_name=None, related_query_name=None,
                 limit_choices_to=None, parent_link=False, to_field=None, db_constraint=True, **kwargs):
        kwargs['verbose_name'] = verbose_name
        super(ForeignKey, self).__init__(to, on_delete, related_name, related_query_name, limit_choices_to,
                                         parent_link, to_field, db_constraint, **kwargs)


class Aplicacao(Model):
    nome = CharField('Nome', max_length=250)
    ativo = BooleanField('Ativo')

    class Meta:
        verbose_name = "Aplicação"
        verbose_name_plural = "Aplicações"

    def __str__(self):
        return self.nome


class Protocolo(Model):
    nome = CharField('Nome', max_length=250, unique=True)
    ativo = BooleanField('Ativo')

    class Meta:
        verbose_name = "Protocólo"
        verbose_name_plural = "Protocólos"

    def __str__(self):
        return self.nome


class AplicacaoProtocolo(Model):
    aplicacao = ForeignKey('Aplicação', Aplicacao)
    protocolo = ForeignKey('Protocolo', Protocolo)
    ativo = BooleanField('Ativo')

    class Meta:
        verbose_name = "Aplicação x Protocólo"
        verbose_name_plural = "Aplicações x Protocólos"
        unique_together = ('aplicacao', 'protocolo')

    def __str__(self):
        return "%s - %s" % (self.aplicacao, self.protocolo)
