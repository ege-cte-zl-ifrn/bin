from django.contrib.admin import register, ModelAdmin, TabularInline, StackedInline
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as OriginalUserAdmin
from django.contrib.admin.sites import site
from .models import Usuario, Aplicacao


# site.unregister(User)
# User.get_full_name.short_description = _("Nome")

@register(Usuario)
class UserAdmin(OriginalUserAdmin):
    readonly_fields = ('last_login', 'date_joined')
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('username', 'password', 'date_joined', 'last_login')}),
        # (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('username', 'password1', 'password2')}),
        # (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
    )
    list_display = ('username', 'get_full_name', 'status')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
    # status.short_description = _('status')


@register(Aplicacao)
class AplicacaoAdmin(ModelAdmin):
    pass
