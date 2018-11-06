from oauth2_provider.oauth2_backends import OAuthLibCore


class SuapSsoOAuthLib(OAuthLibCore):
    
     def _get_extra_credentials(self, request):
        """
        Produce extra credentials for token response. This dictionary will be
        merged with the response.
        See also: `oauthlib.oauth2.rfc6749.TokenEndpoint.create_token_response`
        :param request: The current django.http.HttpRequest object
        :return: dictionary of extra credentials or None (default)
        """
        return {
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }

