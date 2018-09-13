from django.urls import path
from . import views
from .views import ApiEndpoint

urlpatterns = [
    path('', views.index, name='index'),
    path('api/hello', ApiEndpoint.as_view()),
    path('secret', views.secret_page, name='secret_page'),
]
