from django.http import HttpResponse
from .models import Input
from django.template import loader


def index(request):
    input = Input.objects.all()
    template = loader.get_template('index.html')
    context = {
        'input': input,
    }
    return HttpResponse(template.render(context, request))
