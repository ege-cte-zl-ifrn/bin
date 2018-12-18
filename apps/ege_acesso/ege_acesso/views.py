import datetime
import urllib
import jwt
import json
import uuid
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views import View
from .models import Aplicacao, TransationToken


def _validate_client_id(client_id):
    try:
        return Aplicacao.objects.get(client_id=client_id, excluido_em__isnull=True)
    except Exception as e:
        raise Exception("Invalid client ID")


def _validate_state(request):
    assert 'state' in request.GET
    return request.GET['state']


def _validate_referer(request, aplicacao):
    # TODO validar se o referer está em urls_origem_permitidas
    request
    aplicacao.urls_origem_permitidas


def _validate_redirect_uri(request, aplicacao):
    assert 'redirect_uri' in request.GET
    # TODO validar se o redirect_uri está em urls_origem_permitidas
    redirect_uri = urllib.parse.unquote_plus(request.GET['redirect_uri'])
    aplicacao
    return redirect_uri


def _generate_auth_token(request, aplicacao, state, redirect_uri):
    hashcode = "%s" % uuid.uuid1()
    tt = TransationToken.objects.create(aplicacao=aplicacao,
                                        usuario=request.user,
                                        hashcode=hashcode,
                                        state=state,
                                        redirect_uri=redirect_uri,
                                        referer="",
                                        expiracao=datetime.datetime.now() + datetime.timedelta(minutes=10))
    return hashcode


def _validate_auth_token(request, aplicacao):
    assert 'auth_token' in request.GET
    auth_token = request.GET['auth_token']
    # state = request.POST['state']
    tolerance = datetime.datetime.now() - datetime.timedelta(minutes=10)
    transaction_token = TransationToken.objects.get(aplicacao=aplicacao,
                                                    hashcode=auth_token,
                                                    # state=state,
                                                    expiracao__gt=tolerance)
    transaction_token.aplicacao
    # transaction_token.delete()
    return transaction_token


def _generate_jwt(transaction_token):
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
        'created_at': "%s" % user.created_at,
        'changed_at': "%s" % user.changed_at,
        'password_set_at': "%s" % user.password_set_at,
        'last_access_at': "%s" % user.last_access,
        'last_ad_access_at': "%s" % user.last_ad_access_at,
        'date_joined_at': "%s" % user.date_joined,
        'first_access_at': "%s" % user.first_access_at,
    }
    return jwt.encode(data, transaction_token.aplicacao.segredo, algorithm='HS512')


def index_view(request):
    return HttpResponse("Acho que você deseja acessar teu perfil, então clique")


@login_required
def authorize_view(request):
    assert 'client_id' in request.GET, "empty client_id on get"
    aplicacao = _validate_client_id(request.GET['client_id'])
    state = _validate_state(request)
    redirect_uri = _validate_redirect_uri(request, aplicacao)
    auth_token = _generate_auth_token(request, aplicacao, state, redirect_uri)
    # return HttpResponse(json.dumps({'aplicacao': aplicacao.id, 'state': state, 'redirect_uri': redirect_uri, 'auth_token': auth_token, }))
    return redirect("%s&auth_token=%s" % (redirect_uri, auth_token))


@csrf_exempt
def validate_view(request):
    assert 'client_id' in request.GET, "empty client_id on post"
    aplicacao = _validate_client_id(request.GET['client_id'])
    transaction_token = _validate_auth_token(request, aplicacao)
    return HttpResponse(_generate_jwt(transaction_token))
