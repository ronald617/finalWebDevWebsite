from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/businesses")
def businesses():
    return render_template("businesses.html")

@app.route("/computing")
def computing():
    return render_template("computing.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/design")
def design():
    return render_template("design.html")

@app.route("/facilities")
def facilities():
    return render_template("facilities.html")

@app.route("/howToFindUs")
def howToFindUs():
    return render_template("howToFindUs.html")

@app.route("/informationStaff")
def informationStaff():
    return render_template("informationStaff.html")

@app.route("/informationStudents")
def informationStudents():
    return render_template("informationStudents.html")

@app.route("/learningResources")
def learningResources():
    return render_template("learningResources.html")


if __name__ == "__main__":
    app.run(debug=True)
