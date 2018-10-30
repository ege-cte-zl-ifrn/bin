from rest_framework.serializers import ModelSerializer, CharField
from .models import Usuario


class UsuarioSerializer(ModelSerializer):

    presentation_name = CharField()

    class Meta:
        model = Usuario
        exclude = ["password", "groups", "user_permissions", "ativo"]
