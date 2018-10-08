from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuario
from .serializers_v1 import UsuarioSerializer


class UserMyAtributesView(APIView):

    def get(self, request, format=None):
        user = get_object_or_404(Usuario, pk=request.user.pk)
        serializer = UsuarioSerializer(user)
        return Response(serializer.data)
