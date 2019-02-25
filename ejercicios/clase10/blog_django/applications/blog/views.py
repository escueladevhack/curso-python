from django.views import View
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404

from . import (
    models,
    conf
)

class List(View):

    def get(self, request, *args, **kwargs):
        context = dict()
        context["posts"] = models.Post.objects.all()
        return TemplateResponse(request, "list.html", context=context)

class Create(View):

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, "create.html")

    def post(self, request, *args, **kwargs):
        title = request.POST['title']
        body = request.POST['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            messages.add_message(
                request,
                messages.ERROR,
                error
            )
        else:
            post = models.Post(
                title=title,
                body=body
            )
            post.save()
            return HttpResponseRedirect(
                reverse(
                    conf.get_prefixed_url(conf.BLOG_LIST_URL_NAME)
                )
            )


class Detail(View):

    def get(self, request, *args, **kwargs):
        context = dict()
        print(kwargs)
        context["post"] = get_object_or_404(models.Post, pk=kwargs.get("post_id", ""))
        return TemplateResponse(request, "detail.html", context=context)


class Update(View):
    def get(self, request, *args, **kwargs):
        context = dict()
        context["post"] = get_object_or_404(models.Post, pk=kwargs.get("post_id", ""))
        return TemplateResponse(request, "update.html", context=context)

    def post(self, request, *args, **kwargs):
        title = request.POST['title']
        body = request.POST['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            messages.add_message(
                request,
                messages.ERROR,
                error
            )
        else:
            post = models.Post.objects.get(pk=kwargs.get("post_id", ""))
            post.title = title
            post.body = body
            post.save()
            return HttpResponseRedirect(
                reverse(
                    conf.get_prefixed_url(conf.BLOG_LIST_URL_NAME)
                )
            )


class Delete(View):
    def get(self, request, *args, **kwargs):
        context = dict()
        post = get_object_or_404(models.Post, pk=kwargs.get("post_id", ""))
        post.delete()
        return HttpResponseRedirect(
            reverse(
                conf.get_prefixed_url(conf.BLOG_LIST_URL_NAME)
            )
        )

