from flask import Flask
from flask.helpers import url_for, request
from flask.templating import render_template
from werkzeug.utils import redirect

from database import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    print("Initializing DB")
    db.init_app(app)
    from models import Post
    with app.test_request_context():
        db.create_all()
    print("DB Initialized successfully")

    @app.route("/", methods=["GET"])
    def lista():
        context = dict()
        context["posts"] = Post.query.all()
        return render_template('lista.html', **context)

    @app.route("/crear", methods=["GET", "POST"])
    def crear():
        if request.method == 'POST':
            title = request.form['title']
            body = request.form['body']

            post = Post(
                title=title,
                body=body
            )
            db.session.add(post)
            db.session.commit()
            return redirect("")
        return render_template('crear.html')

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000, debug=True)
