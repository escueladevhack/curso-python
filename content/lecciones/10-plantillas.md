Title: Plantillas
Author: Mauricio Collazos
Date: 2019-2-25
![]()
---
class: center, middle, light, first-slide
# Plantillas
## Mauricio Collazos
.footnote[]
---
# Plantillas
- string.Template
- Mako
- Jinja2
- Django Templates
---
# Descubrimiento de plantillas
- Plantillas en raiz de proyecto
- Plantillas por aplicación
---
# Interpolación

Interpolación
```html
Hola {{ nombre }}
```

---
# Operaciones Condicionales

```html
{% if variable %}
    Verdadero
{% else %}
    False
{% endif %}
```
---

# Operaciones Iterativas
```
{% for color in colores %}
    {{ color }}
{% endfor %}
```
---
# Extensibilidad
Base HTML
```html
<body>
    <section class="content">
      <header>
        {% block header %}

        {% endblock %}
      </header>
      {% block content %}

      {% endblock %}
    </section>
</body>

```

---

Lista html
```html
{% extends 'base.html' %}

{% block header %}
  <h1>Posts</h1>
{% endblock %}

{% block content %}
    {% for post in posts %}
    <article class="post">
      <header>
        <div >
          <h1>
              <a href="{{ url_for('blog.blog_detail', post_id=post.id) }}">
                  {{ post['title'] }}
              </a>
          </h1>
        </div>
      </header>
      <p class="body">{{ post.body }}</p>
    </article>

 {% endfor %}
{% endblock %}
```

---
