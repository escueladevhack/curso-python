import json
import pandas as pd
from flask import Flask, request
app = Flask(__name__)


archivo = "tareas.csv"


@app.route("/", methods=["GET"])
def listar_todas():
    tareas = pd.read_csv(archivo)
    return tareas.to_string()


@app.route("/", methods=["POST"])
def crear():
    tareas = pd.read_csv(archivo)
    tarea = pd.DataFrame(dict(request.form), index=[0])
    tareas = pd.concat([tareas,tarea])
    tareas.to_csv(archivo, columns=["id", "titulo", "descripcion"])
    return tareas.to_string(columns=["id", "titulo", "descripcion"])


@app.route("/", methods=["DELETE"])
def eliminar():
    id_tarea = request.form.get("id", None)
    tareas = json.load(open(archivo))
    tarea_eliminar = None
    for tarea in tareas:
        if id_tarea == tarea["id"]:
            tarea_eliminar = tarea
            break
    if tarea_eliminar is None:
        return "Not found", 404
    tareas.remove(tarea_eliminar)
    json.dump(tareas, open(archivo, "w+"))
    return json.dumps(tarea_eliminar)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
