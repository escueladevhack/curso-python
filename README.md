# Curso de backend con Python

Curso rápido de [Python](https://python.org/) para [DevHack](https://www.devhack.co/)
En este repositorio encontrará:

- [content](content): Todo el contenido del curso: presentaciones y artículos
- [ejercicios](ejercicios): Código en Python correspondiente a cada clase
- [output](output): Una versión compilada de la página del curso
- [project](project): Referencias a repositorios con código de los proyectos realizados en este curso
- [themes](themes): Tema de Pelican para construir el sitio estático

Este sitio fue construido usando [Pelican](https://blog.getpelican.com/)

Para configurar el ambiente de desarrollo

```bash
# Create an environment
conda create --name curso_rapido_python
# Activate the environment
source activate curso_rapido_python
# Install pelican dependencies
conda install -c conda-forge pelican markdown livereload
```


Para ejecutar local

```bash
pelican --autoreload
```

Y para verlo en el navegador

```bash
cd output
python3 -m http.server 
# Para salir cntrl + c
```


Para sincronizar

```bash
cd output
aws s3 sync . s3://curso-rapido-python.contraslash.com
```


Referencias proyecto

-[](https://towardsdatascience.com/pandas-tips-and-tricks-33bcc8a40bb9)