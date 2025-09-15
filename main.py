from flask import Flask, render_template
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
app = Flask(
    __name__,
    static_folder=str(BASE_DIR / "static"),
    template_folder=str(BASE_DIR / "templates"),
)

@app.route("/")
def home():
    return render_template("quienesSomos.html", title="ProyectoG3O")

@app.route("/Links")
def links():
    return render_template("LinksRelacionados.html", title = "Links Relacionados")

@app.route("/IngCatastral")
def ingCat():
    return render_template("IngCatastralyGeodesia.html", title = "Ingenieria Catastral y Geodesia")

@app.route("/Contacto")
def contacto():
    return render_template("contacto.html", title = "Contacto")

if __name__ == "__main__":
    app.run(debug=True)