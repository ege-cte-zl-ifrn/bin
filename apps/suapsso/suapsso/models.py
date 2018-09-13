from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, Permission
from django.db.models import Model, CharField, BooleanField, ForeignKey as OriginalForeignKey, DateTimeField

from django.db import models


class Input(models.Model):
    input_text = models.CharField(max_length=250)

    def __str__(self):
        return self.input_text


class ForeignKey(OriginalForeignKey):

    def __init__(self, verbose_name, to, on_delete=None, related_name=None, related_query_name=None,
                 limit_choices_to=None, parent_link=False, to_field=None, db_constraint=True, **kwargs):
        kwargs['verbose_name'] = verbose_name
        super(ForeignKey, self).__init__(to, on_delete, related_name, related_query_name, limit_choices_to,
                                         parent_link, to_field, db_constraint, **kwargs)


class Application(Model):
    name = CharField(_('name'), max_length=250)
    is_active = BooleanField(_('active'), default=True)

    class Meta:
        verbose_name = _("Application")
        verbose_name_plural = _("Applications")

    def __str__(self):
        return self.name


class Protocol(Model):
    name = CharField(_('name'), max_length=250)
    is_active = BooleanField(_('active'), default=True)

    class Meta:
        verbose_name = _("Protocolo")
        verbose_name_plural = _("Protocolos")

    def __str__(self):
        return self.name


class ProtocolApplication(Model):
    application = ForeignKey(_("Application"), Application)
    protocol = ForeignKey(_("Protocolo"), Protocol)
    is_active = BooleanField(_('active'), default=True)

    class Meta:
        verbose_name = _("Application x Protocol")
        verbose_name_plural = _("Applications x Protocols")
        unique_together = ('application', 'protocol')

    def __str__(self):
        return "%s - %s" % (self.application, self.protocol)


class Token(Model):
    user = ForeignKey(_("user"), User)
    token = CharField(_("token"), max_length=250)
    created = DateTimeField(_("created"), auto_now_add=True)
    expires = DateTimeField(_("expires"))
    is_full_permission = BooleanField(_("is full permission"), default=False)

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def __str__(self):
        return "%s - %s" % (self.user, self.token)


class TokenPermission(Model):
    token = ForeignKey(_("Token"), Token)
    permission = ForeignKey(_("permission"), Permission)

    class Meta:
        verbose_name = _("Token permission")
        verbose_name_plural = _("Token permissions")

    def __str__(self):
        return "%s - %s" % (self.token, self.permission)


class UserAttribute(Model):
    name = CharField(_('name'), max_length=250)

    class Meta:
        verbose_name = _("User attribute")
        verbose_name_plural = _("User attributes")

    def __str__(self):
        return self.name


class TokenAttribute(Model):
    token = ForeignKey(_("Token"), Token)
    user_attribute = ForeignKey(_("User attribute"), UserAttribute)

    class Meta:
        verbose_name = _("Token x User attribute")
        verbose_name_plural = _("Tokens x User attributes")

    def __str__(self):
        return "%s - %s" % (self.token, self.user_attribute)
