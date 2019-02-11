Title: Patrones de Diseño
Author: Mauricio Collazos
Date: 2019-02-11
![]()
---
class: center, middle, light, first-slide
# Patrones de diseño
## Mauricio Collazos
.footnote[]
---
[Code Reviews and why are we wrong about it](https://speakerdeck.com/asendecka/code-review-and-why-are-we-wrong-about-it-and-how-to-use-it-to-our-advantage)
---
class: light
# Definición básica

Los patrones de diseño son herramientas abstractas para resolver problemas de una manera clara y eficiente.

[Design Patterns: Elements of reusable object oriented software](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612)
 
---
# Revisión rápida a algunas deficiniones

[Design Patterns](https://sourcemaking.com/design_patterns) By [Source Making](https://sourcemaking.com/) 
---
# Restricción de acceso

```python
class Usuario:
    _metodos_expuestos = ['obtener', 'guardar', 'eliminar']

    def __getattr__(self, atributo):
        if atributo in self._metodos_expuestos:
            return getattr(self, atributo)
```

---
# Cadena de responsabilidad
```python
class CadenaDeValidaciones(object):
    def __init__(self, validadores=None):
        self._validadores = list()
        if validadores is not None:
            self._validadores += validadores

    def es_valida(self, contrasena):
        for validador in self._validadores:
            if not validador(contrasena):
                return False  
        return True

filtro_contrasenas = CadenaDeValidaciones([
                filtro_mayusculas,
                filtro_numeros,
                filtro_especiales])
contrasena_validada = filtro_contrasenas.es_valida(contrasena)
```

---
# Comando
```python
class Renombrar(object):
    def __init__(self, de, a):
        self._de = de
        self._a = a

    def ejecutar(self):
        os.rename(self._de, self._a)

    def deshacer(self):
        os.rename(self._a, self._de)

class Historial(object):
    def __init__(self):
        self._comandos = list()

    def ejecutar(self, comando):
        self._comandos.append(comando)
        comando.execute()

    def deshacer(self):
        self._comandos.pop().deshacer()

historial = Historial()
historial.ejecutar(Renombrar('archivo1.txt', 'archivo2.txt'))
historial.ejecutar(Renombrar('archivo2.txt', 'archivo4.txt'))
historial.deshacer()
historial.deshacer()
```
---
# Singleton
```python
class Logger(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            cls._logger = super(Logger, cls
                    ).__new__(cls, *args, **kwargs)
        return cls._logger
```
---
# Inyección de dependencias
```python
class Comando:

    def __init__(self, autenticar=None, autorizar=None):
        self.autenticar = autenticar or self._no_autenticado
        self.autorizar = autorizar or self._no_autorizado

    def ejecutar(self, usuario, accion):
        self.autenticar(usuario)
        self.autorizar(usuario, accion)
        return action()

if es_super_usuario:
    comando = Comando(siempre_autenticado, siempre_autorizado)
else:
    comando = Comando(config.autenticado, config.autorizado)
comando.ejecutar(usuario, eliminar)
```
---
# Fachada
```python
class Carro(object):

    def __init__(self):
        self._neumaticos = [
            Neumatico('front_left'),
            Neumatico('front_right'),
            Neumatico('rear_left'),
            Neumatico('rear_right'), 
        ]
        self._tanque = Tanque(70)

    def presion_de_neumaticos(self):
        return [neumatico.presion for neumatico in self._neumaticos]

    def nivel_de_gasolina(self):
        return self._tanque.nivel
```
---
# Adaptador
```python
def log(message, destination):
    destination.write('[{}] - {}'.format(datetime.now(), message))
```


---
# Decorador
```python
def esta_autenticado(metodo):
    def decorador(*args, **kwargs):
        if verificar_autenticacion(kwargs['user']):
            return metodo(*args, **kwargs )
        else:
            raise UsuarioNoAutenticado
    return decorador
    
@esta_autenticado
def ejecutar(accion, *args, **kwargs):
    return accion()
```

---
# Ejercicios
- Implementar un programa completo que use un validador de contraseñas
- Implementar un programa completo que permita renombrar  y eliminar archivos
- Implemente un programa que dependiendo las preferencias de un usuario muestre la temperatura en Celsius o Farengheit
- Implemente un sistema de autenticación con restricciones por permisos