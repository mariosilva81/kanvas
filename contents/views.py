from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from contents.models import Content
from contents.serializers import ContentSerializer
from courses.models import Course
from rest_framework.exceptions import NotFound
from drf_spectacular.utils import extend_schema
from accounts.permissions import IsSuperUser
from rest_framework.permissions import IsAuthenticated
from contents.permissions import IsCourseStudentOwnerOrAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.request import Request


class ContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id"

    @extend_schema(
        description="Rota para criação de conteúdo de um curso",
        tags=["Criação de conteúdo de um curso"],
        parameters=[ContentSerializer],
    )
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer: ContentSerializer) -> Content:
        found_course = get_object_or_404(Course, pk=self.kwargs["course_id"])
        serializer.save(course=found_course)


class ContentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsCourseStudentOwnerOrAdmin]
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    lookup_url_kwarg = "content_id"

    def get_object(self):
        try:
            Course.objects.get(id=self.kwargs["course_id"])
            content = Content.objects.get(id=self.kwargs["content_id"])
        except Content.DoesNotExist:
            raise NotFound({"detail": "content not found."})
        except Course.DoesNotExist:
            raise NotFound({"detail": "course not found."})
        self.check_object_permissions(self.request, content)
        return content

    @extend_schema(
        description="Rota para listagem de conteúdo de um curso por ID",
        tags=["Listagem, edição e exclusão de conteúdo de um curso"],
    )
    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        description="Rota para edição de conteúdo de um curso por ID",
        tags=["Listagem, edição e exclusão de conteúdo de um curso"],
    )
    def patch(self, request: Request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        description="Rota para exclusão de conteúdo de um curso por ID",
        tags=["Listagem, edição e exclusão de conteúdo de um curso"],
    )
    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
