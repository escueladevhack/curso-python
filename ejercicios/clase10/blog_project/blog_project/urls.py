"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from blog import views
from . import conf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Lista.as_view(), name=conf.LISTAR_POST_URL_NAME),
    path('crear', views.Crear.as_view(), name=conf.CREAR_POST_URL_NAME),
    path('<int:pk>/detalle', views.Detalle.as_view(), name=conf.DETALLE_POST_URL_NAME),
    path('<int:pk>/actualizar', views.Actualizar.as_view(), name=conf.ACTUALIZAR_POST_URL_NAME),
    path('<int:pk>/eliminar', views.Eliminar.as_view(), name=conf.ELIMINAR_POST_URL_NAME),
    path(
        'ingresar',
        LoginView.as_view(
            template_name="login.html",
            form_class=AuthenticationForm
        )
    )
]

from django.contrib.auth.mixins import LoginRequiredMixin

# settings.py
LOGIN_URL = "ingresar"
from django import http

def  form_valid(self, form):
    twit = form.save(commit=False)
    twit.user = self.request.user
    return http.HttpResponseRedirect(self.success_url)
