from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# ---------- DATABASE CONNECTION ----------

def get_db_connection():
    """
    Returns a new MySQL connection.
    Change user/password if yours are different.
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",           # <-- your MySQL username
        password="myPassword$12",  # <-- put your MySQL password here
        database="mydb"        # <-- your database name
    )

# ---------- ROUTES ----------

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
    """
    Fetch all courses from the `course-list` table in `mydb`
    and pass them to templates/courses.html as `courses`.
    """
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            CourseTitle,
            CourseType,
            CourseSummary,
            CourseAwardName,
            UcasCode,
            UcasPoints,
            YearOfEntry,
            ModeOfAttendance,
            StudyLength,
            HasFoundationYear,
            CourseSubject,
            NoLongerRecruiting
        FROM `course-list`;
    """)

    course_list = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("courses.html", courses=course_list)


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


# ---------- MAIN ----------

if __name__ == "__main__":
    app.run(debug=True)
