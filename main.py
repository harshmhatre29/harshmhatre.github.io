from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def harsh():
    return render_template("index.html")

@app.route('/Home')
def harsh_home():
    return render_template("index.html")

@app.route('/About')
def harsh_about():
    return render_template("about.html")

@app.route('/Contact')
def harsh_contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')