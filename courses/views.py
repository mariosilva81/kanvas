from .models import Course
from .serializers import CourseSerializer
from accounts.permissions import IsAdminOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.request import Request


class CourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    serializer_class = CourseSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Course.objects.all()
        return Course.objects.filter(students=self.request.user.id)

    def perform_create(self, serializer: CourseSerializer) -> Course:
        if "instructor" in serializer.validated_data:
            serializer.save(instructor=serializer.validated_data["instructor"])
        else:
            serializer.save()

    @extend_schema(
        description="Rota para listagem de cursos",
        tags=["Criação e listagem de cursos"],
    )
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        description="Rota para criação de um curso",
        tags=["Criação e listagem de cursos"],
        parameters=[CourseSerializer],
    )
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CourseDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Course.objects.all()
        return Course.objects.filter(students=self.request.user.id)

    @extend_schema(
        description="Rota para listagem de um curso por ID",
        tags=["Listagem, edição e exclusão de curso"],
    )
    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        description="Rota para edição de um curso por ID",
        tags=["Listagem, edição e exclusão de curso"],
    )
    def patch(self, request: Request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()

    @extend_schema(
        description="Rota para exclusão de um curso por ID",
        tags=["Listagem, edição e exclusão de curso"],
    )
    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
