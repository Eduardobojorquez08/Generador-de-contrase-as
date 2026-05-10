from flask import Flask, render_template, request, jsonify
from generador import crear_contraseña
from verificador import verificar_contraseña

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/generar")
def generar():
    longitud = int(request.args.get("longitud"))
    contraseña = crear_contraseña(longitud)
    return jsonify({"contraseña": contraseña})


@app.route("/verificar")
def verificar():
    verificacion = request.args.get("contraseña")
    contraseña_usuario = verificar_contraseña(verificacion)
    return jsonify({"verificacion": contraseña_usuario})

if __name__ == "__main__":
    app.run(debug=True)
