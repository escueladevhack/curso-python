# Blog flask

Instalar las dependencias

```bash
conda install flask-sqlalchemy
```

Crear un archivo que maneje una única instancia de la base de datos
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

Crear un archivo de modelos *models.py*
```python
from datetime import datetime

from .database import db

class Post(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    title = db.Column(
        db.String(80),
        nullable=False
    )
    body = db.Column(
        db.Text,
        nullable=False
    )
    pub_date = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    def __str__(self):
        return "{}".format(self.title)
```

La aplicación debe ejecutarse desde la carpeta padre del proyecto
Para ejecutar la aplicación
```bash
FLASK_RUN_PORT=8000 FLASK_DEBUG=1 FLASK_APP=blog_flask flask run
```

Para usuarios windows
```bash
set FLASK_RUN_PORT=8000 
set FLASK_DEBUG=1 
set FLASK_APP=blog_flask
flask run
```

Para crear posts

```python
# Importe los paquetes necesarios
from blog_flask import (
    app as blog_app,
    models as blog_models,
    database as blog_database
)
# Cree una aplicación
app = blog_app.create_app()
# Indique a la base de datos que contexto va a usar
app.app_context().push()
# Cree su objeto post
p1 = blog_models.Post()
p1.id = 1
p1.title = "Hello world"
p1.body = "lorem ipsum"
# Esto es simplemente un alias para el objeto SQLAlchemy
db = blog_database.db
# Introduzca los cambios a la zona de stagging
db.session.add(p1)
# Ejecute la transacción de todo lo que está en zona de stagging
db.session.commit()

# Para obtener todos los posts
all_posts = blog_models.Post.query.all()


# Para obtener un post en particular

post1 = blog_models.Post.query.filter_by(id=10).first()

# Para eliminar algún post en particular
blog_models.Post.query.filter_by(id=10).delete()
db.session.commit()

```
