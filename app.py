from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


# def get_db_connection():
#     return psycopg2.connect(
#         host="localhost",
#         database="postgres",
#         user=os.environ["POSTGRES_USER"],
#         password=os.environ["POSTGRES_PASSWORD"],
#     )


@app.route("/")
def root():
    return "Hello World!"


@app.route("/characters")
def get_characters():
    return "characters!"
    # connection = get_db_connection()
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM character;")
    # characters = cursor.fetchall()
    # cursor.close()
    # connection.close()
    # return jsonify(characters)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
