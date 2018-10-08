from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.models import CharField, DateTimeField, BooleanField, TextField
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    """
department	COTIC/EAD
displayName	Kelson da Costa Medeiros
extensionAttribute1	DG/EAD
extensionAttribute10	Ativo
extensionAttribute2	Técnico-administrativo
extensionAttribute3	FG1
extensionAttribute4	kelson.medeiros@academico.ifrn.edu.br
extensionAttribute6	64583457120
mail	kelson.medeiros@ifrn.edu.br
sAMAccountName	2080882
givenName	Kelson
sn	da Costa Medeiros
title	ANALISTA DE TEC DA INFORMACAO
whenChanged	20181002201926.0Z
whenCreated	20140117104211.0Z    
pwdLastSet	02/10/2018 20:19
thumbnailPhoto
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
    created_at = CharField(_('whenCreated'), max_length=150, null=True, blank=True)
    changed_at = CharField(_('whenChanged'), max_length=150, null=True, blank=True)
    password_set_at = CharField(_('pwdLastSet'), max_length=150, null=True, blank=True)
    last_access = DateTimeField(_('last access'), null=True, blank=True)
    date_joined = DateTimeField(_('date joined'), default=timezone.now)

    def save(self, *args, **kwargs):
        self.is_active = 'Ativo' == self.ativo
        super().save(*args, **kwargs)

    @property
    def presentation_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')
        ordering = ['first_name']
