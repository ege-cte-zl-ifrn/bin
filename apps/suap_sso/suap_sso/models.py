from django.utils.translation import gettext_lazy as _
from django.db.models import CharField, DateTimeField
from django.contrib.auth.models import AbstractUser


# class Usuario(AbstractUser):
#     username = CharField(_('username'), max_length=150, primary_key=True)
#     last_access = DateTimeField(_('last access'), null=True, blank=True)

#     class Meta:
#         verbose_name = _('Usuário')
#         verbose_name_plural = _('Usuários')
#         ordering = ['first_name']
