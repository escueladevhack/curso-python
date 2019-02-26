from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models

from blog_project import conf

class Lista(TemplateView):
    template_name = "lista.html"

    def get_context_data(self, **kwargs):
        context = super(Lista, self).get_context_data(**kwargs)
        context['posts'] = models.Post.objects.all()
        context['nombre'] = "Mauricio"
        
        context['detalle_url'] = conf.DETALLE_POST_URL_NAME
        context['crear_url'] = conf.CREAR_POST_URL_NAME

        return context


class Crear(CreateView):
    model = models.Post
    fields = (
        'title',
    )
    success_url = reverse_lazy("listar_post")
    template_name = "crear.html"
    
    def get_context_data(self, **kwargs):
        context = super(Crear, self).get_context_data(**kwargs)

        context['nombre'] = "Mauricio"

        return context


class Detalle(DetailView):
    model = models.Post
    context_object_name = "post"
    template_name = "detalle.html"
    
    
    def get_context_data(self, **kwargs):
        context = super(Detalle, self).get_context_data(**kwargs)

        context['nombre'] = "Mauricio"
        
        context['actualizar_url'] = conf.ACTUALIZAR_POST_URL_NAME
        context['eliminar_url'] = conf.ELIMINAR_POST_URL_NAME

        return context


class Actualizar(UpdateView):
    model = models.Post
    fields = (
        'title',
        'body'
    )
    context_object_name = "post"
    
    template_name = "actualizar.html"
    
    def get_success_url(self):
        return reverse_lazy(
            conf.DETALLE_POST_URL_NAME, 
            kwargs={
                "pk": self.object.id
            }
        )
        
        
class Eliminar(DeleteView):
    model = models.Post
    template_name = "eliminar.html"
    context_object_name = "post"
    success_url = reverse_lazy(conf.LISTAR_POST_URL_NAME)
