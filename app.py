from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def home():
    return "Sin estilos"

@app.route("/bonito")
def bonito():
    return render_template("index.html")
    