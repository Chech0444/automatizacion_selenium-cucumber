from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret123"

USERS = {"admin": "1234", "user": "pass"}

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in USERS and USERS[username] == password:
            return redirect(url_for("dashboard", username=username))
        else:
            flash("Credenciales invalidas", "error")
    return render_template("login.html")

@app.route("/dashboard/<username>")
def dashboard(username):
    return f"<h1>Bienvenido {username}!</h1><a href='/login'>Salir</a>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
