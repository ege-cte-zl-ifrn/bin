from django.urls import path, include
from . import views
from .views import ApiEndpoint

urlpatterns = [
    path('', include('ege_django_theme.urls')),
    path('api/hello', ApiEndpoint.as_view()),
    path('secret', views.secret_page, name='secret_page'),
]
