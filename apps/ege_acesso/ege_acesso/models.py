from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.models import Model, ForeignKey, CASCADE
from django.db.models import CharField, DateTimeField, BooleanField, TextField, FileField, PositiveIntegerField
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Usuario(AbstractUser):
    """
department:	Setor/Campus
displayName:	Nome completo do cara
extensionAttribute1:	Setor superior/Campus
extensionAttribute10:	Ativo
extensionAttribute2:	Cargo
extensionAttribute3:	Função
extensionAttribute4:	nome.sobrenoem@academico.email.edu.br
extensionAttribute6:	12345678901
mail:	nome.sobrenoem@email.edu.br
sAMAccountName:	1234567
givenName:	Nome
sn:	completo do cara
title:	Cargo
whenChanged:	20010203040506.0Z
whenCreated:	20010203040506.0Z
pwdLastSet:	03/02/2001 04:05
thumbnailPhoto:
    """
    username = CharField(_('username'), max_length=150, primary_key=True)
    first_name = CharField(_('givenName'), max_length=150, null=True, blank=True)
    last_name = CharField(_('sn'), max_length=150, null=True, blank=True)
    social_name = CharField(_('social_name'), max_length=150, null=True, blank=True)
    department = CharField(_('department'), max_length=150, null=True, blank=True)
    campus = CharField(_('extensionAttribute1'), max_length=150, null=True, blank=True)
    ativo = CharField(_('extensionAttribute10'), max_length=150, null=True, blank=True)
    is_active = BooleanField(_('Está ativo?'), default=True)
    is_staff = BooleanField(_('staff status'), default=False)
    is_superuser = BooleanField(_('superuser status'), default=False)
    carrer = CharField(_('extensionAttribute2'), max_length=150, null=True, blank=True)
    job = CharField(_('extensionAttribute3'), max_length=150, null=True, blank=True)
    cpf = CharField(_('extensionAttribute6'), max_length=150, null=True, blank=True)
    academic_email = CharField(_('extensionAttribute4'), max_length=150, null=True, blank=True)
    enterprise_email = CharField(_('mail'), max_length=150, null=True, blank=True)
    email = CharField(_('personal mail'), max_length=150, null=True, blank=True)
    title = CharField(_('title'), max_length=150, null=True, blank=True)
    photo_blob = TextField(_('thumbnailPhoto'), null=True, blank=True)
    created_at = DateTimeField(_('whenCreated'), max_length=150, null=True, blank=True)
    changed_at = DateTimeField(_('whenChanged'), max_length=150, null=True, blank=True)
    password_set_at = DateTimeField(_('pwdLastSet'), max_length=150, null=True, blank=True)
    last_access = DateTimeField(_('last access'), null=True, blank=True)
    last_ad_access_at = DateTimeField(_('last access'), null=True, blank=True)
    date_joined = DateTimeField(_('date joined'), default=timezone.now)
    first_access_at = DateTimeField(_('last access'), null=True, blank=True)

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')
        ordering = ['first_name']

    def __str__(self):
        return "%s (%s as a %s)" % (self.username, self.presentation_name, self.status)

    def save(self, *args, **kwargs):
        self.is_active = 'Ativo' == self.ativo
        super().save(*args, **kwargs)

    @property
    def presentation_name(self):
        if self.social_name is not None:
            return self.social_name
        elif self.first_name is not None and self.last_name is not None:
            return "%s %s" % (self.first_name, self.last_name)
        else:
            return self.username

    @property
    def status(self):
        result = ""
        if self.is_superuser:
            result += "%s" % _("superuser")
        elif self.is_staff:
            result += "%s" % _("staff")
        else:
            result += "%s" % _("user")
        result += " %s" % (_("is active") if self.is_active else _("is inactive"))
        return result


class Aplicacao(Model):
    responsavel = ForeignKey(verbose_name=_('Responsável'), to=Usuario, on_delete=CASCADE)
    nome = CharField(_('Nome'), max_length=150)
    descricao = TextField(_('Descrição'), null=True, blank=True)
    client_id = CharField(_('Cliend ID'), max_length=150)
    segredo = CharField(_('Segredo do cliente'), max_length=150)
    logo = FileField(_('logo'), null=True, blank=True)
    urls_callbacks_permitidas = TextField(_('URLs de callback permitidas'), null=True, blank=True)
    urls_origem_permitidas = TextField(_('URLs de origem permitidas'), null=True, blank=True)
    expiracao = PositiveIntegerField(_('Expira em segundos'), default=300)
    criado_em = DateTimeField(_('whenCreated'))
    excluido_em = DateTimeField(_('is deleted'), null=True, blank=True)

    class Meta:
        verbose_name = _('Aplicação')
        verbose_name_plural = _('Aplicações')

    def __str__(self):
        return "%s [%s]" % (self.nome, self.responsavel)


class TransationToken(Model):
    aplicacao = ForeignKey(verbose_name=_('Aplicação'), to=Aplicacao, on_delete=CASCADE)
    usuario = ForeignKey(verbose_name=_('Usuário'), to=Usuario, on_delete=CASCADE)
    hashcode = CharField(_('Hash'), max_length=150)
    state = CharField(_('state'), max_length=150)
    redirect_uri = CharField(_('redirect_uri'), max_length=150)
    referer = CharField(_('referer'), max_length=150)
    expiracao = DateTimeField(_('Expira em'))

    class Meta:
        verbose_name = _('Token de transação')
        verbose_name_plural = _('Tokens de transações')

    def __str__(self):
        return "%s - %s - %s" % (self.hash, self.aplicacao, self.expiracao)
