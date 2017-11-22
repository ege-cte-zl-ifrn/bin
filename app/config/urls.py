from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^sso/admin/', admin.site.urls),
    url(r'^sso/cas/', include('cas_server.urls', namespace="cas_server")),
]
