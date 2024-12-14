import sqlite3 # database module

# Create or Locate Table
def signUp():
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    # Student table for student accounts
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        full_name TEXT NOT NULL
    )""")
    # Teacher table for teacher accounts
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teacher (
        teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        full_name TEXT NOT NULL
    )""")
    # Assessment table for assessments created by teachers
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assessment (
        assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id)
    )""")
    # Review table for reviews created or edited by students
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS review (
        review_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        assessment_id INTEGER NOT NULL,
        review_content TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES student(student_id),
        FOREIGN KEY (assessment_id) REFERENCES assessment(assessment_id)
    )""")
    # Student answer table for storing student answers
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_answer (
        answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        assessment_id INTEGER NOT NULL,
        selected_option TEXT NOT NULL,
        submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES student(student_id),
        FOREIGN KEY (assessment_id) REFERENCES assessment(assessment_id)
    )""")
    # Scores and feedback table for storing scores and teacher feedback
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores_feedback (
        feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        assessment_id INTEGER NOT NULL,
        score INTEGER NOT NULL,
        feedback TEXT,
        teacher_id INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES student(student_id),
        FOREIGN KEY (assessment_id) REFERENCES assessment(assessment_id),
        FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id)
    )""")
    connect.commit()
    connect.close()
# ======================================= STUDENT ACCOUNT DATABASE =====================================
# Add student account
def addNewStudent(username, password, full_name):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO student (username, password, full_name) VALUES (?, ?, ?)", (username, password, full_name))
    connect.commit()
    connect.close()
# Check if username already exist
def checkStudentAcc(username):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("SELECT username FROM student WHERE username = ?", (username,))
    result = cursor.fetchall()
    connect.close()
    return result
# check student account from database
def studentLog(username, password):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM student WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    # Check if a result was found
    if result:
        return True  # Indicate successful login
    else:
        return False  # Indicate login failure
    connect.close()
# ======================================= TEACHER ACCOUNT DATABASE =====================================
# Add teacher account
def addNewTeacher(username, password, full_name):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO teacher (username, password, full_name) VALUES (?, ?, ?)", (username, password, full_name))
    connect.commit()
    connect.close()
# Check if username already exist
def checkTeacherAcc(username):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("SELECT username FROM teacher WHERE username = ?", (username,))
    result = cursor.fetchall()
    connect.close()
    return result
# check teaher account from database
def teacherLog(username, password):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM teacher WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    # Check if a result was found
    if result:
        return True  # Indicate successful login
    else:
        return False  # Indicate login failure
    connect.close()
# ======================================= QUIZ DATABASE =====================================
# Create Assessment
def createAssessment(subject, question, optionA, optionB, optionC, optionD, answer):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO assessment (subject, question, optionA, optionB, optionC, optionD, answer) VALUES (?, ?, ?, ?, ?, ?, ?)", (subject, question, optionA, optionB, optionC, optionD, answer))
    connect.commit()
    connect.close()
# Display assessment
def displayAssessment(subject):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM assessment WHERE subject=?", (subject,))
    assessment = cursor.fetchall()
    connect.close()
    return assessment

signUp()