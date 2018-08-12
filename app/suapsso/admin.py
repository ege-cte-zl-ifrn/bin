from django.contrib.admin import register, ModelAdmin, TabularInline, StackedInline
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as OriginalUserAdmin
from django.contrib.admin.sites import site
from .models import Application, Protocol, ProtocolApplication, Token, TokenAttribute, TokenPermission, UserAttribute


site.unregister(User)

User.get_full_name.short_description = _("Nome")


@register(User)
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
    list_display = ('username', 'status')
    # list_display = ('username', 'email', 'get_full_name', 'status')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

    def status(self, o):
        result = ""
        if o.is_superuser:
            result += "%s" % _("superuser")
        elif o.is_staff:
            result += "%s" % _("staff")
        else:
            result += "%s" % _("user")
        result += " %s" % (_("is active") if o.is_active else _("is inactive"))
        return result

    status.short_description = _('status')


class ProtocolApplicationInline(TabularInline):
    model = ProtocolApplication


class TokenAttributeInline(TabularInline):
    model = TokenAttribute


class TokenPermissionInline(TabularInline):
    model = TokenPermission


@register(Protocol)
class ProtocolAdmin(ModelAdmin):
    pass


@register(Application)
class ApplicationAdmin(ModelAdmin):
    inlines = (ProtocolApplicationInline,)
#
#
# @register(ProtocolApplication)
# class ProtocolApplicationAdmin(ModelAdmin):
#     list_display = ['application', 'protocol', 'is_active', ]
#     search_fields = ['application__name', 'protocol__name']
#     list_filter = ['is_active', 'protocol__name']


@register(Token)
class TokenAdmin(ModelAdmin):
    inlines = (TokenAttributeInline, TokenPermissionInline)
#
#
# @register(TokenAttribute)
# class TokenAttributeAdmin(ModelAdmin):
#     pass
#
#
# @register(TokenPermission)
# class TokenPermissionAdmin(ModelAdmin):
#     pass


@register(UserAttribute)
class UserAttributeAdmin(ModelAdmin):
    pass
