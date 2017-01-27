from django.conf.urls import include, url
from rest_framework import routers

from . import viewsets

app_name = '{{cookiecutter.app_name}}'


router = routers.SimpleRouter()
router.register(r'{{cookiecutter.model_name|lower}}', viewsets.{{cookiecutter.model_name}}ViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
