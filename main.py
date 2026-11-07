from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
app= Flask(__name__)
# ------------------------- DATABASE -------------------------------------
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[float] = mapped_column(String, nullable=False)
    location: Mapped[float] = mapped_column(String, nullable=False)
    has_sockets: Mapped[float] = mapped_column(String, nullable=False)
    has_toilets: Mapped[float] = mapped_column(String, nullable=False)
    can_take_calls: Mapped[float] = mapped_column(String, nullable=False)
    seats: Mapped[float] = mapped_column(String, nullable=False)
    coffee_price: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

# ------------------------- ROUTES ---------------------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cafes")
def cafes():
    return render_template("cafes.html")



if __name__== "__main__":
    app.run(debug=True)

# TODO: 2. create a table webpage which shows a given data
# TODO: 3. create a form that lets users add data to to db
# TODO: 4. create db and feed data
# TODO: 5. add user fed data to db
