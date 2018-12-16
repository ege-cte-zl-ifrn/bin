import urllib
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.generic import View, TemplateView


class BaseView(View):

    def _validate_client_id(self, client_id):
        # raise Exception("Invalid client ID")s
        return None

    def get(self, request):
        return HttpResponse('result')


class IndexView(TemplateView):
    template_name = "ege_authn/index.html"


class AuthorizeView(BaseView):

    def _validate_state(self, state):
        # raise Exception("Invalid request state")
        return None

    def _validate_redirect_uri(self, client_id, redirect_uri):
        # redirect_uri = urllib.parse.unquote_plus(request.GET['redirect_uri'])
        # raise Exception("Invalid redirect_uri")
        return None

    def _generate_token(self, client):
        # redirect_uri = urllib.parse.unquote_plus(request.GET['redirect_uri'])
        # raise Exception("Invalid redirect_uri")
        return None

    @login_required
    def get(self, request):
        client = self._validate_client_id(request.GET['client_id'])
        self._validate_state(request)
        redirect_uri = self._validate_redirect_uri(request, client)
        auth_token = self._generate_token(client)
        return redirect("%s&auth_token=%s" % (redirect_uri, auth_token))


class ValidateView(BaseView):

    def _validate_auth_token(self, redirect_uri):
        # raise Exception("Invalid auth_token")
        return None

    def _generate_jwt(self, client, auth_token):
        # raise Exception("Invalid auth_token")
        return None

    @csrf_exempt
    def post(self, request):
        client = self._validate_client_id(request.POST['client_id'])
        self._validate_auth_token(request.POST['auth_token'])
        self._generate_jwt(client, request.POST['auth_token'])

        return HttpResponse("3")
