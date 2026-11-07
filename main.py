from flask import Flask, render_template, redirect , request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app= Flask(__name__)
# ------------------------- FORM  -------------------------------------
app.config['SECRET_KEY'] = 'just-a-key'
bootstrap = Bootstrap5(app)
class Cafe_Form(FlaskForm):
  name = StringField('Cafe Name', validators=[DataRequired()])
  map_url = StringField('Map URL', validators=[DataRequired()])
  img_url = StringField('Image URL', validators=[DataRequired()])
  has_socket = StringField('Socket', validators=[DataRequired()])
  location = StringField('Location', validators=[DataRequired()])
  has_wifi = StringField('Wifi', validators=[DataRequired()])  
  has_toilet = StringField('Toilet', validators=[DataRequired()])
  can_take_calls = StringField('Can Take Calls', validators=[DataRequired()])
  seats = StringField('Seats', validators=[DataRequired()])
  coffee_price = StringField('Coffee Price', validators=[DataRequired()])
  submit = SubmitField('Submit')

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
    has_toilet: Mapped[float] = mapped_column(String, nullable=False)
    can_take_calls: Mapped[float] = mapped_column(String, nullable=False)
    seats: Mapped[float] = mapped_column(String, nullable=False)
    coffee_price: Mapped[float] = mapped_column(Float, nullable=False)
    has_wifi :Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

# ------------------------- ROUTES ---------------------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cafes")
def cafes():
    with app.app_context():
        result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
        cafes_list = result.scalars().all()
    return render_template("cafes.html", data_list= cafes_list)

@app.route("/add", methods= ['POST', 'GET'])
def add_cafe():
    add_form= Cafe_Form()
    if request.method=='POST':
        with app.app_context():
            new_cafe= Cafe( name = add_form.name.data, map_url = add_form.map_url.data, img_url= add_form.img_url.data, 
            location= add_form.location.data, has_sockets= add_form.has_socket.data, has_wifi = add_form.has_wifi.data,
            can_take_calls= add_form.can_take_calls.data, seats= add_form.seats.data,
            has_toilet= add_form.has_toilet.data, coffee_price= add_form.coffee_price.data, )
            db.session.add(new_cafe)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("add.html", form= add_form)

# ---------------------------------------------------------------------------
if __name__== "__main__":
    app.run(debug=True)

