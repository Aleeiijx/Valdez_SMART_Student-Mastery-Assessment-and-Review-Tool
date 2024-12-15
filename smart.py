from tkinter import *           # GUI / tkinter
from tkinter import messagebox  # messagebox
from tkinter import ttk         # combobox, treeview
from time import *              # time module
import smartDatabase            # sqlite3 database file

# First Window
class Smart():
    studentLogIn_called = False
    teacherLogIn_called = False
    def __init__(self, window):
        self.window = window
        self.window.title("Student Mastery Assessment and Review Tool")
        self.window.geometry("1200x650+50+50")
        self.window.config(bg="#481054")
        self.window.resizable(0, 0)
        # Background Image
        self.bgphoto = PhotoImage(file='background.png') # background image
        background = Label(self.window, image=self.bgphoto, bg='#A786EF')
        background.place(relx=.5, rely=.5, anchor=CENTER) # background picture location
        # Student Log In````
        def studentLogIn():
            Smart.studentLogIn_called = True
            Smart.teacherLogIn_called = False
            self.window.destroy()
            logIn_window = Tk()
            logIn(logIn_window)
            logIn_window.mainloop()
        # Teacher Log In
        def teacherLogIn():
            Smart.teacherLogIn_called = True
            Smart.studentLogIn_called = False
            self.window.destroy()
            logIn_window = Tk()
            logIn(logIn_window)
            logIn_window.mainloop()
        # I AM A text
        title = Label(self.window, text='I AM A', fg='black', bg='#B391B5', font=('Times New Roman', 50), bd=3, relief=RAISED, padx=10)
        title.pack(pady=50)
        # Picture
        self.student = PhotoImage(file='student.png')
        self.teacher = PhotoImage(file='teacher.png')
        # Button fors Student and Teacher
        self.student_window = Button(self.window, image=self.student, command=studentLogIn, bd=4, bg="#B391B5", activebackground="#B391B5", cursor='hand2') # student button
        self.student_window.place(relx=0.5, rely=0.5, anchor=CENTER, x=-200) # student button lcoation
        self.teacher_window = Button(self.window, image=self.teacher, command=teacherLogIn, bd=4, bg="#B391B5", activebackground="#B391B5", cursor='hand2') # teacher button
        self.teacher_window.place(relx=0.5, rely=0.5, anchor=CENTER, x=200) # teacher button location
        # Label for Buttons
        self.student_text = Label(window, text='STUDENT', fg='black', bg='#B391B5', font=('Times New Roman', 40), padx=5, bd=3, relief=RIDGE)
        self.student_text.place(relx=0.5, rely=0.81, anchor=CENTER, x=-200)
        self.teacher_text = Label(window, text='TEACHER', fg='black', bg='#B391B5', font=('Times New Roman', 40), padx=5, bd=3, relief=RIDGE)
        self.teacher_text.place(relx=0.5, rely=0.81, anchor=CENTER, x=200)

# Log In Window
class logIn:
    def __init__(self, window):
        self.window = window
        self.window.title("Student Mastery Assessment and Review Tool") # Title of the window
        self.window.geometry("1200x650+150+100") # size of the window
        self.window.config(bg="#481054") # background color of the window
        self.window.resizable(0, 0) # cannot resize window
        # background Image
        self.bgphoto = PhotoImage(file='background.png') # background image
        background = Label(self.window, image=self.bgphoto, bg='#A786EF')
        background.place(relx=.5, rely=.5, anchor=CENTER) # background picture location
        framebg = PhotoImage(file='framebg.png') # box background picture to make it look transparent
        # Log In Box
        self.box = Frame(background, width=350, height=450, bd=3, bg='#B391B5',relief=RAISED)  # purple box without border
        self.box.place(relx=.52, rely=.415, anchor=CENTER)  # purple box location
        self.boxlabel = Label(self.box, image=framebg)
        self.boxlabel.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.boxlabel.image = framebg
        # Log in Text
        logIn = Label(self.box, text='Log In Form', fg='black', bg='#B391B5', font=('Times New Roman', 20)) # Log in text insinde purple box
        logIn.place(x=10, y=10) # log in text purple box location
        # Username Code
        self.user = Entry(self.box, width=20, fg='black', border=0, bg='#B391B5', font=('Times New Roman', 20)) # Input fields for Username
        self.user.place(x=30,y=75) # Username Location
        self.user.insert(0, 'Username') # Text Inside username
        self.user.bind('<FocusIn>', lambda e: self.user.delete(0, 'end'))  # Clear on focus
        self.user.bind('<FocusOut>', lambda e: self.user.insert(0, 'Username') if not self.user.get() else None)  # Restore placeholder if empty
        Frame(self.box, width=280, height=2, bg='black').place(x=30, y=109) # straight line under passwordx xxx
        # Password Code
        self.passcode = Entry(self.box, width=20, fg='black', border=0, bg='#B391B5', font=('Times New Roman', 20), show='*') # input fields for password
        self.passcode.place(x=30, y=155) # Password Location
        self.passcode.insert(0, 'Password') # Text Inside Password
        self.passcode.bind('<FocusIn>', lambda e: self.passcode.delete(0, 'end')) # pag clinick yung password ay mawawala sya
        self.passcode.bind('<FocusOut>', lambda e: self.passcode.insert(0, 'Password')) # pag hindi clinick ay ididisplay password
        Frame(self.box, width=280, height=2, bg='black').place(x=30, y=189) # straight line under password
        # Eye Icon Button
        self.close_img = PhotoImage(file='close_eye.png') # image for close eye
        self.open_img = PhotoImage(file='open_eye.png') # image for open eye
        self.showBtn=Button(self.passcode,image=self.close_img,border=0,bg='#B391B5',activebackground='#B391B5',cursor='hand2',command=self.show) # Eye Button
        self.showBtn.place(relx=.97, rely=.5, anchor=E) # eye button location
        # Log in Button differs depending whether student or teacher
        if Smart.studentLogIn_called:
            Button(self.box, width=35, pady=7, text='Student Log In', bg='black', fg='white', border=0, cursor='hand2', command=self.studentLog).place(x=35, y=250) # Login Button
        elif Smart.teacherLogIn_called:
            Button(self.box, width=35, pady=7, text='Teacher Log In', bg='black', fg='white', border=0, cursor='hand2', command=self.teacherLog).place(x=35, y=250) # Login Button
        # Label Text Under Log in
        account = Label(self.box, text="Don't have an account yet?", fg='black', bg='#B391B5', font=('Times New Roman', 12)) # Don't have an account yet Label
        account.place(x=55, y=300) # location ng Don't have an account yet
        Button(self.box, width=35, pady=7, text='Back', bg='black', fg='white', border=0, cursor='hand2', command=self.backbtn).place(x=35, y=350) # Back button
        sign = Button(self.box, width=6, text='Sign Up', font='Times 12', bg='black', fg='white', border=0, cursor='hand2', command=self.signup) # Sign Up Button
        sign.place(x=230, y=300) # sign up button location
    # Eye Button Function to reveal 
    def show(self):
        self.showBtn.config(image=self.open_img,bd=0,bg='#B391B5',activebackground='#B391B5',cursor='hand2', command=self.hide)
        self.passcode.config(show='')
    def hide(self):
        self.showBtn.config(image=self.close_img,bd=0,bg='#B391B5',activebackground='#B391B5',cursor='hand2', command=self.show)
        self.passcode.config(show='*')
    # Back Button to go back to chossing between student and teacher
    def backbtn(self):
        self.window.destroy()
        smart_window = Tk()
        Smart(smart_window)
        smart_window.mainloop()
    # Sign Up Window
    def signup(self):
        self.new_window = Toplevel(self.window)
        self.app = signUp(self.new_window)
    # student account
    def studentLog(self):
        username = self.user.get()
        password = self.passcode.get()
        userData = smartDatabase.studentLog(username, password)
        if username == 'Username' or password == 'Password' or not username or not password:
            messagebox.showerror("Invalid Input", "Please enter both username and password")
            return
        elif userData:
            messagebox.showinfo("Success!", f"Log In Succesfully!\n\nWelcome back {username}!")
            self.window.destroy()
            smart_window = Tk()
            studentDashboard(smart_window, userData)
            smart_window.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    # teacher account
    def teacherLog(self):
        username = self.user.get()
        password = self.passcode.get()
        userData = smartDatabase.teacherLog(username, password)
        if username == 'Username' or password == 'Password' or not username or not password:
            messagebox.showerror("Invalid Input", "Please enter both username and password")
            return
        elif userData:
            messagebox.showinfo("Success!", f"Log In Succesfully!\n\nWelcome back {username}!")
            self.window.destroy()
            smart_window = Tk()
            teacherDashboard(smart_window, userData)
            smart_window.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

# Sign Up Window
class signUp():
    def __init__(self, window):
        self.window = window
        self.window.title("Student Mastery Assessment and Review Tool")
        self.window.geometry("400x400+750+225")
        self.window.config(bg="#413B46")
        self.window.resizable(0, 0)
        # Log In Box
        self.box = Label(self.window, width=50, height=25, bg='#B391B5') # Log In box
        self.box.place(relx=.5, rely=.5, relwidth=.9, relheight=.9, anchor=CENTER) # Log In box location
        # Sign Up Text
        self.logIn = Label(self.box, text='Sign Up Form', fg='black', bg='#B391B5', font=('Times New Roman', 20)) # Sign Up Text
        self.logIn.pack() # Sign Up Text location
        # Full Name Input Fields
        self.fullnameFrame = LabelFrame(self.box, text='Full Name', fg='black', bg='#B391B5', font=('Times New Roman', 12))
        self.fullnameFrame.pack()  # Adjusted size for alignment
        self.fullname_sign = Entry(self.fullnameFrame, width=20, fg='black', bg='#B391B5', font=('Times New Roman', 20), bd=0)
        self.fullname_sign.pack(padx=5)  # Padding inside the LabelFrame
        # Username Input Fields
        self.username_frame = LabelFrame(self.box, text='Username', fg='black', bg='#B391B5', font=('Times New Roman', 12))
        self.username_frame.pack()  # Adjusted size for alignment
        self.username_sign = Entry(self.username_frame, width=20, fg='black', bg='#B391B5', font=('Times New Roman', 20), bd=0)
        self.username_sign.pack(padx=5)  # Padding inside the LabelFrame
        # Image show eye
        self.close_img = PhotoImage(file='close_eye.png') # image for close eye
        self.open_img = PhotoImage(file='open_eye.png') # image for open eye
        # Password Input Fields
        self.password_frame = LabelFrame(self.box, text='Password', fg='black', bg='#B391B5', font=('Times New Roman', 12))
        self.password_frame.pack()  # Adjusted size for alignment
        self.password_sign = Entry(self.password_frame, width=20, fg='black', bg='#B391B5', font=('Times New Roman', 20), show='*', bd=0)
        self.password_sign.pack(padx=5)  # Padding inside the LabelFrame
        # Show Password Button
        self.showBtn=Button(self.password_sign,image=self.close_img,border=0,bg='#B391B5',activebackground='#B391B5',cursor='hand2', command=self.show) # Eye Button
        self.showBtn.place(relx=.97, rely=.4, anchor=E) # eye button location
        # Sign Up Button
        if Smart.studentLogIn_called:
            Button(self.box, width=35, pady=7, text='Student Sign Up', bg='black', fg='white', border=0, cursor='hand2', command=self.addStudent).pack(pady=30) # Sign Up Button to add to the database
        elif Smart.teacherLogIn_called:
            Button(self.box, width=35, pady=7, text='Teacher Sign Up', bg='black', fg='white', border=0, cursor='hand2', command=self.addTeacher).pack(pady=30) # Sign Up Button to add to the database
    # Student add account
    def addStudent(self):
        fullname = self.fullname_sign.get()
        username = self.username_sign.get()
        password = self.password_sign.get()
        userAcc = smartDatabase.checkStudentAcc(username)
        if userAcc:
            messagebox.showerror("Invalid Input!", "USERNAME ALREADY EXIST")
            self.window.deiconify()
        elif not username or not password or not fullname:
            messagebox.showerror("Invalid Input!", "Please enter valid credentials")
            self.window.deiconify()
        elif len(username) > 12 or len(fullname) > 12: # Check if username or full name is more than 12 characters
            messagebox.showerror("Invalid Input!", "YOUR USERNAME OR FULL NAME CAN'T BE MORE THAN 12 CHARACTERS!")
            self.window.deiconify()
        else: # lalabas pag clinick sign up
            if messagebox.askyesno('Confirmation', 'Are you sure you want to sign up this account?'):
                smartDatabase.addNewStudent(username, password, fullname)
                messagebox.showinfo('Sign Up', f"Account {username} has signed up succesfully!")
                self.window.destroy()
            else:
                messagebox.showerror('Cancelled', 'SIGN UP FAILED!')
                self.window.deiconify()
    # Teacher add account
    def addTeacher(self):
        username = self.username_sign.get()
        password = self.password_sign.get()
        fullname = self.fullname_sign.get()
        userAcc = smartDatabase.checkTeacherAcc(username)
        if userAcc:
            messagebox.showinfo("Invalid Input!", "USERNAME ALREADY EXIST")
            self.window.deiconify()
        elif not username or not password or not fullname:
            messagebox.showerror("Invalid Input!", "Please enter valid credentials")
            self.window.deiconify()
            return
        elif len(username) > 12 or len(fullname) > 12: # Check if username or full name is more than 12 characters
            messagebox.showerror("Invalid Input!", "YOUR USERNAME OR FULL NAME CAN'T BE MORE THAN 12 CHARACTERS!")
            self.window.deiconify()
        else: # lalabas pag clinick sign up
            if messagebox.askyesno('Confirmation', 'Are you sure you want to sign up this account?'):
                smartDatabase.addNewTeacher(username, password, fullname)
                messagebox.showinfo('Sign Up', f"Account {username} has signed up succesfully!")
                self.window.destroy()
            else:
                messagebox.showerror('Cancelled', 'SIGN UP FAILED!')
                self.window.deiconify()
    # Eye Icon or show password
    def show(self):
        self.showBtn.config(image=self.open_img,bd=0,bg='#B391B5',activebackground='#B391B5',cursor='hand2', command=self.hide)
        self.password_sign.config(show='')
    def hide(self):
        self.showBtn.config(image=self.close_img,bd=0,bg='#B391B5',activebackground='#B391B5',cursor='hand2', command=self.show)
        self.password_sign.config(show='*')

# Student Dashboard Window
class studentDashboard():
    def __init__(self, window, userData):
        self.window = window
        self.window.title("Student Dashboard")
        self.window.geometry("1430x700+50+50")
        self.window.config(bg="#481054")
        self.window.resizable(0, 0)
        # Fetch the data of the username that sucesfully log in
        self.userData = userData
        # Background Image
        self.bgphoto = PhotoImage(file='student_bg.png') # background image
        background = Label(self.window, image=self.bgphoto, bg='#A786EF')
        background.place(x=0, y=0, relwidth=1, relheight=1)# background picture location
        # Update Time
        def update_time():
            time_label.config(text=strftime("%I:%M:%S %p"))
            date_label.config(text=strftime("%m/%d/%Y"))
            self.after_id = self.window.after(1000, update_time) # Update every 1 second
        # Header Frame
        header_frame = Frame(self.window, bg="#741687", height=50)
        header_frame.pack(fill="x")
        # Logo (Placeholder)
        logo_label = Label(header_frame, text="🧑‍🏫📘", bg="#741687", fg="white", font=("Arial",28))
        logo_label.pack(side="left", padx=10, pady=5)
        logo_label = Label(header_frame, text="🧑‍🏫📘", bg="#741687", fg="white", font=("Arial",28))
        logo_label.pack(side="right", padx=10, pady=5)
        # Title
        title_label = Label(header_frame, text="Student Dashboard", bg="#741687", fg="white", font=("Arial",30, "bold"))
        title_label.pack(pady=5)
        # Footer Frame
        footer_frame = Frame(self.window, bg="#BE90D4", height=30)
        footer_frame.pack(fill="x")
        # Welcome Text
        welcome_label = Label(footer_frame, text=f"Welcome: {self.userData[3]}", bg="#BE90D4", font=("Arial", 10))
        welcome_label.pack(side="left", padx=(560, 10))
        # Date
        date_label = Label(footer_frame, bg="#BE90D4", font=("Arial", 10))
        date_label.pack(side="left", padx=10)
        # Time
        time_label = Label(footer_frame, text="Time: --:--:--", bg="#BE90D4", font=("Arial", 10))
        time_label.pack(side="left", padx=10)
        # Start the time update loop
        update_time()
        # Frame for buttons (placed on the left side)
        self.button_frame = Frame(self.window, bg="#59175E")
        self.button_frame.pack(side=LEFT, padx=30)
        # Logo Image
        self.logo_img = PhotoImage(file='logoteacher1.png')
        Label(self.button_frame, image=self.logo_img, bg='#59175E').pack()
        # Full name
        Label(self.button_frame, text=self.userData[1], font='Arial 14 bold', bg='#df4bf7', fg="white", width=10, padx=3, pady=3).pack()
        # Add styled buttons
        self.btn1 = Button(self.button_frame, text="Home", font="Arial 12", bg="#BE90D4", fg="white", width=20, height=2, padx=3, pady=3, cursor='hand2', command=self.homeDash)
        self.btn2 = Button(self.button_frame, text="Create a Review", font="Arial 12", bg="#b65ecc", fg="white", width=20, height=2, padx=3, pady=3, cursor='hand2', command=self.makeReview)
        self.btn3 = Button(self.button_frame, text="Take Assessment", font="Arial 12", bg="#8E44AD", fg="white", width=20, height=2, padx=3, pady=3, cursor='hand2', command=self.takeAssessment)
        self.btn4 = Button(self.button_frame, text="View Score and Feedback", font="Arial 12", bg="#8E44AD", fg="white", width=20, height=2, padx=3, pady=3, cursor='hand2', command=self.viewScore)
        self.btn5 = Button(self.button_frame, text="Log Out", font="Arial 12", bg="#8E44AD", fg="white", width=20, height=2, padx=3, pady=3, cursor='hand2', command=self.logOut)
        # Arrange buttons in the button frame (vertically)
        self.btn5.pack(padx=10, pady=10, side=BOTTOM)
        self.btn4.pack(padx=10, pady=10, side=BOTTOM)
        self.btn3.pack(padx=10, pady=10, side=BOTTOM)
        self.btn2.pack(padx=10, pady=10, side=BOTTOM)
        self.btn1.pack(padx=10, pady=10, side=BOTTOM)
        #Main Label Frames
        self.mFrame = Frame(self.window, bg='#ca64fb', bd=6, relief=RIDGE)
        self.mFrame.pack(side=LEFT, padx=20, pady=20, fill=BOTH, expand=True)
        # Call home function first
        self.homeDash()
    # destroy all widget
    def destroy(self):
        for widget in self.mFrame.winfo_children():
            widget.destroy()
    # ======================================================================= HOME PAGE =======================================================================
    def homeDash(self):
        self.destroy()
        self.studentbg = PhotoImage(file='student_bg.png') # Student home
        self.studenthome = Label(self.mFrame, image=self.studentbg, bg='#A786EF')
        self.studenthome.pack()
    # ======================================================================= CREATE A REVIEW =======================================================================
    def makeReview(self):
        self.destroy()
        # Clear input after adding a quiz to the database
        def clearInput():
            self.questionEntry.delete(0, END)
            self.optionA.delete(0, END)
            self.optionB.delete(0, END)
            self.optionC.delete(0, END)
            self.optionD.delete(0, END)
            self.answerEntry.delete(0, END)
        # Display Quiz
        def displayQuiz():
            flashcard = smartDatabase.displayFlashcard()
            for widget in self.displayScroll.winfo_children():
                widget.destroy()
            if flashcard:
                for index, row in enumerate(flashcard, start=1):
                    # New Frame for each questions
                    flashcardFrame = Frame(self.displayScroll, bd=4, relief=GROOVE, bg='#bb49cd', width=1040, height=130)
                    flashcardFrame.pack(fill=X, padx=20, pady=(20, 0))
                    flashcardFrame.propagate(0)
                    # Flashcard ID
                    flashcardID = Label(flashcardFrame, text=row[0], font='Arial 10 bold', bg='#bb49cd')
                    flashcardID.place(x=0, y=0)
                    # Student username who created the flashcrad
                    studentID = Label(flashcardFrame, text=f"Created by Student: {row[8]}", font='Arial 10 bold', bg='#bb49cd')
                    studentID.place(relx=.5, rely=0)
                    # Flashcard Subject
                    flashcardSubject = Label(flashcardFrame, text=f"Subject: {row[1]}", font='Arial 16 bold', bg='#bb49cd')
                    flashcardSubject.place(relx=1, rely=0, anchor=NE)
                    # Questions
                    flashcardQuestion = Label(flashcardFrame, text=f"Question: {row[2]}", font='Arial 16 bold', bg='#bb49cd', wraplength=800)
                    flashcardQuestion.pack(padx=(15,0), pady=(5, 0), anchor=W)
                    # Options
                    optionsFrame = Frame(flashcardFrame, bg='#bb49cd')  # Sub-frame for options
                    optionsFrame.pack(fill=X, padx=10, pady=10)
                    FlashcardOptionA = Label(optionsFrame, text=f"A. {row[3]}", font='Arial 14', bg='#bb49cd')
                    FlashcardOptionB = Label(optionsFrame, text=f"B. {row[4]}", font='Arial 14', bg='#bb49cd')
                    FlashcardOptionC = Label(optionsFrame, text=f"C. {row[5]}", font='Arial 14', bg='#bb49cd')
                    FlashcardOptionD = Label(optionsFrame, text=f"D. {row[6]}", font='Arial 14', bg='#bb49cd')
                    FlashcardOptionA.grid(row=0, column=0, padx=20)
                    FlashcardOptionB.grid(row=0, column=1, padx=20)
                    FlashcardOptionC.grid(row=0, column=2, padx=20)
                    FlashcardOptionD.grid(row=0, column=3, padx=20)
                    # Correct Answer
                    FlashcardAnswer = Label(flashcardFrame, text=f"Answer: {row[7]}", font='Arial 14 bold', bg='#bb49cd')
                    FlashcardAnswer.pack(anchor=W, padx=10, pady=(0, 10))
                    # Buttons
                    FlashcardDel = Button(flashcardFrame, text='DELETE', relief=RAISED, bg='#df4bf7', cursor='hand2', font='Arial 10', 
                                        command=lambda flashcard_id=row[0]: removeFlashcard(flashcard_id))
                    FlashcardDel.place(relx=.93, rely=.95, anchor=SE)
                    FlashcardEdit = Button(flashcardFrame, text='EDIT', relief=RAISED, bg='#df4bf7', cursor='hand2', font='Arial 10',
                                        command=lambda flashcard_id=row[0]: editFlashcard(flashcard_id))
                    FlashcardEdit.place(relx=.98, rely=.95, anchor=SE)
            else:
                Label(self.displayScroll, text="FLASHCARD IS EMPTY!", bg='#df4bf7', font='Arial 20 bold').place(relx=.5, rely=.5, anchor=CENTER)
        # Add Flashcard
        def addFlashcard():
            question = self.questionEntry.get()
            optionA = self.optionA.get()
            optionB = self.optionB.get()
            optionC = self.optionC.get()
            optionD = self.optionD.get()
            answer = self.answerEntry.get()
            subject = self.chooseSubject.get()
            if not question or not optionA or not optionB or not optionC or not optionD or not answer:
                messagebox.showerror("Error", "All fields are required!")
                return
            elif answer not in [optionA, optionB, optionC, optionD]:
                messagebox.showerror("Error", "Answer Does not match the available options")
            else:
                if messagebox.askyesno('Confirmation', 'Are you sure you want to add this question?'):
                    smartDatabase.createFlashcard(self.userData[0], subject, question, optionA, optionB, optionC, optionD, answer)
                    clearInput()
                    displayQuiz()
                else:
                    messagebox.showerror('Cancelled', 'You failed to add quiz')
                    return
        # Remove flashcard
        def removeFlashcard(flashcard_id):
            if messagebox.askyesno('Confirmation','Are you sure you want to delete this flashcard?'):
                smartDatabase.deleteFlashcard(flashcard_id)
                messagebox.showinfo("Success!", "Succesfully deleted the flashcard")
                clearInput()
                self.addBtn.config(text='ADD QUIZ', command=addFlashcard)
                displayQuiz()
            else: messagebox.showwarning('Cancelled', 'FAILED TO REMOVE FLASHCARD')
        # Edit Flashcard
        def editFlashcard(flashcard_id):
            # Update flashcard
            def updateFlashcard():
                flashcard_id = flashcard[0][0]
                question = self.questionEntry.get()
                optionA = self.optionA.get()
                optionB = self.optionB.get()
                optionC = self.optionC.get()
                optionD = self.optionD.get()
                answer = self.answerEntry.get()
                subject = self.chooseSubject.get()
                if not question or not optionA or not optionB or not optionC or not optionD or not answer:
                    messagebox.showerror("Error", "All fields are required!")
                    return
                elif answer not in [optionA, optionB, optionC, optionD]:
                    messagebox.showerror("Error", "Answer Does not match the available options")
                else:
                    if messagebox.askyesno('Confirmation', 'Are you sure you want to update this flashcard?'):
                        smartDatabase.updateFlashcard(flashcard_id, subject, question, optionA, optionB, optionC, optionD, answer)
                        self.addBtn.config(text='ADD QUIZ', command=addFlashcard)
                        clearInput()
                        displayQuiz()
                    else:
                        messagebox.showerror('Cancelled', 'You failed to update quiz')
                        return
            if messagebox.askyesno('Confirmation','Are you sure you want to edit this flashcard?'):
                flashcard = smartDatabase.searchFlashcard(flashcard_id)
                for i, row in enumerate(flashcard):
                    # Delete Data in Input Fields
                    self.questionEntry.delete(0, END)
                    self.optionA.delete(0, END)
                    self.optionB.delete(0, END)
                    self.optionC.delete(0, END)
                    self.optionD.delete(0, END)
                    self.answerEntry.delete(0, END)
                    # Insert value from database
                    self.chooseSubject.delete(0, END)
                    self.questionEntry.insert(0, flashcard[0][3])
                    self.optionA.insert(0, flashcard[0][4])
                    self.optionB.insert(0, flashcard[0][5])
                    self.optionC.insert(0, flashcard[0][6])
                    self.optionD.insert(0, flashcard[0][7])
                    self.answerEntry.insert(0, flashcard[0][8])
                    self.addBtn.config(text='Update', command=updateFlashcard)
            else: messagebox.showwarning('Cancelled', 'FAILED TO EDIT FLASHCARD')
        # Questions Frame
        self.questionFrame = Frame(self.mFrame, bg='purple')
        self.questionFrame.pack(fill=BOTH)
        # Header Frame
        self.headerFrame = Frame(self.questionFrame, bg='purple')
        self.headerFrame.pack(fill=X)
        # Header Label
        self.headerLabel = Label(self.headerFrame, text='Create Flashcard', font='Arial 20 bold', bg='purple', fg='white')
        self.headerLabel.pack()
        # Question Frame
        self.inputFrame = Frame(self.questionFrame, bg='purple')
        self.inputFrame.pack(fill=X)
        Label(self.inputFrame, text='Question: ', font='Arial 12 bold', bg='purple', fg='white').pack(side=LEFT, padx=(30, 0), pady=10)
        self.questionEntry = Entry(self.inputFrame, width=75, font='Arial 16')
        self.questionEntry.pack(side=LEFT, padx=10, pady=10)
        # Options Frame
        self.optionFrame = Frame(self.questionFrame, bg='purple')
        self.optionFrame.pack(fill=X)
        Label(self.optionFrame, text='Options: ', font='Arial 12 bold', bg='purple', fg='white').pack(side=LEFT, padx=(30, 0), pady=10)
        self.optionA = Entry(self.optionFrame, width=14, font='Arial 16')
        self.optionB = Entry(self.optionFrame, width=14, font='Arial 16')
        self.optionC = Entry(self.optionFrame, width=14, font='Arial 16')
        self.optionD = Entry(self.optionFrame, width=14, font='Arial 16')
        self.optionA.pack(side=LEFT, padx=20, pady=10)
        self.optionB.pack(side=LEFT, padx=20, pady=10)
        self.optionC.pack(side=LEFT, padx=20, pady=10)
        self.optionD.pack(side=LEFT, padx=20, pady=10)
        # Answer Frame
        self.answerFrame = Frame(self.questionFrame, bg='purple')  # Corrected frame creation
        self.answerFrame.pack(fill=X)
        Label(self.answerFrame, text='Answer: ', font='Arial 12 bold', bg='purple', fg='white').pack(side=LEFT, padx=(30, 0), pady=10)
        self.answerEntry = Entry(self.answerFrame, font='Arial 16', width=32)
        self.answerEntry.pack(side=LEFT, padx=20, pady=10)
        # Choose Subject
        Label(self.answerFrame, text='Choose Subject: ', font='Arial 16 bold', bg='purple', fg='white').pack(side=LEFT, padx=20)
        self.chooseSubject = ttk.Combobox(self.answerFrame, font='Arial 16', width=11, state='readonly', cursor='hand2', values=["English", "Mathematics", "Science"])
        self.chooseSubject.pack(side=LEFT, padx=10)
        self.chooseSubject.current(0)
        # Add Button
        self.addBtn = Button(self.answerFrame, text="ADD QUIZ", width=10, cursor='hand2', bg="#df4bf7", fg="white", font="Arial 12", padx=10, pady=5, bd=3, relief=RAISED, command=addFlashcard)
        self.addBtn.pack(side=LEFT, padx=20, pady=10)
        # Display Quiz Frame
        self.displayQuiz = Frame(self.mFrame, bg='#bb49cd')
        self.displayQuiz.pack(fill=BOTH, expand=True)
        # Create canvas
        self.myCanvas = Canvas(self.displayQuiz, bg='#bb49cd')
        self.myCanvas.pack(side=LEFT, fill=BOTH, expand=True)
        # Create scrollbar
        self.scroll = Scrollbar(self.displayQuiz, orient=VERTICAL, command=self.myCanvas.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        # Frame
        self.myCanvas.configure(yscrollcommand=self.scroll.set)
        self.displayScroll = Frame(self.myCanvas, bg='#bb49cd')
        self.myCanvas.create_window((0, 0), window=self.displayScroll, anchor="nw")
        self.displayScroll.bind("<Configure>", lambda e: self.myCanvas.configure(scrollregion=self.myCanvas.bbox("all")))
        # Display quiz
        displayQuiz()
    # ======================================================================= TAKE ASSESSMENT =======================================================================
    def takeAssessment(self):
        self.destroy()
        self.mFrame.config(bg='#9f149f')
        student_id = self.userData[0]
        # self.count = smartDatabase.count()
        # print(self.count)
        # Button creation utility
        def create_button(text, command):
            return Button(self.mFrame, text=text, font="Arial 20 bold", width=20, bg="#bb49cd", bd=5, cursor='hand2', 
                        relief=RAISED, command=command).pack(pady=20)
        # Flashcard Option
        def flashcard():
            self.destroy()
            Label(self.mFrame, text="Choose a Subject", bg='#9f149f', font='Arial 30 bold').pack(pady=30)
            create_button("English", englishFlash)
            create_button("Mathematics", mathFlash)
            create_button("Science", scienceFlash)
            create_button("RETURN", self.takeAssessment)
        # Assessment Option
        def teachAssess():
            self.destroy()
            Label(self.mFrame, text="Choose a Subject", bg='#9f149f', font='Arial 30 bold').pack(pady=30)
            create_button("English", englishAssessment)
            create_button("Mathematics", mathAssessment)
            create_button("Science", scienceAssessment)
            create_button("RETURN", self.takeAssessment)
        # Flashcard Questions
        def flashcardQuestion(subject):
            self.destroy()
            flashcard = smartDatabase.displayFlashcardSubject(subject)
            question = 0
            timer_duration = 30
            selected_answer = StringVar()
            selected_answers = []
            # Display Question
            def displayQuestion():
                self.destroy()
                if flashcard:
                    # Top Frame for Timer
                    topFrame = Frame(self.mFrame, bg='#bb49cd')
                    topFrame.pack(fill=X)
                    timer_label = Label(topFrame, font='Arial 12', text='Timer', bg='#bb49cd')
                    timer_label.pack(pady=10)
                    def update_timer():
                        nonlocal timer_duration
                        if timer_duration > 0  and timer_label.winfo_exists():
                            timer_duration -= 1
                            timer_label.config(text=f'Time left: {timer_duration}s')
                            self.mFrame.after(1000, update_timer)
                        elif timer_duration == 0:
                            submitAns()  # Automatically proceed when timer reaches 0
                    update_timer()
                    # Question Frame
                    questionFrame = Frame(self.mFrame, bg='#e08cee', bd=5, relief=GROOVE)
                    questionFrame.pack(side=LEFT, fill=BOTH, padx=60, pady=50)
                    # Questions
                    Label(questionFrame, bg='#e08cee', padx=200).pack() # make frame fixed width
                    questionLabel = Label(questionFrame, text=flashcard[question][3], font='Arial 24 bold', bg='#e08cee', wraplength=300)
                    questionLabel.pack(expand=True)
                    # Answer Frame
                    answerFrame = Frame(self.mFrame, bg='#e08cee', bd=5, relief=GROOVE)
                    answerFrame.pack(side=LEFT, fill=BOTH, padx=60, pady=50)
                    # Option label
                    options = flashcard[question][4:8]
                    for option in options:
                        Radiobutton(answerFrame, text=option, value=option, variable=selected_answer, font='Arial 16', bg='#e08cee',
                                    width=20, wraplength=300, cursor='hand2').pack(pady=20)
                    # Submit Button
                    submitBtn = Button(answerFrame, text='Submit', font='Arial 14', bg='#df4bf7', bd=3, cursor='hand2', relief=RAISED, command=submitAns)
                    submitBtn.pack(side=BOTTOM, padx=150, pady=(0, 20))
                    # Return Button
                    Button(topFrame, text="RETURN", font="Arial 12", width=10, bg="#df4bf7", bd=3, cursor='hand2', 
                        relief=RAISED, command=self.takeAssessment).place(relx=.99, rely=.5, anchor=E)
                else: Label(self.mFrame, text="NO QUESTIONS FOUND", font="Arial 32 bold", bg='#9f149f').pack(expand=True)
            # Submit Answer
            def submitAns():
                nonlocal question, timer_duration
                # Record the student's selected answer in the database
                selected_option = selected_answer.get()
                selected_answers.append(selected_option) 
                question += 1
                if question < len(flashcard):
                    timer_duration = 30  # Reset timer for the next question
                    displayQuestion()
                else:
                    score()
            # Record Score
            def score():
                correct_answer = 0
                for i, selected_option in enumerate(selected_answers):
                    if selected_option == flashcard[i][8]:  # Compare selected answer with correct answer
                        correct_answer += 1
                self.destroy()
                Label(self.mFrame, text=f"Congrats! You Scored {correct_answer} / {question}", font="Arial 32 bold", bg='#9f149f').pack(expand=True)
                create_button("RETURN", self.takeAssessment)
            # Display Questions
            displayQuestion()
        # Flashcard English
        def englishFlash():
            flashcardQuestion("English")
        # Flashcard Math
        def mathFlash():
            flashcardQuestion("Mathematics")
        # Flashcard Science
        def scienceFlash():
            flashcardQuestion("Science")
        # Assessment Questions
        def AssessmentQuestion(subject):
            self.destroy()
            assessment = smartDatabase.displayAssessment(subject)
            score = smartDatabase.displayScore()
            question = 0
            selected_answer = StringVar()
            timer_duration = 30
            selected_answers = []
            # Display Question
            def displayQuestion():
                nonlocal question
                self.destroy()
                # Top Frame for Timer
                topFrame = Frame(self.mFrame, bg='#bb49cd')
                topFrame.pack(fill=X)
                timer_label = Label(topFrame, font='Arial 12', text='Timer', bg='#bb49cd')
                timer_label.pack(pady=10)

                def update_timer():
                    nonlocal timer_duration
                    if timer_duration > 0  and timer_label.winfo_exists():
                        timer_duration -= 1
                        timer_label.config(text=f'Time left: {timer_duration}s')
                        self.mFrame.after(1000, update_timer)
                    elif timer_duration == 0:
                        submitAns()  # Automatically proceed when timer reaches 0
                update_timer()
                # Question Frame
                questionFrame = Frame(self.mFrame, bg='#e08cee', bd=5, relief=GROOVE)
                questionFrame.pack(side=LEFT, fill=BOTH, padx=60, pady=50)
                # Questions
                Label(questionFrame, bg='#e08cee', padx=200).pack() # make frame fixed width
                questionLabel = Label(questionFrame, text=assessment[question][2], font='Arial 24 bold', bg='#e08cee', wraplength=300)
                questionLabel.pack(expand=True)
                # Answer Frame
                answerFrame = Frame(self.mFrame, bg='#e08cee', bd=5, relief=GROOVE)
                answerFrame.pack(side=LEFT, fill=BOTH, padx=60, pady=50)
                # Option label
                options = assessment[question][3:7]
                for option in options:
                    Radiobutton(answerFrame, text=option, value=option, variable=selected_answer, font='Arial 16', bg='#e08cee',
                                width=20, wraplength=300, cursor='hand2').pack(pady=20)
                # Submit Button
                submitBtn = Button(answerFrame, text='Submit', font='Arial 14', bg='#df4bf7', bd=3, cursor='hand2', relief=RAISED, command=submitAns)
                submitBtn.pack(side=BOTTOM, padx=150, pady=(0, 20))
                # Return Button
                Button(topFrame, text="RETURN", font="Arial 12", width=10, bg="#df4bf7", bd=3, cursor='hand2', 
                    relief=RAISED, command=self.takeAssessment).place(relx=.99, rely=.5, anchor=E)
            # Submit Answer
            def submitAns():
                nonlocal question, timer_duration
                # Record the student's selected answer in the database
                selected_option = selected_answer.get()
                selected_answers.append(selected_option) 
                question += 1
                if question < len(assessment):
                    timer_duration = 30  # Reset timer for the next question
                    displayQuestion()
                else:
                    score()
            # Record Score
            def score():
                correct_answer = 0
                attempt_number = attempt[0][1] if attempt else 0
                # Check if every selection answer is correct
                for i, selected_option in enumerate(selected_answers):
                    if selected_option == assessment[i][7]:  # Compare selected answer with correct answer
                        correct_answer += 1 
                if attempt:
                    attempt_number += 1
                    smartDatabase.updateScore(self.userData[0], assessment[0][0], correct_answer, attempt_number)
                else:
                    attempt_number = 1
                    smartDatabase.studentScore(self.userData[0], assessment[0][0], assessment[0][9], attempt_number, correct_answer)
                self.destroy()
                Label(self.mFrame, text=f"Congrats! You Scored {correct_answer} / {question}", font="Arial 32 bold", bg='#9f149f').pack(expand=True)
                create_button("RETURN", self.takeAssessment)
            # Check if assessment exists
            if assessment:
                attempt = smartDatabase.checkAttempt(student_id, assessment[0][0])

                if attempt: 
                    Label(self.mFrame, text='You already attempted this assessment', font='Arial 16 bold', bg='#bb49cd').pack(expand=True)
                    create_button("RE ATTEMPT", displayQuestion)
                else: 
                    displayQuestion()
            else:
                Label(self.mFrame, text="NO QUESTIONS FOUND", font="Arial 32 bold", bg='#9f149f').pack(expand=True)
                create_button("RETURN", self.takeAssessment)
            # Display Questions
            # displayQuestion()
            # Flashcard English
        # Assessment English
        def englishAssessment():
            AssessmentQuestion("English")
        # Assessment Math
        def mathAssessment():
            AssessmentQuestion("Mathematics")
        # Assessment Science
        def scienceAssessment():
            AssessmentQuestion("Science")
        # Flashcard Button
        self.flashcardBtn = Button(self.mFrame, bg='#bb49cd', width=50, height=20, bd=3, cursor='hand2', relief=RAISED, command=flashcard)
        self.flashcardBtn.pack(side=LEFT, padx=(120, 0))
        # Teacher Assessment Button
        self.teacherAssessmentBtn = Button(self.mFrame, bg='#bb49cd', width=50, height=20, bd=3, cursor='hand2', relief=RAISED, command=teachAssess)
        self.teacherAssessmentBtn.pack(side=LEFT, padx=(120, 0))
        # Label
        Label(self.mFrame, text="Flashcard", bg='#e08cee', font="Times 20", padx=5, bd=3, relief=RIDGE).place(relx=.28, rely=.83, anchor=CENTER)
        Label(self.mFrame, text="Teacher Assessment", bg='#e08cee', font="Times 20", padx=5, bd=3, relief=RIDGE).place(relx=.74, rely=.83, anchor=CENTER)
    # ======================================================================= VIEW SCORE =======================================================================
    def viewScore(self):
        self.destroy()
        self.mFrame.config(bg='#740074')
        viewStats = smartDatabase.studentView(self.userData[0])
        # Header Frame
        self.scoreHeader = Frame(self.mFrame, bg='#740074')
        self.scoreHeader.pack(fill=X)
        Label(self.scoreHeader, font='Arial 32 bold', text='VIEW ASSESMENT', bg='#740074').pack(pady=(0, 20))
        # Frame for table
        self.tableFrame = Frame(self.mFrame)
        self.tableFrame.pack(fill=BOTH)
        # Table for viewing scores and feedback
        self.table = ttk.Treeview(self.tableFrame, columns=('ID', 'Name', 'Subject', 'Score', 'Attempt', 'Feedback'), show='headings')
        self.table.heading('ID', text='Student ID')
        self.table.heading('Name', text='Full Name')
        self.table.heading('Subject', text='Subject')
        self.table.heading('Score', text='Score')
        self.table.heading('Attempt', text='Attempt Nummber')
        self.table.heading('Feedback', text='Feedback')

        self.table.column('ID', width=100)
        self.table.column('Name', width=200)
        self.table.column('Subject', width=150)
        self.table.column('Score', width=100)
        self.table.column('Attempt', width=200)
        self.table.column('Feedback', width=200)

        for row in viewStats:
            self.table.insert('', END, values=row)

        self.table.pack(fill=X)
    # ======================================================================= LOG OUT =======================================================================
    def logOut(self):
        if messagebox.askyesno('Confirmation', 'Are you sure you want to log Out?'):
            self.window.after_cancel(self.after_id)
            self.window.destroy()
            logIn_window = Tk()
            logIn(logIn_window)
            logIn_window.mainloop()
        else:
            messagebox.showwarning('Cancelled', 'Log Out Failed')
            self.window.deiconify()
            return

# Teacher Dashboard Window
class teacherDashboard():# 
    def __init__(self, window, userData):
        self.window = window
        self.window.title("Student Mastery Assessment and Review Tool")
        self.window.geometry("1430x700+50+50")
        self.window.config(bg="#481054")
        self.window.resizable(0, 0)
        # Fetch the data of the username that sucesfully log in
        self.userData = userData
        # background photo
        self.bgphoto = PhotoImage(file='teacher_bg.png') # background image
        background = Label(self.window, image=self.bgphoto, bg='#A786EF')
        background.place(x=0, y=0, relwidth=1, relheight=1)# background picture location
        # Update Time
        def update_time():
            time_label.config(text=strftime("%I:%M:%S %p"))
            date_label.config(text=strftime("%m/%d/%Y"))
            self.after_id = self.window.after(1000, update_time) # Update every 1 second
        # Header Frame
        header_frame = Frame(self.window, bg="#741687", height=50)
        header_frame.pack(fill="x")
        # Logo (Placeholder)
        logo_label = Label(header_frame, text="🧑‍🏫📘", bg="#741687", fg="white", font=("Arial",28))
        logo_label.pack(side="left", padx=10, pady=5)
        logo_label = Label(header_frame, text="🧑‍🏫📘", bg="#741687", fg="white", font=("Arial",28))  
        logo_label.pack(side="right", padx=10, pady=5)
        # Title
        title_label = Label(header_frame, text="Teacher Dashboard", bg="#741687", fg="white", font=("Arial",30, "bold"))
        title_label.pack(pady=5)
        # Footer Frame
        footer_frame = Frame(self.window, bg="#BE90D4", height=30)
        footer_frame.pack(fill="x")
        # Welcome Text
        welcome_label = Label(footer_frame, text=f"Welcome: {self.userData[3]}", bg="#BE90D4", font=("Arial", 10))
        welcome_label.pack(side="left", padx=(560, 10))
        # Date
        date_label = Label(footer_frame, bg="#BE90D4", font=("Arial", 10))
        date_label.pack(side="left", padx=10)
        # Time
        time_label = Label(footer_frame, text="Time: --:--:--", bg="#BE90D4", font=("Arial", 10))
        time_label.pack(side="left", padx=10)
        # Start the time update loop
        update_time()
        # Frame for buttons (placed on the left side)
        self.button_frame = Frame(self.window, bg="#59175E")
        self.button_frame.pack(side=LEFT, padx=30)
        # Logo Image
        self.logo_img = PhotoImage(file='logoteacher1.png')
        Label(self.button_frame, image=self.logo_img, bg='#59175E').pack()
        #Main Label Frames
        self.mFrame = Frame(self.window, bg='#ca64fb', bd=6, relief=RIDGE)
        self.mFrame.pack(side=LEFT, padx=20, pady=20, fill=BOTH, expand=True)
        # Full name
        Label(self.button_frame, text=self.userData[1], font='Arial 14 bold', bg='#df4bf7', fg="white", width=10, padx=3, pady=3).pack()
        # Add styled buttons
        self.btn1 = Button(self.button_frame, text="Home", font="Arial 12", bg="#BE90D4", fg="white", width=20, height=2, padx=3, pady=3, command=self.homeDash)
        self.btn2 = Button(self.button_frame, text="Create Assessment", font="Arial 12", bg="#b65ecc", fg="white", width=20, height=2, padx=3, pady=3, command=self.createAssessment)
        self.btn3 = Button(self.button_frame, text="View Assessment", font="Arial 12", bg="#8E44AD", fg="white", width=20, height=2, padx=3, pady=3, command=self.viewAssessment)
        self.btn4 = Button(self.button_frame, text="View Score and Feedback", font="Arial 12", bg="#8E44AD", fg="white", width=20, height=2, padx=3, pady=3, command=self.viewScore)
        self.btn5 = Button(self.button_frame, text="Log Out", font="Arial 12", bg="#8E44AD", fg="white", width=20, height=2, padx=3, pady=3, command=self.logOut)
        # Arrange buttons in the button frame (vertically)
        self.btn5.pack(padx=10, pady=10, side=BOTTOM)
        self.btn4.pack(padx=10, pady=10, side=BOTTOM)
        self.btn3.pack(padx=10, pady=10, side=BOTTOM)
        self.btn2.pack(padx=10, pady=10, side=BOTTOM)
        self.btn1.pack(padx=10, pady=10, side=BOTTOM)
        # Call home page first
        self.homeDash()
    # Destroy every widgegt in main frame
    def destroy(self):
        for widget in self.mFrame.winfo_children():
            widget.destroy()
    # ======================================================================= HOME PAGE  =======================================================================
    def homeDash(self):
        self.destroy()
        self.teacherbg = PhotoImage(file='Teacherbg.png') # Student home
        self.teacherHome = Label(self.mFrame, image=self.teacherbg, bg='#A786EF')
        self.teacherHome.pack()
    # ======================================================================= CREATE ASSESSMENT =======================================================================
    def createAssessment(self):
        self.destroy()
        self.mFrame.config(bg='#b24bb2')
        # Clear input after adding a quiz to the database
        def clearInput():
            self.questionEntry.delete(0, END)
            self.optionA.delete(0, END)
            self.optionB.delete(0, END)
            self.optionC.delete(0, END)
            self.optionD.delete(0, END)
            self.answerEntry.delete(0, END)
        # Add math question to database
        def createQuestion(subject):
            def addMath():
                question = self.questionEntry.get()
                optionA = self.optionA.get()
                optionB = self.optionB.get()
                optionC = self.optionC.get()
                optionD = self.optionD.get()
                answer = self.answerEntry.get()
                if not subject or not question or not optionA or not optionB or not optionC or not optionD or not answer:
                    messagebox.showerror("Error", "All fields are required!")
                    return
                elif answer not in [optionA, optionB, optionC, optionD]:
                    messagebox.showerror("Error", "Answer Does not match the available options")
                else:
                    if messagebox.askyesno('Confirmation', f"Are you sure you want to add this {subject} question?'"):
                        smartDatabase.createAssessment(self.userData[0], subject, question, optionA, optionB, optionC, optionD, answer)
                        clearInput()
                    else:
                        messagebox.showerror('Cancelled', 'You failed to add quiz')
                        return
            self.headerLabel.config(text=f"Create {subject} Assessment")
            self.addBtn.config(command=addMath)
        # English
        def english():
            createQuestion("English")
        def math():
            createQuestion("Mathematics")
        def science():
            createQuestion("Science")
        # Button getting clicked 
        def chooseFirst():
            messagebox.showerror("Invalid Input", "CHOOSE A SUBJECT FIRST!\n\nENGLISH\n\nMATH\n\nSCIENCE")
        # Buttons
        self.buttonFrame = Frame(self.mFrame, bg='#b24bb2')
        self.buttonFrame.pack(fill=X, pady=(0, 30))
        Label(self.buttonFrame, font='Arial 32 bold', text='CHOOSE SUBJECT', bg='#b24bb2').pack(pady=(0, 20))
        Button(self.buttonFrame, font='Arial 14', text='English', width=20, cursor='hand2', bg='#b24bb2', command=english).pack(side=LEFT, padx=60)
        Button(self.buttonFrame, font='Arial 14', text='Mathematics', width=20, cursor='hand2', bg='#b24bb2', command=math).pack(side=LEFT, padx=60)
        Button(self.buttonFrame, font='Arial 14', text='Science', width=20, cursor='hand2', bg='#b24bb2', command=science).pack(side=LEFT, padx=60)
        # Questions Frame
        self.questionFrame = Frame(self.mFrame, bg='purple')
        self.questionFrame.pack(fill=BOTH, expand=True)  # Ensure it fills and expands properly
        # Header Frame
        self.headerFrame = Frame(self.questionFrame, bg='purple', pady=10)
        self.headerFrame.pack(fill=X)
        # Header Label
        self.headerLabel = Label(self.headerFrame, text='Create Assessment', font='Arial 20 bold', bg='purple', fg='white')
        self.headerLabel.pack(side=LEFT, padx=(300, 0))
        # Question Frame
        self.inputFrame = Frame(self.questionFrame, bg='purple')
        self.inputFrame.pack(fill=X)
        Label(self.inputFrame, text='Question: ', font='Arial 12 bold', bg='purple', fg='white').pack(side=LEFT, padx=(30, 0), pady=20)
        self.questionEntry = Entry(self.inputFrame, width=75, font='Arial 16')
        self.questionEntry.pack(side=LEFT, padx=10, pady=20)
        # Options Frame
        self.optionFrame = Frame(self.questionFrame, bg='purple')
        self.optionFrame.pack(fill=X)
        Label(self.optionFrame, text='Options: ', font='Arial 12 bold', bg='purple', fg='white').pack(side=LEFT, padx=(30, 0), pady=20)
        self.optionA = Entry(self.optionFrame, width=14, font='Arial 16')
        self.optionB = Entry(self.optionFrame, width=14, font='Arial 16')
        self.optionC = Entry(self.optionFrame, width=14, font='Arial 16')
        self.optionD = Entry(self.optionFrame, width=14, font='Arial 16')
        self.optionA.pack(side=LEFT, padx=20, pady=20)
        self.optionB.pack(side=LEFT, padx=20, pady=20)
        self.optionC.pack(side=LEFT, padx=20, pady=20)
        self.optionD.pack(side=LEFT, padx=20, pady=20)
        # Answer Frame
        self.answerFrame = Frame(self.questionFrame, bg='purple')  # Corrected frame creation
        self.answerFrame.pack(fill=X)
        Label(self.answerFrame, text='Answer: ', font='Arial 12 bold', bg='purple', fg='white').pack(side=LEFT, padx=(30, 0), pady=20)
        self.answerEntry = Entry(self.answerFrame, font='Arial 16', width=30)
        self.answerEntry.pack(side=LEFT, padx=20, pady=20)
        # Add Button
        self.addBtn = Button(self.answerFrame, text="ADD QUIZ", width=10, bg="#4682b4", fg="white", font=("Arial", 12), padx=10, pady=5, cursor='hand2', relief=RAISED, command=chooseFirst)
        self.addBtn.pack(side=RIGHT, padx=20, pady=20)
    # ======================================================================= VIEW ASSESSMENT =======================================================================
    def viewAssessment(self):
        self.destroy()
        self.mFrame.config(bg='#b24bb2')
        # Remove Assessment
        def removeAssessment(assessment_id):
            if messagebox.askyesno('Confirmation','Are you sure you want to delete this Assessment?'):
                smartDatabase.deleteAssessment(assessment_id)
                messagebox.showinfo("Success!", "Succesfully deleted the Assessment")
                self.viewAssessment()
            else: messagebox.showwarning('Cancelled', 'FAILED TO REMOVE ASSESSMENT')
        # Edit Assessment
        def editAssessment(assessment_id):
            if messagebox.askyesno('Confirmation','Are you sure you want to edit this Assessment?'):
                self.editWindow = Toplevel(self.window)
                self.app = Assessment(self.editWindow, assessment_id)
            else: messagebox.showwarning('Cancelled', 'FAILED TO EDIT ASSESSMENT')
        # View Assessment
        def viewAssessment(subject):
            self.viewHeading.config(text=f"View {subject} Assessment")
            for widget in self.questionScroll.winfo_children():
                widget.destroy()
            quiz = smartDatabase.displayAssessment(subject)
            if quiz:
                for index, row in enumerate(quiz, start=1):
                    # New Frame for each questions
                    assessmentFrame = Frame(self.questionScroll, bd=4, relief=GROOVE, bg='#bb49cd', width=1000, height=130)
                    assessmentFrame.pack(fill=X, padx=20, pady=(20, 0))
                    assessmentFrame.propagate(0)
                    # Assessment ID
                    assessmentID = Label(assessmentFrame, text=row[0], font='Arial 10 bold', bg='#bb49cd')
                    assessmentID.place(x=0, y=0)
                    # Teacher username who created the flashcrad
                    # studentID = Label(assessmentFrame, text=f"Created by Teacher: {row[8]}", font='Arial 10 bold', bg='#bb49cd')
                    # studentID.place(relx=1, rely=0, anchor=NE)
                    # Questions
                    assessmentQuestion = Label(assessmentFrame, text=f"Question: {row[2]}", font='Arial 16 bold', bg='#bb49cd', wraplength=800)
                    assessmentQuestion.pack(padx=(15,0), pady=(5, 0), anchor=W)
                    # Options
                    optionsFrame = Frame(assessmentFrame, bg='#bb49cd')  # Sub-frame for options
                    optionsFrame.pack(fill=X, padx=10, pady=10)
                    assessmentOptionA = Label(optionsFrame, text=f"A. {row[3]}", font='Arial 14', bg='#bb49cd')
                    assessmentOptionB = Label(optionsFrame, text=f"B. {row[4]}", font='Arial 14', bg='#bb49cd')
                    assessmentOptionC = Label(optionsFrame, text=f"C. {row[5]}", font='Arial 14', bg='#bb49cd')
                    assessmentOptionD = Label(optionsFrame, text=f"D. {row[6]}", font='Arial 14', bg='#bb49cd')
                    assessmentOptionA.grid(row=0, column=0, padx=20)
                    assessmentOptionB.grid(row=0, column=1, padx=20)
                    assessmentOptionC.grid(row=0, column=2, padx=20)
                    assessmentOptionD.grid(row=0, column=3, padx=20)
                    # Correct Answer
                    assessmentAnswer = Label(assessmentFrame, text=f"Answer: {row[7]}", font='Arial 14 bold', bg='#bb49cd')
                    assessmentAnswer.pack(anchor=W, padx=10, pady=(0, 10))
                    # Buttons
                    assessmentDel = Button(assessmentFrame, text='DELETE', relief=RAISED, bg='#df4bf7', cursor='hand2', font='Arial 10',
                                    command=lambda assessment_id=row[0]: removeAssessment(assessment_id))
                    assessmentDel.place(relx=.93, rely=.95, anchor=SE)
                    assessmentEdit = Button(assessmentFrame, text='EDIT', relief=RAISED, bg='#df4bf7', cursor='hand2', font='Arial 10',
                                    command=lambda assessment_id=row[0]: editAssessment(assessment_id))
                    assessmentEdit.place(relx=.98, rely=.95, anchor=SE)
            else:
                Label(self.questionScroll, text=f"{subject} SUBJECT IS EMPTY", bg='#bb49cd', font='Arial 32 bold').place(relx=.5, rely=.5, anchor=CENTER)
        def viewEnglish():
            viewAssessment("English")
        def viewMath():
            viewAssessment("Mathematics")
        def viewScience():
            viewAssessment("Science")
        # Headings
        self.buttonFrame = Frame(self.mFrame, bg='#b24bb2')
        self.buttonFrame.pack(fill=X, pady=(0, 30))
        self.viewHeading = Label(self.buttonFrame, font='Arial 32 bold', text='View Assessment', bg='#b24bb2')
        self.viewHeading.pack(pady=(0, 20))
        Button(self.buttonFrame, font='Arial 14', text='English', width=20, cursor='hand2', bg='#b24bb2', command=viewEnglish).pack(side=LEFT, padx=60)
        Button(self.buttonFrame, font='Arial 14', text='Mathematics', width=20, cursor='hand2', bg='#b24bb2', command=viewMath).pack(side=LEFT, padx=60)
        Button(self.buttonFrame, font='Arial 14', text='Science', width=20, cursor='hand2', bg='#b24bb2', command=viewScience).pack(side=LEFT, padx=60)
        # Questions Frame
        self.questionFrame = Frame(self.mFrame, bg='purple')
        self.questionFrame.pack(fill=BOTH, expand=True)  # Ensure it fills and expands properly
        # Create canvas
        self.myCanvas = Canvas(self.questionFrame, bg='purple')
        self.myCanvas.pack(side=LEFT, fill=BOTH, expand=True)
        # Create scrollbar
        self.scroll = Scrollbar(self.questionFrame, orient=VERTICAL, command=self.myCanvas.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        # Frame
        self.myCanvas.configure(yscrollcommand=self.scroll.set)
        self.questionScroll = Frame(self.myCanvas, bg='purple')
        self.myCanvas.create_window((0, 0), window=self.questionScroll, anchor="nw")
        self.questionScroll.bind("<Configure>", lambda e: self.myCanvas.configure(scrollregion=self.myCanvas.bbox("all")))
        # Label
        Label(self.questionScroll, text="Choose a subject to view assessment", bg='purple', font='Arial 32 bold').pack(padx=150, pady=150)
    # ======================================================================= VIEW SCORE =======================================================================
    def viewScore(self):
        self.destroy()
        self.mFrame.config(bg='#740074')
        # Edit feedback
        def editFeedback():
            selected_item = self.table.selection()
            # If user did not select in tree view
            if not selected_item:
                messagebox.showwarning("No Selection", "Please select a row to edit feedback.")
                return
            item = self.table.item(selected_item, 'values')
            # after pressing the button
            if messagebox.askyesno('Confirmation','Are you sure you want to edit this feedback?'):
                self.feedbackEntry.delete("1.0", END)
                self.feedbackEntry.insert("1.0", item[5])
                self.feedBtn.config(text="Update Feedback", command=updateFeedback)
            else:
                messagebox.showwarning('Cancelled', 'You choose not to edit the feedback')
        # Update feedback
        def updateFeedback():
            feedback = self.feedbackEntry.get("1.0", END).strip()
            if messagebox.askyesno('Confirmation','Are you sure you want to update this feedback?'):
                smartDatabase.updateFeedback(viewStats[0][0], self.userData[0], feedback)
                self.feedBtn.config(text="Edit Feedback", command=editFeedback)
                self.viewScore()
            else:
                messagebox.showwarning('Cancelled', 'You choose not to update the feedback')
        # fetch data from database
        viewStats = smartDatabase.TeachertView()
        # Header Frame
        self.scoreHeader = Frame(self.mFrame, bg='#740074')
        self.scoreHeader.pack(fill=X)
        Label(self.scoreHeader, font='Arial 32 bold', text='VIEW SCORE AND FEEDBACK', bg='#740074').pack(pady=(0, 20))
        # Frame for table
        self.tableFrame = Frame(self.mFrame)
        self.tableFrame.pack(fill=BOTH, expand=True)
        # Create a vertical scrollbar before using it in the Treeview
        self.scrollbar = Scrollbar(self.tableFrame, orient="vertical")
        # Table for viewing scores and feedback
        self.table = ttk.Treeview(self.tableFrame, columns=('ID', 'Name', 'Subject', 'Score', 'Attempt', 'Feedback'), show='headings', yscrollcommand=self.scrollbar.set)
        # Table Column Headers
        self.table.heading('ID', text='Student ID')
        self.table.heading('Name', text='Full Name')
        self.table.heading('Subject', text='Subject')
        self.table.heading('Score', text='Score')
        self.table.heading('Attempt', text='Attempts')
        self.table.heading('Feedback', text='Feedback')
        # Table Columns (Container for data in the database)
        self.table.column('ID', width=75, anchor=CENTER)
        self.table.column('Name', width=200, anchor=CENTER)
        self.table.column('Subject', width=150, anchor=CENTER)
        self.table.column('Score', width=50, anchor=CENTER)
        self.table.column('Attempt', width=50, anchor=CENTER)
        self.table.column('Feedback', width=300)
        # Pack the scrollbar
        self.scrollbar.config(command=self.table.yview) 
        self.scrollbar.pack(side=RIGHT, fill=Y)
        # Iterate all data in database and insert it in the table
        for row in viewStats:
            self.table.insert('', END, values=row)
        # Pack the Treeview widget
        self.table.pack(fill=BOTH, expand=True)
        # feedback button
        self.feedBtn = Button(self.mFrame, text="Edit Feedback", font="Arial 16 bold", width=20, bg="#df4bf7", bd=5, fg='white',
                    cursor='hand2', relief=RAISED, command=editFeedback)
        self.feedBtn.pack(pady=10)
        # Feedback frame
        self.feedback = Frame(self.mFrame, bg='#bb49cd')
        self.feedback.pack(fill=BOTH, expand=True, pady=10, padx=20)
        # Feedback entry
        self.feedbackEntry = Text(self.feedback, font='Arial 12')
        self.feedbackEntry.pack()
    # ======================================================================= LOG OUT =======================================================================
    def logOut(self):
        if messagebox.askyesno('Confirmation', 'Are you sure you want to log Out?'):
            self.window.after_cancel(self.after_id)
            self.window.destroy()
            logIn_window = Tk()
            logIn(logIn_window)
            logIn_window.mainloop()
        else:
            messagebox.showwarning('Cancelled', 'Log Out Failed')
            self.window.deiconify()
            return

# Edit Assessment
class Assessment():
    def __init__(self, window, assessment_id):
        self.window = window
        self.window.title("Assessmet")
        self.window.geometry("600x400+300+100")
        self.window.config(bg="#481054")
        self.window.resizable(0, 0)
        # Assessment Data
        self.assessmentData = smartDatabase.searchAssessment(assessment_id)
        # Labels
        self.title = Label(self.window, text='Editing Assessment', font='Arial 20 bold', bg='#481054', fg='white')
        self.question = Label(self.window, text='Question: ', font='Helvetica 14 bold', fg='white', bg='#481054')
        self.optionA = Label(self.window, text='Option A: ', font='Helvetica 14', fg='white', bg='#481054')
        self.optionB = Label(self.window, text='Option B: ', font='Helvetica 14', fg='white', bg='#481054')
        self.optionC = Label(self.window, text='Option C: ', font='Helvetica 14', fg='white', bg='#481054')
        self.optionD = Label(self.window, text='Option D: ', font='Helvetica 14', fg='white', bg='#481054')
        self.answer = Label(self.window, text='Answer: ', font='Helvetica 14 bold', fg='white', bg='#481054')
        self.subject = Label(self.window, text='Choose Subject: ', font='Helvetica 14 bold', fg='white', bg='#481054')
        # Label Placements
        self.title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.question.grid(row=1, column=0, sticky=W, padx=(30,0), pady=(10, 0))
        self.optionA.grid(row=2, column=0, sticky=W, padx=(30,0), pady=(10, 0))
        self.optionB.grid(row=3, column=0, sticky=W, padx=(30,0), pady=(10, 0))
        self.optionC.grid(row=4, column=0, sticky=W, padx=(30,0), pady=(10, 0))
        self.optionD.grid(row=5, column=0, sticky=W, padx=(30,0), pady=(10, 0))
        self.answer.grid(row=6, column=0, sticky=W, padx=(30,0), pady=(10, 0))
        self.subject.grid(row=7, column=0, sticky=W, padx=(30,0), pady=(10, 0))
        # Input fields
        self.questionInput = Entry(self.window, width=50, font='Helvetica 10')
        self.optionAInput = Entry(self.window, width=50, font='Helvetica 10')
        self.optionBInput = Entry(self.window, width=50, font='Helvetica 10')
        self.optionCInput = Entry(self.window, width=50, font='Helvetica 10')
        self.optionDInput = Entry(self.window, width=50, font='Helvetica 10')
        self.answerInput = Entry(self.window, width=50, font='Helvetica 10')
        self.chooseSubject = ttk.Combobox(self.window, width=11, state='readonly', values=["English", "Mathematics", "Science"], font='Helvetica 10')
        self.chooseSubject.current(0)
        # Input fields placemen
        self.questionInput.grid(row=1, column=1, pady=(10, 0))
        self.optionAInput.grid(row=2, column=1, pady=(10, 0))
        self.optionBInput.grid(row=3, column=1, pady=(10, 0))
        self.optionCInput.grid(row=4, column=1, pady=(10, 0))
        self.optionDInput.grid(row=5, column=1, pady=(10, 0))
        self.answerInput.grid(row=6, column=1, pady=(10, 0))
        self.chooseSubject.grid(row=7, column=1, pady=(10, 0))
        # Pre-fill the fields with existing values
        self.questionInput.insert(0, self.assessmentData[0][3])
        self.optionAInput.insert(0, self.assessmentData[0][4])
        self.optionBInput.insert(0, self.assessmentData[0][5])
        self.optionCInput.insert(0, self.assessmentData[0][6])
        self.optionDInput.insert(0, self.assessmentData[0][7])
        self.answerInput.insert(0, self.assessmentData[0][8])
        # Update Button
        self.editBtn = Button(self.window, text="Update Assessment", width=30, font='Helvetica 14', cursor='hand2', bd=3, relief=RAISED, command=self.edit)
        self.editBtn.grid(row=10, column=0, columnspan=2, pady=25)
    def edit(self):
        assessment_id = self.assessmentData[0][0]
        oldSubject = self.assessmentData[0][2]
        question = self.questionInput.get()
        optionA = self.optionAInput.get()
        optionB = self.optionBInput.get()
        optionC = self.optionCInput.get()
        optionD = self.optionDInput.get()
        answer = self.answerInput.get()
        subject = self.chooseSubject.get()
        if not question or not optionA or not optionB or not optionC or not optionD or not answer:
            messagebox.showerror("Error", "All fields are required!")
        elif answer not in [optionA, optionB, optionC, optionD]:
            messagebox.showerror("Error", "Answer Does not match the available options")
            self.window.deiconify()
        else:
            if messagebox.askyesno('Confirmation', f"Are you sure you want to update this {oldSubject} question?"):
                smartDatabase.updateAssessment(assessment_id, subject, question, optionA, optionB, optionC, optionD, answer)
                messagebox.showinfo("Success!", "Assessment edited Succesfully")
                self.window.destroy()
            else:
                messagebox.showerror('Cancelled', 'You failed to edit the assessment')
                self.window.deiconify()

window = Tk()
app = Smart(window)
window.mainloop()