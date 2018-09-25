from django.http import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')


@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)


@login_required()
def perfil_index(request, *args, **kwargs):
    context = {"perfil": "soy yo"}
    return render(request, 'suapsso/perfil_index.html', context)
