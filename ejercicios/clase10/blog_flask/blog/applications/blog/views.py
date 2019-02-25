from flask.views import View
from flask.templating import render_template
from flask.helpers import url_for, request, flash
from flask.globals import g
from werkzeug.utils import redirect

from . import (
    conf,
    models
)

class List(View):

    def dispatch_request(self):
        context = dict()
        context["posts"] = models.Post.query.all()
        return render_template('list.html', **context)



class Create(View):
    methods = ["GET", "POST"]
    def dispatch_request(self):
        if request.method == 'POST':
            title = request.form['title']
            body = request.form['body']
            error = None

            if not title:
                error = 'Title is required.'

            if error is not None:
                flash(error)
            else:
                post = models.Post(
                    title=title,
                    body=body
                )
                models.db.session.add(post)
                models.db.session.commit()
                return redirect(
                    url_for(
                        conf.get_prefixed_url(conf.BLOG_LIST_URL_NAME)
                    )
                )
        return render_template('create.html')


class Detail(View):
    def dispatch_request(self, post_id):
        context = dict()
        context["post"] = models.Post.query.filter_by(id=post_id).first_or_404()
        print(context)

        return render_template('detail.html', **context)


class Update(View):
    methods = ["GET", "POST"]
    def dispatch_request(self, post_id):
        context = dict()
        context["post"] = models.Post.query.filter_by(id=post_id).first_or_404()
        print(context)
        if request.method == 'POST':
            title = request.form['title']
            body = request.form['body']
            error = None

            if not title:
                error = 'Title is required.'

            if error is not None:
                flash(error)
            else:
                post = context["post"]
                post.title = title
                post.body = body
                models.db.session.commit()
                return redirect(
                    url_for(
                        conf.get_prefixed_url(conf.BLOG_DETAIL_URL_NAME),
                        post_id=post.id
                    )
                )
        return render_template('update.html', **context)


class Delete(View):
    def dispatch_request(self, post_id):
        models.Post.query.filter_by(id=post_id).delete()
        models.db.session.commit()
        return redirect(
            url_for(
                conf.get_prefixed_url(conf.BLOG_LIST_URL_NAME)
            )
        )