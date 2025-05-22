from flask import Flask, render_template, request
import sqlite3

# Initialize the Flask app
app = Flask(__name__, template_folder='templates')

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('../database/student_dashboard.db')  # Make sure this path is correct
    conn.row_factory = sqlite3.Row
    return conn

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the profile page
@app.route('/profile')
def profile():
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = 1').fetchone()
    conn.close()
    return render_template('profile.html', student=student)

# Route for the test page
@app.route('/test', methods=['GET', 'POST'])
def test_page():
    grade = None
    total = None
    error = None

    if request.method == 'POST':
        try:
            internal = request.form['internal']
            external = request.form['external']

            if not internal or not external:
                error = "Please enter both marks."
            else:
                internal = int(internal)
                external = int(external)
                total = internal + external

                if total >= 90:
                    grade = 'A+'
                elif total >= 80:
                    grade = 'A'
                elif total >= 70:
                    grade = 'B'
                elif total >= 60:
                    grade = 'C'
                elif total >= 50:
                    grade = 'D'
                else:
                    grade = 'F'
        except ValueError:
            error = "Please enter valid numbers."

    return render_template('test.html', grade=grade, total=total, error=error)

# Route for uploading/viewing books (if required)
@app.route('/books', methods=['GET', 'POST'])
def books():
    error = None
    success = None

    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')

        if not title or not author:
            error = "Please provide both title and author."
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
            conn.commit()
            conn.close()
            success = "Book added successfully."

    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return render_template('books.html', books=books, error=error, success=success)

if __name__ == '__main__':
    app.run(debug=True)    