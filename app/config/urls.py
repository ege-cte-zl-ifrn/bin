from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings

urlpatterns = [
    url(r'^%s/admin/' % settings.URL_PATH_PREFIX, admin.site.urls),
    url(r'^%s/cas/' % settings.URL_PATH_PREFIX, include('cas_server.urls', namespace="cas_server")),
    url(r'^%s/$' % settings.URL_PATH_PREFIX, RedirectView.as_view(url='/sso/admin/')),
    url(r'^$', RedirectView.as_view(url='/sso/admin/')),
]
