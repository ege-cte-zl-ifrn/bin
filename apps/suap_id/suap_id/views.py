from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# @login_required
def perfil_index(request):
    return render(request, template_name='suap_id/perfil_index.html')

