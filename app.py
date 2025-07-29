from flask import Flask, render_template, request
from rectangle import Rectangle

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["GET", "POST"])
def calculate_area():
    #use this if method = POST
    #length = float(request.form['length'])
    #width = float(request.form['width'])

    #use this if method = GET
    length = float(request.args['length'])
    width = float(request.args['width'])


    rect = Rectangle(length, width)
    result = rect.area()

    return render_template("result.html", area=result)

if __name__ == "__main__":
    app.run(debug=True)