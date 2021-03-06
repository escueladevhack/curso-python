Title: Clases
Author: Mauricio Collazos
Date: 2019-02-06
![]()
---
class: center, middle, light, first-slide
# Clases
## Mauricio Collazos
.footnote[]
---
class: light
# Definición básica
```python
class NombreDeClase(ClasePadre, ClaseMadre):
    cuerpo
```

---
# Constructores

```python
class Nombre de clases(ClasePadre, ClaseMadre):
    def __init__(self):
        sentencias
```

---
# Atributos
```python
class Nombre de clases(ClasePadre, ClaseMadre):
    atributo_publico = 0
    _atributo_privado = 0
```

---
# Propiedades
```python
class Nombre de clases(ClasePadre, ClaseMadre):
    @property
    def atributo(self):
        return self._atributo


    @atributo.setter
    def atributo(self, value):
        self._atributo = value


    @atributo.deleter
    def atributo(self):
        del self._atributo
```
---
# Métodos de clase y estáticos
```python
class Nombre de clases(ClasePadre, ClaseMadre):
    @classmethod
    def metodo_de_clase(cls):
        sentencias
        
    @staticmethod
    def metodo_estatico():
        sentencias
```
---
# Herencia
```python
class FiguraGeometrica(object):
    def perímetro(self):
        raise NotImplementedError("Método no implementado")
        
    def area(self):
        raise NotImplementedError("Método no implementado")
    
    
class Cuadrado(FiguraGeometrica):
    pass
```
## Ejercicios
- Cree la clase rectángulo
- Cree la clase cuadrado
- Cree la clase triángulo
- Cree la clase círculo

---
# Ejercicios
- Diseñe un esquema de herencia para animales mamíferos
  - Implemente clases concretas para un perro y un delfín
- Implemente una clase que transforme números romanos a arábigos y viceversa
- Diseñe un modelo orientado a objetos que simule el tiempo de espera promedio de una persona haciendo fila en un banco
  - asuma que el tiempo de atención de un cajero es de 5 a 10 minutos
  - las personas llegan aleatoreamente entre cada 3 y 6 minutos
  - plantee escenarios con 1, 2 y 3 cajeros