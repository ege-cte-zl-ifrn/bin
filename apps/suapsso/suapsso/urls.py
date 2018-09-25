from django.urls import path, include
from . import views
from .views import ApiEndpoint

def barra(request):
    return "oi"

urlpatterns = [
    path('api/hello', ApiEndpoint.as_view()),
    path('secret', views.secret_page, name='secret_page'),
    path('', views.perfil_index, name='suapsso__perfil_index'),
]
