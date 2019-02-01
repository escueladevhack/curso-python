Author: Mauricio Collazos
Title: Virtualenvs Cheat Sheet
Date: 2018-10-08
---
![]()
---
class: center, middle
# Virtualenvs Cheat Sheet
## Mauricio Collazos
---
**Listar todos los ambientes**

```bash
conda env list
```
---
**Crear un ambiente**

Conda
```bash
conda create --name [nombre_del_ambiente]
```

Virtualenv
```bash
python -m venv [nombre_del_ambiente]
```

**Activar un ambiente**

Conda
```bash
# x-nix
source activate [nombre_del_ambiente]
# windows
activate [nombre_del_ambiente]
```

Virtualenv
```bash
# x-nix
source carpeta_del_ambiente/bin/activate
# windows
carpeta_del_ambiente\Scripts\activate
```
---


**Descripción del ambiente para replicas**

Conda
```bash
conda env export > environment.yml
```

Virtualenv
```bash
pip freeze > requirements.txt
```
---
**Replicar ambiente**

Conda
```bash
conda install --file environment.yml
```

Virtualenv
```bash
pip install -r requirements.txt
```


**Instalar paquete**

Conda
```bash
conda install [nombre_paquete]
```

Virtualenv
```bash
pip install [nombre_paquete]
```
