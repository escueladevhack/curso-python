Title: Funciones
Author: Mauricio Collazos
Date: 2019-02-04
![]()
---
class: center, middle, light, first-slide
# Funciones
## Mauricio Collazos
.footnote[]
---
class: light
# Definición básica
```python
def nombre_de_funcion(parametro1, parametr2):
    sentencias
```

---
# Documentación de funciones

```python
def nombre_de_funcion(parametro1, parametr2):
    """Esta función hace algo en específico"""
    sentencias
```

---
# Paso por valor vs paso por referencia
```python
def agregar(a):
    """Esta función agrega 1 a un número"""
    a = a+1
    return a


b = 1
print(agregar1(b))
print(b)
```

```python
def pegar(a):
    """Esta función agrega un elemento 1 a una lista"""
    a.append(1)
    print(a)
    return  a
    
b = [1,2,3]
print(pegar(b))
print(b)
```
---
# Argumentos nombrados
```python
def sumar(a, b=1):
    """Esta función agrega 1 o un valor b"""
    return  a + b


print(sumar(1))
print(sumar(1, b=5))
```

---
# Múltiples argumentos
```python
def agregar(a, *args):
    """Esta función agrega valores a la lista a"""
    return  a.extend(args)


a = [1,2,3,4]
agregar(a, 5,6,7,8)
print(a)
```
---
# Múltiples argumentos nombrados
```python
def agregar(**kwargs):
    """Esta muestra los múltiples argumentos nombrados"""
    print(kwargs)


agregar(a=1, b=2, c=3)
```
--- 
# Ejercicios
- Cree una función que lea una números hasta que se digite el 0
