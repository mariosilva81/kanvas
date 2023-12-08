from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView
from .models import Account
from .serializers import AccountSerializer
from rest_framework.request import Request


class AccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @extend_schema(
        description="Rota para criação de usuários",
        tags=["Criação de usuários"],
        parameters=[AccountSerializer],
    )
    def post(self, request: Request):
        return self.create(request)


@extend_schema(
    description="Rota para autenticação e obtenção de tokens de acesso",
    tags=["Autenticação"],
    request=TokenObtainPairSerializer,
    responses={200: TokenObtainPairSerializer, 400: "Bad Request"},
)
class LoginView(TokenObtainPairView):
    ...
