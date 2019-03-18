Title: MatPlotLib
Author: Mauricio Collazos
Date: 2019-02-27
![]()
---
class: center, middle, light, first-slide
# MatPlotLib
## Mauricio Collazos
.footnote[]
---
# Una primera figura

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show()
```

---
# Usando otro tipo de líneas

```python
fig = plt.figure()
ax = plt.axes()
ax.plot(x, np.sin(x), "--");
```

```python
fig = plt.figure()
ax = plt.axes()
ax.plot(x, np.sin(x), "o");
```

---
# Gráfico de puntos
```python
fig = plt.figure()
ax = plt.axes()
ax.scatter(x, np.sin(x));
```

---
# Histogramas

```python
plt.style.use('seaborn-white')

data = np.random.randn(1000)
plt.hist(data);
```

---
# Nombrando las gráficas

```python
plt.style.use('classic')
x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), '-b', label='Seno')
ax.plot(x, np.cos(x), '--r', label='Coseno')
ax.axis('equal')
leg = ax.legend();
```

---
# Gráficas en 3d

```python
from mpl_toolkits import mplot3d
fig = plt.figure()
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
```

---
# Gráficas más complejas
```python
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
```

---
# Seaborn

```python
import seaborn as sns
import pandas as pd

df = pd.DataFrame()

df['x'] = np.random.randn(1000)
df['y'] = np.random.randn(1000)

sns.lmplot('x', 'y', data=df, fit_reg=False)

```

---
# Usando un dataset
```python
tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=tips);
```

```python
sns.catplot(x="day", y="total_bill", hue="sex", kind="swarm", data=tips);
```

```python
sns.catplot(x="day", y="total_bill", kind="box", data=tips);
```

---
# Mas alternativas de visualización
- [Bokeh](https://bokeh.pydata.org/en/latest/)
- [Plotly](https://plot.ly/)
- [Vispy](http://vispy.org/)
- [Vega](https://vega.github.io/)

---
# Complementar contenido con
https://www.kaggle.com/neilslab/seaborn-visualization
https://realpython.com/python-data-visualization-bokeh/