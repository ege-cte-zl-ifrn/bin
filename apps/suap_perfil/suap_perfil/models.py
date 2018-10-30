from django.utils.translation import gettext as _
from django.db.models import Model, CharField, TextField, NullBooleanField, FileField, ForeignKey, CASCADE
from django.contrib.auth.models import User


class Perfil(Model):
    usuario = ForeignKey(User, verbose_name=_('Usuário'), on_delete=CASCADE)
    polo_nome = CharField(_('Nome do pólo'), max_length=250, blank=True, null=True)
    polo_codigo = CharField(_('Código do pólo'), max_length=250, blank=True, null=True)
    campus_nome = CharField(_('Nome do campus'), max_length=250, blank=True, null=True)
    campus_codigo = CharField(_('Código do campus'), max_length=250, blank=True, null=True)
    biografia = TextField(_('Biografia'), blank=True, null=True)
    email_publico = NullBooleanField(_('Exibir para todos'))
    necessidade_especial_publico = NullBooleanField(_('Exibir para todos'))

    class Meta:
        verbose_name = _('Perfil')
        verbose_name_plural = _('Perfis')


class PerfilFoto(Model):
    imagem = FileField(_('Exibir para todos'))
    status = FileField(_('Exibir para todos'))
    solicitada_em = FileField(_('Exibir para todos'))
    homologacao_em = FileField(_('Exibir para todos'))
    homologacao_por = FileField(_('Exibir para todos'))
    

class OpcoesAcessibilidade(Model):
    fonte_tamanho = CharField(_('Exibir para todos'), max_length=250, blank=True, null=True)
    paleta = CharField(_('Exibir para todos'), max_length=250, blank=True, null=True)
    legendagem = NullBooleanField(_('Exibir para todos'), max_length=250, blank=True, null=True)
    libras = NullBooleanField(_('Exibir para todos'), max_length=250, blank=True, null=True)
    ledor = NullBooleanField(_('Exibir para todos'), max_length=250, blank=True, null=True)


class NecessidadeEspecial(Model):
    nome = CharField(_('Exibir para todos'), max_length=250, blank=True, null=True)


class PerfilNecessidadeEspecial(Model):
    nome = CharField(_('Exibir para todos'), max_length=250, blank=True, null=True)
