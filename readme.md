# SUAP SSO - Sistema de autenticação unificado



## Objetivo

Desenvolver e implantar um sistema de autenticação unificado que utilize a base do SUAP e do AD para as aplicações Web e Mobile Android.



## Justificativa

Atualmente os usuários do EaD necessitam acessar vários serviços na web, para cada serviço é solicitado ao usuário que informe o IFRN-Id e a senha causando uma verdadeira proliferação de aplicativos que coletam e validam a senha. Este problema tente a aumentar pois estamos desenvolvendo uma série de aplicativos mobile (Android e iPhone).

Para se ter uma ideia de serviços ofertados via web ou mobile que os usuários do EaD consumem ou consumirão veja a Lista 1:

*Lista 1 - Serviços em uso ou a serem utilizados pelos usuários do Campus EaD*
1. Webmail – Web
2. Moodle acadêmico – Web
3. Moodle presencial – Web
4. Administração do portal do IFRN – Web
5. Administração do portal do EaD – Web
6. Administração do portal do Colóquio – Web
7. Administração do portal do SEMEAD – Web
8. Central de chamados do Natal Central – Web
9. Central de chamados do EaD – Web
10. Portal do Office – Web
11. Microsoft Imagine – Web
12. TI – Web
13. SUAP – WEB e Android
14. Ingresso – Web
15. Processo Seletivo – Web
16. Mensageiro instantâneo – Web, Android e iPhone
17. Administração do portal cadastro em eventos – Web
18. Mural eletrônico – Web
19. Cadastro de prestadores de serviço – Android, em construção
20. Sistema de pré-matrícula online – Web, em construção
21. Sistema de solicitação à secretaria acadêmica – Web, em construção



## Proposta

Desenvolver e implementar um Web Single Sign-On (W-SSO) e um Android Mobile Authenticator (AMA) para ser utilizado pelas aplicações cadastradas.

*Lista 2 -  Protocolos preferenciais*
1.	CAS
2.	OpenID
3.	SAML 1 e SAML2
4.	**OAuth2**
5.	JWT


*Lista 3 - Implementações possíveis*
1. WSO2 Identity Server
2. CAS - django-cas-server - https://github.com/nitmir/django-cas-server
3. Django OAuth Toolkit
4. django-saml-service-provider
5. django-saml2-auth
6. django-oidc-provider

*Lista 4 - Implementações descartadas*
1. CAS - https://github.com/KTHse/django-cas2 - 5 anos sem suporte em 2017/12/15
2. CAS - https://github.com/castlabs/django-cas - 6 anos sem suporte em 2017/12/15




### Requisitos

1.	O W-SSO deverá implementar ao menos o padrão OAuth2.
2.	O W-SSO deverá realizar o Web Single Log-Out (W-SLO) da sessão.
3.	O W-SSO opcionalmente implementará todos os serviços da Lista 2, em que utilizará o compartilhamento da sessão.
4.	Deverá permitir autenticação de serviços utilizando tokens de autenticação.
5.	Deverá permitir a invalidação de token e da sessão associada a este token.
6.	Deverá permitir a gestão do perfil do usuário.
7.	Deverá permitir que o usuário tenha mais de uma função institucional atribuída a sua identidade e que cada um esteja associado a uma UOrg., com período de início e fim devidamente definidos.
8.	Poderá usar como opções de W-SSO as implementações da lista Lista 3.


## Sobre a implementação

1. É necessário usar HTTPS, para tanto, podemos usar o NGINX ou uma implementação puramente em Django, para a 
implementaçãom em Django vamos testar http://www.marinamele.com/2014/09/security-on-django-app-https-everywhere.html
2. Usarei, sempre que possível, o Moodle como cliente de teste
