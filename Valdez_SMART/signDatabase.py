import sqlite3 # database module

# Create or Locate Table
def signUp():
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS student(
                    username text,
                    password text
                    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS teacher(
                    username text,
                    password text
                    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS assessment(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    subject TEXT NOT NULL,
                    question TEXT NOT NULL,
                    optionA TEXT NOT NULL,
                    optionB TEXT NOT NULL,
                    optionC TEXT NOT NULL,
                    optionD TEXT NOT NULL,
                    answer TEXT NOT NULL
                    )""")
    connect.commit()
    connect.close()
# ======================================= STUDENT ACCOUNT DATABASE =====================================
# Add student account
def addNewStudent(username, password):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO student (username, password) VALUES (?, ?)", (username, password))
    connect.commit()
    connect.close()
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
def addNewTeacher(username, password):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO teacher (username, password) VALUES (?, ?)", (username, password))
    connect.commit()
    connect.close()
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