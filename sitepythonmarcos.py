from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/contatos")
def contact():
    return render_template("contact.html")

@app.route("/users/<name_user>")
def users(name_user):
    return render_template("users.html", name_user=name_user)

if __name__ == "__main__":
    app.run(debug=True)
