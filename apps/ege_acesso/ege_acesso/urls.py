from django.urls import path
from django.conf import settings
from django.views.generic.base import RedirectView
from .views import AuthorizeView, ValidateView


urlpatterns = [
    path('', RedirectView.as_view(url=settings.LOGIN_REDIRECT_URL), name='index'),
    path('jwt/', RedirectView.as_view(url=settings.LOGIN_REDIRECT_URL), name='jwt'),
    path('jwt/authorize/', AuthorizeView),
    path('jwt/validate/', ValidateView),
]
