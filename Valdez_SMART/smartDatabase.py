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
        full_name TEXT NOT NULL UNIQUE
    )""")
    # Teacher table for teacher accounts
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teacher (
        teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        full_name TEXT NOT NULL UNIQUE
    )""")
    # Assessment table for assessments created by teachers
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assessment (
        assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        question TEXT NOT NULL UNIQUE,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id)
    )""")
    # Flashcard table for flashcards created or edited by students
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS flashcard (
        flashcard_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        question TEXT NOT NULL UNIQUE,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES student(student_id)
    )""")
    # Student Assessment score table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS score_and_feedback (
        score_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        assessment_id INTEGER NOT NULL,
        teacher_id INTEGER NOT NULL,
        attempt_number INTEGER NOT NULL,
        score INTEGER NOT NULL UNIQUE,
        feedback TEXT,
        FOREIGN KEY (student_id) REFERENCES student(student_id),
        FOREIGN KEY (assessment_id) REFERENCES assessment(assessment_id),
        FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id)
    )""")
    connect.commit()
    connect.close()
# ======================================= POPULATE DATA =====================================
# Populate Student
def populateStudent():
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute(""" 
        INSERT OR IGNORE INTO student(username, password, full_name)
        VALUES
        ('Calexia', 'calexia', 'Valdez, Alejandra Patria '),
        ('nhari', 'nhari', 'Arguelles, Kriskyla '),
        ('hajinomoto', 'hajinomoto', 'Balmes, Katrine Angeleen '),
        ('Azelt', 'azelt', 'Dela Cruz, Chester Paul'),
        ('karishe', 'karishe', 'Valida, Keil Rizher'),
        ('Cyz', 'Cyz', 'Magpantay, Cyzries'),
        ('odeth', 'odeth', 'Doria, Jodeth '),
        ('apple', 'apple', 'Comia, Andrea '),
        ('njelaxx', 'njelaxx', 'Becite, Nicole Angela'),
        ('vaughnamr', 'vaughnamr', 'Amar, Vaugh Philip Samuel'),
        ('jhonleks', 'jhonleks', 'Bacani, John Lex'),
        ('margarethsss', 'margarethsss', 'Comia, Margareth'),
        ('cessykath', 'cessykath', 'Llarenas, Princess Kathleen'),
        ('janreb', 'janreb', 'Vergara, John Reb'),
        ('yeskween', 'yeskween', 'Evangelio, Jayvee')
    """)
    connect.commit()
    connect.close()
# Populate teacher
def populateTeacher():
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute(""" 
        INSERT OR IGNORE INTO teacher(username, password, full_name)
        VALUES
        ('arjo', 'arjo', 'MENDOZA, ARJONEL M.'),
        ('mau', 'mau', 'DELA CRUZ, MAURICE OLIVER Y.'),
        ('joe', 'joe', 'DE CASTRO, JOEY R.'),
        ('glyy', 'glyy', 'REYES, GLYDEL ANN E.'),
        ('karenn', 'karenn', 'MENDOZA, BABY KAREN L.'),
        ('Jeyzel', 'Jeyzel', 'MADLANGBAYAN, JAZEL B.'),
        ('Adlang', 'Adlang', 'MADLANGBAYAN, ALLEN B.'),
        ('ria', 'ria', 'CASTILLO, RIA L.'),
        ('kimm', 'kimm', 'MARASIGAN, KIMBERLY I.'),
        ('ange', 'ange', 'SISON, MARIA ANGELICA E.'),
        ('sharm', 'sharm', 'MALALUAN, SHARMAINE S.'),
        ('mariel', 'mariel', 'MANDANE, JOHN MARIEL P.'),
        ('selka', 'cessykath', 'MAURICIO, KAREN SELKA V.'),
        ('laersi', 'laersi', 'PENERO, ISRAEL P.'),
        ('marieemoiselle', 'marieemoiselle', 'AGDON, FATIMA MARIE P.')
    """)
    connect.commit()
    connect.close()
# Populate Assessment
def populateAssessment():
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute(""" 
        INSERT OR IGNORE INTO assessment (teacher_id, subject, question, option_a, option_b, option_c, option_d, correct_answer)
        VALUES
        (1, 'English', 'What is the synonym of "happy"?', 'Sad', 'Angry', 'Joyful', 'Lazy', 'Joyful'),
        (2, 'Mathematics', 'What is 5 + 7?', '10', '12', '11', '13', '12'),
        (3, 'Science', 'What is the chemical symbol for water?', 'H2O', 'CO2', 'O2', 'NaCl', 'H2O'),
        (4, 'English', 'What is the antonym of "difficult"?', 'Easy', 'Hard', 'Tough', 'Complex', 'Easy'),
        (5, 'Mathematics', 'What is the square root of 64?', '6', '7', '8', '9', '8'),
        (6, 'Science', 'What planet is known as the Red Planet?', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Mars'),
        (7, 'English', 'Choose the correct verb: "She ___ to school every day."', 'Go', 'Goes', 'Went', 'Gone', 'Goes'),
        (8, 'Mathematics', 'What is 15 x 3?', '30', '45', '50', '60', '45'),
        (9, 'Science', 'What is the process by which plants make their food?', 'Digestion', 'Respiration', 'Photosynthesis', 'Fermentation', 'Photosynthesis'),
        (10, 'English', 'What is a group of lions called?', 'Herd', 'Pack', 'Pride', 'Flock', 'Pride'),
        (11, 'Mathematics', 'What is 81 divided by 9?', '7', '8', '9', '10', '9'),
        (12, 'Science', 'What gas do humans breathe in?', 'Oxygen', 'Nitrogen', 'Carbon Dioxide', 'Helium', 'Oxygen'),
        (13, 'English', 'What is the plural of "child"?', 'Childs', 'Childes', 'Children', 'Childrens', 'Children'),
        (14, 'Mathematics', 'What is the value of Pi up to two decimal places?', '3.12', '3.13', '3.14', '3.15', '3.14'),
        (15, 'Science', 'What is the boiling point of water in Celsius?', '90', '95', '100', '110', '100')
    """)
    connect.commit()
    connect.close()
# Populate Flashcard
def populateFlashcard():
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute(""" 
        INSERT OR IGNORE INTO flashcard (student_id, subject, question, option_a, option_b, option_c, option_d, correct_answer)
        VALUES
        (1, 'English', 'What is the opposite of "fast"?', 'Slow', 'Quick', 'Rapid', 'Swift', 'Slow'),
        (2, 'Mathematics', 'What is 7 - 3?', '4', '5', '3', '6', '4'),
        (3, 'Science', 'What is the largest planet in the solar system?', 'Earth', 'Jupiter', 'Mars', 'Saturn', 'Jupiter'),
        (4, 'English', 'What is the past tense of "run"?', 'Running', 'Ran', 'Runs', 'Runned', 'Ran'),
        (5, 'Mathematics', 'What is 9 x 9?', '80', '81', '82', '83', '81'),
        (6, 'Science', 'What is the main gas in the air we breathe?', 'Oxygen', 'Nitrogen', 'Carbon Dioxide', 'Helium', 'Nitrogen'),
        (7, 'English', 'What is a synonym of "big"?', 'Tiny', 'Small', 'Large', 'Thin', 'Large'),
        (8, 'Mathematics', 'What is 25 divided by 5?', '4', '5', '6', '7', '5'),
        (9, 'Science', 'What organ pumps blood through the body?', 'Lungs', 'Heart', 'Brain', 'Kidneys', 'Heart'),
        (10, 'English', 'What is the plural of "mouse"?', 'Mouses', 'Mouse', 'Mice', 'Mices', 'Mice'),
        (11, 'Mathematics', 'What is 2 raised to the power of 3?', '6', '7', '8', '9', '8'),
        (12, 'Science', 'What is the primary source of energy for life on Earth?', 'Moon', 'Sun', 'Wind', 'Water', 'Sun'),
        (13, 'English', 'What is the past tense of "write"?', 'Writing', 'Wrote', 'Writes', 'Written', 'Wrote'),
        (14, 'Mathematics', 'What is 50% of 100?', '40', '45', '50', '60', '50'),
        (15, 'Science', 'What part of the plant conducts photosynthesis?', 'Stem', 'Roots', 'Leaves', 'Flowers', 'Leaves')
    """)
    connect.commit()
    connect.close()
# Populate ScoreFeedback
def populateScoreFeedback():
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute(""" 
        INSERT OR IGNORE INTO score_and_feedback (student_id, assessment_id, teacher_id, attempt_number, score, feedback)
        VALUES
        (1, 1, 1, 1, 5, 'Good attempt, but work on synonyms.'),
        (2, 2, 2, 1, 4, 'Great job! Keep practicing math.'),
        (3, 3, 3, 1, 5, 'Excellent! Perfect understanding of the topic.'),
        (4, 4, 1, 2, 2, 'Focus more on antonyms.'),
        (5, 5, 2, 1, 4, 'Good work! Revise square roots.'),
        (6, 6, 3, 1, 4, 'Very well done on planetary facts.'),
        (7, 7, 1, 2, 3, 'Watch verb agreement rules.'),
        (8, 8, 2, 1, 5, 'Outstanding! You are excellent at multiplication.'),
        (9, 9, 3, 1, 4, 'Great! Revise photosynthesis further.'),
        (10, 10, 1, 2, 4, 'Work on collective nouns.'),
        (11, 11, 2, 1, 4, 'Good attempt. Division is your strength!'),
        (12, 12, 3, 1, 4, 'Excellent understanding of gases.'),
        (13, 13, 1, 2, 3, 'Revise plural forms of irregular nouns.'),
        (14, 14, 2, 1, 4, 'Well done! Pi approximation is correct.'),
        (15, 15, 3, 1, 5, 'Perfect knowledge of water boiling point.')
    """)
    connect.commit()
    connect.close()
# ======================================= STUDENT ACCOUNT TABLE =====================================
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
    connect.close()
    return result
# ======================================= TEACHER ACCOUNT TABLE =====================================
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
    connect.close()
    return result
# ======================================= ASSESSMENT TABLE =====================================
# Create Assessment
def createAssessment(teacher_id, subject, question, option_a, option_b, option_c, option_d, correct_answer):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute(
        "INSERT INTO assessment (teacher_id, subject, question, option_a, option_b, option_c, option_d, correct_answer) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
        (
            teacher_id, 
            subject, 
            question, 
            option_a, 
            option_b, 
            option_c, 
            option_d, 
            correct_answer
        ))
    connect.commit()
    connect.close()
# Display assessment by Subject
def displayAssessment(subject):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("""
        SELECT 
            assessment_id,
            assessment.subject, 
            assessment.question, 
            assessment.option_a, 
            assessment.option_b, 
            assessment.option_c, 
            assessment.option_d, 
            assessment.correct_answer, 
            teacher.username,
            teacher.teacher_id
        FROM assessment
        JOIN teacher ON assessment.teacher_id = teacher.teacher_id
        WHERE assessment.subject = ?
    """, (subject,))
    assessment = cursor.fetchall()
    connect.close()
    return assessment
# Delete Assessment
def deleteAssessment(assessment_id):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM assessment WHERE assessment_id=?", (assessment_id,))
    connect.commit()
    connect.close()
# Fetch assessment by assessment id
def searchAssessment(assessment_id):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM assessment WHERE assessment_id=?", (assessment_id,))
    assessment = cursor.fetchall()
    connect.close()
    return assessment
# Update Assessment from database
def updateAssessment(assessment_id, subject, question, option_a, option_b, option_c, option_d, correct_answer):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("""
        UPDATE assessment
        SET subject = ?, question = ?, option_a = ?, option_b = ?, option_c = ?, option_d = ?, correct_answer = ?
        WHERE assessment_id = ?
    """, (subject, question, option_a, option_b, option_c, option_d, correct_answer, assessment_id))
    connect.commit()
    connect.close()
# ======================================= FLASHCARD TABLE =====================================
# Create Flashcard
def createFlashcard(student_id, subject, question, option_a, option_b, option_c, option_d, correct_answer):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute(
        "INSERT INTO flashcard (student_id, subject, question, option_a, option_b, option_c, option_d, correct_answer) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
        (
            student_id, 
            subject, 
            question, 
            option_a, 
            option_b, 
            option_c, 
            option_d, 
            correct_answer
        ))
    connect.commit()
    connect.close()
# Join Flashcard content and student table
def displayFlashcard():
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("""
        SELECT 
            flashcard_id,
            flashcard.subject, 
            flashcard.question, 
            flashcard.option_a, 
            flashcard.option_b, 
            flashcard.option_c, 
            flashcard.option_d, 
            flashcard.correct_answer, 
            student.username 
        FROM flashcard
        JOIN student ON flashcard.student_id = student.student_id
        ORDER BY flashcard.subject
    """)
    result = cursor.fetchall()
    connect.close()
    return result
# Delete Flashcard
def deleteFlashcard(flashcard_id):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM flashcard WHERE flashcard_id=?", (flashcard_id,))
    connect.commit()
    connect.close()
# Fetch flashcard by flashcard id
def searchFlashcard(flashcard):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM flashcard WHERE flashcard_id=?", (flashcard,))
    flashcard = cursor.fetchall()
    connect.close()
    return flashcard
# update flashcard
def updateFlashcard(flashcard_id, subject, question, option_a, option_b, option_c, option_d, correct_answer):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("""
        UPDATE flashcard
        SET subject = ?, question = ?, option_a = ?, option_b = ?, option_c = ?, option_d = ?, correct_answer = ?
        WHERE flashcard_id = ?
    """, (subject, question, option_a, option_b, option_c, option_d, correct_answer, flashcard_id))
    connect.commit()
    connect.close()
# Display flashcard by Subject
def displayFlashcardSubject(subject):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM flashcard WHERE subject=?", (subject,))
    flashcard = cursor.fetchall()
    connect.close()
    return flashcard
# ======================================= STUDENT ANSWER DATABASE =====================================
# Create score
def studentScore(student_id, assessment_id, teacher_id, attempt_number, score):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO score_and_feedback (student_id, assessment_id, teacher_id, attempt_number, score) VALUES (?, ?, ?, ?, ?)", (student_id, assessment_id, teacher_id, attempt_number, score,))
    connect.commit()
    connect.close()
# Display Score Table
def displayScore():
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM score_and_feedback")
    result = cursor.fetchall()
    connect.close()
    return result
# Check Score Table
def checkAttempt(student_id, assessment_id):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("SELECT score_id, attempt_number FROM score_and_feedback WHERE student_id = ? AND assessment_id = ?", (student_id, assessment_id,))
    result = cursor.fetchall()
    connect.close()
    return result
# Update Score
def updateScore(student_id, assessment_id, score, attempt_number):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("""
        UPDATE score_and_feedback
        SET score = ?, attempt_number = ?
        WHERE student_id = ? AND assessment_id = ?
    """, (score, attempt_number, student_id, assessment_id))
    connect.commit()
    connect.close()
# ======================================= VIEW SCORE DATABASE =====================================
# Student View by his Student ID
def studentView(student_id):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("""
        SELECT s.student_id, s.full_name, a.subject, ascore.score, ascore.attempt_number, ascore.feedback
        FROM score_and_feedback ascore
        JOIN student s ON ascore.student_id = s.student_id
        JOIN assessment a ON ascore.assessment_id = a.assessment_id
        JOIN teacher t ON ascore.teacher_id = t.teacher_id
        WHERE s.student_id = ?
    """, (student_id,))
    result = cursor.fetchall()
    connect.close()
    return result
# Teacher View on all students
def TeachertView():
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("""
        SELECT s.student_id, s.full_name, a.subject, ascore.score, ascore.attempt_number, ascore.feedback
        FROM score_and_feedback ascore
        JOIN student s ON ascore.student_id = s.student_id
        JOIN assessment a ON ascore.assessment_id = a.assessment_id
        JOIN teacher t ON ascore.teacher_id = t.teacher_id
    """)
    result = cursor.fetchall()
    connect.close()
    return result

def updateFeedback(student_id, teacher_id, feedback):
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("""
        UPDATE score_and_feedback
        SET feedback = ?, teacher_id = ?
        WHERE student_id = ?
    """, (feedback, teacher_id, student_id))
    connect.commit()
    connect.close()
# ======================================= VIEW SCORE DATABASE =====================================
def count():
    connect = sqlite3.connect("smart.db")
    cursor = connect.cursor()
    cursor.execute("SELECT COUNT(*) FROM assessment")
    assessment = cursor.fetchone
    cursor.execute("SELECT COUNT(*) FROM flashcard")
    flashcard = cursor.fetchone
    connect.close()
    count = assessment + flashcard
    return count

signUp()
populateStudent()
populateTeacher()
populateAssessment()
populateFlashcard()
populateScoreFeedback()