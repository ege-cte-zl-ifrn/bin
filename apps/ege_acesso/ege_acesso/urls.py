from django.urls import path
from django.conf import settings
from django.views.generic.base import RedirectView, TemplateView
from .views import index_view, authorize_view, validate_view


urlpatterns = [
    path('', TemplateView.as_view(template_name="ege_acesso/acesso_errado.html",
                                  extra_context={'perfil_url': settings.LOGIN_REDIRECT_URL})),
    path('jwt/', TemplateView.as_view(template_name="ege_acesso/acesso_errado.html")),
    path('jwt/authorize/', authorize_view, name='authorize_view'),
    path('jwt/validate/', validate_view, name='validate_view'),
]
