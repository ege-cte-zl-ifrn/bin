from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import 


class SuapLoginView(LoginView):
    def login(request):
        return render(request, template_name='suap_id/perfil_index.html')