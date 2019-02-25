from flask import Flask

from .database import db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    from .applications.blog import bp as blog_bp
    app.register_blueprint(blog_bp)

    print("Initializing DB")
    db.init_app(app)
    with app.test_request_context():
        db.create_all()
    print("DB Initialized successfully")

    return app