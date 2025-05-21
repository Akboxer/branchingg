from flask import Flask, render_template, request , redirect
import mysql.connector
import pymysql

app = Flask(__name__)

# MySQL connection setup
db = mysql.connector.connect(
    host="localhost",
    user="root",               # ← your MySQL username
    password="Pks@1777",  # ← your MySQL password
    database="school"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    student_class = request.form['class']
    gender = request.form['gender']

    query = "INSERT INTO student (name, class, gender) VALUES (%s, %s, %s)"
    values = (name, student_class, gender)
    cursor.execute(query, values)
    db.commit()

    return "✅ Data submitted successfully!"



@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        password = request.form['password']
        if password == "admin123":
            return redirect("/admin")
        else:
            return render_template('login.html', error="Incorrect password")

    # GET request — with optional filter
    gender = request.args.get('gender')
    cursor = db.cursor()

    if gender:
        cursor.execute("SELECT name, class, gender FROM student WHERE gender = %s", (gender,))
    else:
        cursor.execute("SELECT name, class, gender FROM student")

    data = cursor.fetchall()
    return render_template('dashboard.html', students=data, selected_gender=gender)


if __name__ == '__main__':
    app.run(debug=True)
