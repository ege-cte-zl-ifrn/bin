from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# @login_required
def perfil_index(request):
    return render(request, template_name='ege_perfil/perfil_index.html', context={'login_url': settings.LOGIN_URL})

