from social.backends.oauth import BaseOAuth2
# from comum.models.base import UserProfile


class SabiaOAuth2(BaseOAuth2):
    name = 'ifrnid'
    AUTHORIZATION_URL = 'http://localhost/id/acesso/oauth/authorize/'
    ACCESS_TOKEN_METHOD = 'POST'
    ACCESS_TOKEN_URL = 'http://sso:8000/id/acesso/oauth/token/'
    ID_KEY = 'cpf'
    RESPONSE_TYPE = 'code'
    REDIRECT_STATE = True
    STATE_PARAMETER = True
    USER_DATA_URL = 'https://login.sabia.ufrn.br/api/perfil/dados/'

    # def user_data(self, access_token, *args, **kwargs):
    #     print("user_data(%s, %s, %s)" % (access_token, args, kwargs))
    #     return self.request(
    #         url=self.USER_DATA_URL,
    #         data={'scope': kwargs['response']['scope']},
    #         method='POST',
    #         headers={'Authorization': 'Bearer {0}'.format(access_token)}
    #     ).json()

    # def get_user_details(self, response):
    #     """
    #     Retorna um dicionário mapeando os fields do settings.AUTH_USER_MODEL.
    #     você pode fazer aqui outras coisas, como salvar os dados do usuário
    #     (`response`) em algum outro model.
    #     """
    #     print(response)
    #     splitted_name = response['name'].split()
    #     first_name, last_name = splitted_name[0], ''
    #     if len(splitted_name) > 1:
    #         last_name = splitted_name[-1]
    #     return {
    #         'username': response['cpf'],
    #         'first_name': first_name.strip(),
    #         'last_name': last_name.strip(),
    #         'email': response['email'],
    #     }

    # def extra_data(self, user, uid, response, details=None, *args, **kwargs):
    #     if not UserProfile.objects.filter(user__pk=user.pk).exists():
    #         # Criando o profile básico do Usuário.
    #         user_profile = UserProfile()
    #         user_profile.nome = response['name']
    #         user_profile.cpf = response['cpf']
    #         user_profile.email = response['email']
    #         user_profile.user = user
    #         user_profile.is_recem_criado = True
    #         user_profile.save()
    #     return super(SabiaOAuth2, self).extra_data(user, uid, response, details, *args, **kwargs)