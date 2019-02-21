from flask import Flask, request
import json

app = Flask(__name__)


archivo = "tareas.json"


@app.route("/", methods=["GET"])
def listar_todas():
    tareas = json.load(open(archivo))
    return "\n".join([json.dumps(tarea) for tarea in tareas])


@app.route("/", methods=["POST"])
def crear():
    tareas = json.load(open(archivo))
    tarea = dict(request.form)
    tareas.append(tarea)
    json.dump(tareas, open(archivo, "w+"))
    return json.dumps(tarea)


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
