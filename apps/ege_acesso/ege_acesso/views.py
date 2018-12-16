import datetime
import urllib
import jwt
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.generic import View
from .models import Aplicacao, TransationToken


class ValidateClientIdView(View):
    def _validate_client_id(self, client_id):
        try:
            return Aplicacao.objects.get(client_id=client_id, excluido_em__is_null=True)
        except Exception as e:
            raise Exception("Invalid client ID")


class AuthorizeView(ValidateClientIdView):

    def _validate_state(self, request):
        assert 'state' in request.GET
        return request.GET['state']

    def _validate_referer(self, request, aplicacao):
        # TODO validar se o referer está em urls_origem_permitidas
        request
        aplicacao.urls_origem_permitidas

    def _validate_redirect_uri(self, request, aplicacao):
        assert 'redirect_uri' in request.GET
        # TODO validar se o redirect_uri está em urls_origem_permitidas
        redirect_uri = urllib.parse.unquote_plus(request.GET['redirect_uri'])
        aplicacao
        return redirect_uri

    def _generate_auth_token(self, request, aplicacao, state, redirect_uri):
        hashcode = '2'
        TransationToken.objects.create({"aplicacao": aplicacao,
                                        "usuario": request.user,
                                        "hashcode": hashcode,
                                        "state": state,
                                        "redirect_uri": redirect_uri,
                                        "referer": "",
                                        "expiracao": datetime.datetime.now() + datetime.timedelta(minutes=10)})
        return hashcode

    @login_required
    def get(self, request):
        assert 'client_id' in request.GET
        aplicacao = self._validate_client_id(request.POST['client_id'])
        state = self._validate_state(request)
        redirect_uri = self._validate_redirect_uri(request, aplicacao)
        auth_token = self._generate_auth_token(request, aplicacao, state, redirect_uri)
        return redirect("%s&auth_token=%s" % (redirect_uri, auth_token))


class ValidateView(ValidateClientIdView):

    def _validate_auth_token(self, request, aplicacao):
        assert 'auth_token' in request.GET
        auth_token = request.POST['auth_token']
        state = request.POST['state']
        tolerance = datetime.datetime.now() - datetime.timedelta(minutes=10)
        transaction_token = TransationToken.objects.get(aplicacao=aplicacao,
                                                        auth_token=auth_token,
                                                        state=state,
                                                        expiracao__gt=tolerance)
        transaction_token.aplicacao
        transaction_token.delete()
        return transaction_token

    def _generate_jwt(self, transaction_token):
        user = transaction_token.usuario
        data = {
            'username': user.username,
            'social_name': user.social_name,
            'presentation_name': user.presentation_name,
            'department': user.department,
            'campus': user.campus,
            'is_active': user.is_active,
            'carrer': user.carrer,
            'job': user.job,
            'cpf': user.cpf,
            'academic_email': user.academic_email,
            'enterprise_email': user.enterprise_email,
            'personal_email': user.email,
            'title': user.title,
            'photo_blob': user.photo_blob,
            'created_at': user.created_at,
            'changed_at': user.changed_at,
            'password_set_at': user.password_set_at,
            'last_access_at': user.last_access,
            'last_ad_access_at': user.last_ad_access_at,
            'date_joined_at': user.date_joined,
            'first_access_at': user.first_access_at,
        }
        return jwt.encode(data, transaction_token.aplicacao.segredo, algorithm='HS512')

    @csrf_exempt
    def post(self, request):
        aplicacao = self._validate_client_id(request.POST['client_id'])
        transaction_token = self._validate_auth_token(request, aplicacao)
        return HttpResponse(self._generate_jwt(transaction_token))
