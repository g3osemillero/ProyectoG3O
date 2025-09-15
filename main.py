from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def home():
    return render_template("quienesSomos.html", title="ProyectoG3O")

@app.route("/Links")
def links():
    return render_template("LinksRelacionados.html", title = "Links Relacionados")

@app.route("/IngCatastral")
def ingCat():
    return render_template("IngCatastralyGeodesia.html", title = "Ingenieria Catastral y Geodesia")

if __name__ == "__main__":
    app.run(debug=True)