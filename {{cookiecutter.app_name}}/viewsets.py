from rest_framework import viewsets

from .models import {{cookiecutter.model_name}}


class {{cookiecutter.model_name}}ViewSet(viewsets.ModelViewSet):
    queryset = {{cookiecutter.model_name}}.objects.all()
