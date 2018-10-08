from django.urls import path, include
from rest_framework import routers
from .services_v1 import UserMyAtributesView

# router = routers.DefaultRouter()
# router.register('attributes', UserMyAtributesView, base_name='me')

urlpatterns = [
    path('api/v1/', 
         include([
             path('me/', UserMyAtributesView.as_view())
         ])
    )
]
