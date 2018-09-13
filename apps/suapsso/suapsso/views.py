from django.http import HttpResponse
from .models import Input
from django.template import loader
from oauth2_provider.views.generic import ProtectedResourceView
from django.contrib.auth.decorators import login_required


def index(request):
    input = Input.objects.all()
    template = loader.get_template('index.html')
    context = {
        'input': input,
    }
    return HttpResponse(template.render(context, request))


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')


@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)
