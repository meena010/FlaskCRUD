from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = "app"

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:''@localhost/empdb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

@app.route('/')
def index():
    return render_template("index.html")


db = SQLAlchemy(app)
app.app_context().push()


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
