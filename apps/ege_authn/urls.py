"""
The MIT License (MIT)

Copyright 2015 Umbrella Tech.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
import oauth2_provider.views as oauth2_views
from django.conf.urls.static import static


def redirect_to(to):
    return RedirectView.as_view(url=to)


urlpatterns = [
    path(
        settings.URL_PATH_PREFIX,
        include(
            [
                path('', include('suap_acesso.urls')),
                path('admin/', admin.site.urls),
                path('accounts/', include('django.contrib.auth.urls')),
                path('sso/oauth/', include(('oauth2_provider.urls', 'oauth2_provider_app', ), namespace='oauth2_provider'),),
                # OAuth 2 endpoints:
                path('api/hello', include('suap_acesso.urls')),
                path('secret', include('suap_acesso.urls')),
            ]
        )
    ),
    path('', redirect_to(settings.URL_PATH_PREFIX))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# OAuth2 provider endpoints
oauth2_endpoint_views = [
    path('authorize/$', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    path('token/$', oauth2_views.TokenView.as_view(), name="token"),
    path('revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

if settings.DEBUG:
    # OAuth2 Application Management endpoints
    oauth2_endpoint_views += [
        path('applications/$', oauth2_views.ApplicationList.as_view(), name="list"),
        path('applications/register/$', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        path('applications/(?P<pk>\d+)/$', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        path('applications/(?P<pk>\d+)/delete/$', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        path('applications/(?P<pk>\d+)/update/$', oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]

    # OAuth2 Token Management endpoints
    oauth2_endpoint_views += [
        path('authorized-tokens/$', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
        path('authorized-tokens/(?P<pk>\d+)/delete/$', oauth2_views.AuthorizedTokenDeleteView.as_view(), name="authorized-token-delete"),
    ]

    import debug_toolbar
    urlpatterns.append(path('%s__debug__/' % settings.URL_PATH_PREFIX, include(debug_toolbar.urls)))

