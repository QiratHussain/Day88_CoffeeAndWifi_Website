from flask import Flask, render_template, redirect

app= Flask(__name__)

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
