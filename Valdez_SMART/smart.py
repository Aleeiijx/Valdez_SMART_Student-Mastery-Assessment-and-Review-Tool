from tkinter import *           # GUI / tkinter
from tkinter import messagebox  # messagebox
from tkinter import ttk         # combobox
from time import *              # time module
# import smartDatabase
import smartDatabase


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
        # Student Log In
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
        title = Label(self.window, text='I AM A', fg='black', bg='#B391B5', font=('Times New Roman', 50), bd=3, relief=RAISED, padx=10) # click bla bla text
        title.pack(pady=50) # click bla bla text location
        # Picture
        self.student = PhotoImage(file='student.png')
        self.teacher = PhotoImage(file='teacher.png')
        # Button fors Student and Teacher
        self.student_window = Button(self.window, image=self.student, command=studentLogIn, bd=4, bg="#B391B5", activebackground="#B391B5", cursor='hand2') # student button
        self.student_window.place(relx=0.5, rely=0.5, anchor=CENTER, x=-200) # student button lcoation
        self.teacher_window = Button(self.window, image=self.teacher, command=teacherLogIn, bd=4, bg="#B391B5", activebackground="#B391B5", cursor='hand2') # teacher button
        self.teacher_window.place(relx=0.5, rely=0.5, anchor=CENTER, x=200) # teacher button location
        # Label for Buttons
        self.student_text = Label(window, text='STUDENT', fg='black', bg='#B391B5', font=('Times New Roman', 40), bd=3, relief=RIDGE)
        self.student_text.place(relx=0.5, rely=0.81, anchor=CENTER, x=-200)
        self.teacher_text = Label(window, text='TEACHER', fg='black', bg='#B391B5', font=('Times New Roman', 40), bd=3, relief=RIDGE)
        self.teacher_text.place(relx=0.5, rely=0.81, anchor=CENTER, x=200)

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
        Frame(self.box, width=280, height=2, bg='black').place(x=30, y=109) # straight line under password
        # Password Code
        self.passcode = Entry(self.box, width=20, fg='black', border=0, bg='#B391B5', font=('Times New Roman', 20), show='*') # input fields for password
        self.passcode.place(x=30, y=155) # Password Location
        self.passcode.insert(0, 'Password') # Text Inside Password
        self.passcode.bind('<FocusIn>', lambda e: self.passcode.delete(0, 'end')) # pag clinick yung password ay mawawala sya
        self.passcode.bind('<FocusOut>', lambda e: self.passcode.insert(0, 'Password')) # pag hindi clinick ay ididisplay password
        Frame(self.box, width=280, height=2, bg='black').place(x=30, y=189) # straight line under password
        # Eye Image
        self.close_img = PhotoImage(file='close_eye.png') # image for close eye
        self.open_img = PhotoImage(file='open_eye.png') # image for open eye
        self.showBtn=Button(self.box,image=self.close_img,border=0,bg='#B391B5',activebackground='#B391B5',cursor='hand2',command=self.show) # Eye Button
        self.showBtn.place(x=270, y=160) # eye button location
        # Log in Button differs depending whether student or teacher
        if Smart.studentLogIn_called:
            Button(self.box, width=35, pady=7, text='Student Log In', bg='black', fg='white', border=0, cursor='hand2', command=self.studentLog).place(x=35, y=250) # Login Button
        elif Smart.teacherLogIn_called:
            Button(self.box, width=35, pady=7, text='Teacher Log In', bg='black', fg='white', border=0, cursor='hand2', command=self.teacherLog).place(x=35, y=250) # Login Button
        # Label Text Under Log in
        account = Label(self.box, text="Don't have an account yet?", fg='black', bg='#B391B5', font=('Times New Roman', 12)) # Don't have an account yet Label
        account.place(x=55, y=300) # location ng Don't have an account yet
        Button(self.box, width=35, pady=7, text='Back', bg='black', fg='white', border=0, cursor='hand2', command=self.backbtn).place(x=35, y=350) # Back button
        sign = Button(self.box, width=6, text='Sign Up', bg='black', fg='white', border=0, cursor='hand2', command=self.signup) # Sign Up Button
        sign.place(x=225, y=300) # sign up button location
    # Back Button to go back to chossing between student and teacher
    def backbtn(self):
        self.window.destroy()
        smart_window = Tk()
        Smart(smart_window)
        smart_window.mainloop()
    # Sign Up Window
    def signup(self):
        new_window = Toplevel(self.window)
        self.app = signUp(new_window)
    # Eye Button Function to reveal 
    def show(self):
        self.showBtn.config(image=self.open_img,bd=0,bg='#B391B5',activebackground='#B391B5',cursor='hand2', command=self.hide)
        self.passcode.config(show='')
    def hide(self):
        self.showBtn.config(image=self.close_img,bd=0,bg='#B391B5',activebackground='#B391B5',cursor='hand2', command=self.show)
        self.passcode.config(show='*')
    # student account
    def studentLog(self):
        username = self.user.get()
        password = self.passcode.get()
        if username == 'Username' or password == 'Password':
            messagebox.showerror("Invalid Input", "Please enter both username and password")
            return
        if smartDatabase.studentLog(username, password):
            messagebox.showinfo("Success!", "Log In Succesfully!")
            self.window.destroy()
            smart_window = Tk()
            studentDashboard(smart_window)
            smart_window.mainloop()
        else:
            # If login fails
            messagebox.showerror("Login Failed", "Invalid username or password")
    # teacher account
    def teacherLog(self):
        username = self.user.get()
        password = self.passcode.get()
        if username == 'Username' or password == 'Password':
            messagebox.showerror("Invalid Input", "Please enter both username and password")
            return
        if smartDatabase.teacherLog(username, password):
            messagebox.showinfo("Success!", "Log In Succesfully!")
            self.window.destroy()
            smart_window = Tk()
            teacherDashboard(smart_window)
            smart_window.mainloop()
        else:
            # If login fails
            messagebox.showerror("Login Failed", "Invalid username or password")

class signUp():
    def __init__(self, window):
        self.window = window
        self.window.title("Student Mastery Assessment and Review Tool")
        self.window.geometry("400x400+750+225")
        self.window.config(bg="#413B46")
        self.window.resizable(0, 0)
        # Student add account
        def updateStudent():
            fullname = self.fullname_sign.get()
            username = self.username_sign.get()
            password = self.password_sign.get()
            userAcc = smartDatabase.checkStudentAcc(username)
            if userAcc:
                messagebox.showerror("Invalid Input!", "ACCOUNT ALREADY EXIST")
                self.window.deiconify()
            if not username or not password or not fullname:
                messagebox.showerror("Invalid Input!", "Please enter valid credentials")
                self.window.deiconify()
            else:
                smartDatabase.addNewStudent(username, password, fullname)
                messagebox.showinfo('Sign Up', 'Signed Up Successfully') # lalabas pag clinick sign up
                self.window.destroy()
        # Teacher add account
        def updateTeacher():
            username = self.username_sign.get()
            password = self.password_sign.get()
            fullname = self.fullname_sign.get()
            userAcc = smartDatabase.checkTeacherAcc(username)
            if userAcc:
                messagebox.showinfo("Invalid Input!", "ACCOUNT ALREADY EXIST")
                self.window.deiconify()
            elif not username or not password or not fullname:
                messagebox.showerror("Invalid Input!", "Please enter valid credentials")
                self.window.deiconify()
                return
            else: 
                smartDatabase.teacherLog(username, password)
                smartDatabase.addNewTeacher(username, password, fullname)
                messagebox.showinfo('Sign Up', 'Signed Up Successfully') # lalabas pag clinick sign up
                self.window.destroy()
        # Purple Box
        self.box = Label(self.window, width=50, height=25, bg='#B391B5') # purple box
        self.box.place(relx=.5, rely=.5, relwidth=.9, relheight=.9, anchor=CENTER) # purple box location
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
        self.showBtn=Button(self.password_sign,image=self.open_img,border=0,bg='#B391B5',activebackground='#B391B5',cursor='hand2', command=self.show) # Eye Button
        self.showBtn.place(relx=.95, rely=.4, anchor=E) # eye button location
        # Sign Up Button
        if Smart.studentLogIn_called:
            Button(self.box, width=35, pady=7, text='Student Sign Up', bg='black', fg='white', border=0, cursor='hand2', command=updateStudent).pack(pady=30) # Sign Up Button to add to the database
        elif Smart.teacherLogIn_called:
            Button(self.box, width=35, pady=7, text='Teacher Sign Up', bg='black', fg='white', border=0, cursor='hand2', command=updateTeacher).pack(pady=30) # Sign Up Button to add to the database
    def show(self):
        self.showBtn.config(image=self.close_img,bd=0,bg='#B391B5',activebackground='#B391B5',cursor='hand2', command=self.hide)
        self.password_sign.config(show='')
    def hide(self):
        self.showBtn.config(image=self.open_img,bd=0,bg='#B391B5',activebackground='#B391B5',cursor='hand2', command=self.show)
        self.password_sign.config(show='*')

class studentDashboard():
    def __init__(self, window):
        self.window = window
        self.window.title("Student Dashboard")
        self.window.geometry("1430x700+50+50")
        self.window.config(bg="#481054")
        self.window.resizable(0, 0)

        self.bgphoto = PhotoImage(file='student_bg.png') # background image
        background = Label(self.window, image=self.bgphoto, bg='#A786EF')
        background.place(x=0, y=0, relwidth=1, relheight=1)# background picture location

        # Title label
        self.title_label = Label(self.window, text="Student Dashboard", font=("Arial Bold", 24), bg="#481054", fg="white")
        self.title_label.pack(pady=20)

        # Frame for buttons (placed on the left side)
        self.button_frame = Frame(self.window, bg="#481054")
        self.button_frame.place(relx=.02, rely=.53, relwidth=.15, relheight=.8, anchor=W)

        # Logo Image
        #self.logo_img = PhotoImage(file='logostudent.png')
        #Label(self.button_frame, image=self.logo_img).pack()

        # Main Label Frames
        self.mFrame = Frame(self.window, bg='red', bd=6, relief=RIDGE)
        self.mFrame.place(relx=.95, rely=.53, relwidth=.7, relheight=.75, anchor=E)
        # Add styled buttons
        self.btn1 = Button(self.button_frame, text="Home", font=("Arial", 14), bg="#BE90D4", fg="white", width=20, height=2, command=self.homeDash)
        self.btn2 = Button(self.button_frame, text="Make a Quiz", font=("Arial", 14), bg="#b65ecc", fg="white", width=20, height=2, command=self.makeQuiz)
        self.btn3 = Button(self.button_frame, text="Choose Subject", font=("Arial", 14), bg="#8E44AD", fg="white", width=20, height=2, command=self.chooseSubj)
        self.btn4 = Button(self.button_frame, text="View Score and Feedback", font=("Arial", 14), bg="#8E44AD", fg="white", width=20, height=2, command=self.viewScore)
        self.btn5 = Button(self.button_frame, text="Log Out", font=("Arial", 14), bg="#8E44AD", fg="white", width=20, height=2, command=self.logOut)
        # Arrange buttons in the button frame (vertically)
        self.btn5.pack(pady=10, side=BOTTOM)
        self.btn4.pack(pady=10, side=BOTTOM)
        self.btn3.pack(pady=10, side=BOTTOM)
        self.btn2.pack(pady=10, side=BOTTOM)
        self.btn1.pack(pady=10, side=BOTTOM)

        self.homeDash()
    # destroy all widget
    def destroy(self):
        for widget in self.mFrame.winfo_children():
            widget.destroy()
    def homeDash(self):
        self.destroy()
        self.mainbg = PhotoImage(file='homebg1.png') # background image
        Frame(self.mFrame, bg='#741687', width=1001, height=262).pack(fill=X)
        Frame(self.mFrame, bg='#b24bb2', width=1001, height=262).pack(fill=X)
        bgFrame = Frame(self.mFrame, bg='orange')
        bgFrame.place(relx=.95, rely=.43, relwidth=.9, relheight=.75, anchor=E)
        Label(bgFrame, image=self.mainbg).place(x=0, y=0, relwidth=1, relheight=1)
        Frame(self.mFrame, bg='#af44e2').place(relx=.5, rely=.7, relwidth=.5, relheight=.5, anchor=CENTER)
        self.mFrame.config(bg='#ca64fb')
    def makeQuiz(self):
        question = StringVar()
        optionA = StringVar()
        optionB = StringVar()
        optionC = StringVar()
        optionD = StringVar()
        answer = StringVar()
        subject = StringVar()
        self.destroy()
        self.mFrame.config(bg='#b24bb2')
        def clearInput():
            self.questionEntry.delete(0, END)
            self.optionA.delete(0, END)
            self.optionB.delete(0, END)
            self.optionC.delete(0, END)
            self.optionD.delete(0, END)
            self.answerEntry.delete(0, END)
        def displayQuiz():
            subject = self.chooseSubject.get()
            quiz = smartDatabase.displayAssessment(subject)
            for index, row in enumerate(quiz, start=1):
                print(f"Row {index}: {row}") 
                quizTxt = f"Subject:{row[1]}\n {row[0]} {row[2]}\n\t A) {row[3]}\t B) {row[4]}\t C) {row[5]}\t D) {row[6]}\t\n Answer: {row[7]}"
                label = Label(self.questionFrame, text=quizTxt, anchor="w", justify="left", bg="white", font=("Arial", 10), padx=10, pady=5)
                label.pack()

        def addQuiz():
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
            else:
                if messagebox.askyesno('Confirmation', 'Are you sure you want to add this question?'):
                    smartDatabase.createAssessment(subject, question, optionA, optionB, optionC, optionD, answer)
                    clearInput()
                    displayQuiz()
                else:
                    messagebox.showerror('Cancelled', 'You failed to add quiz')
                    return
                
        self.questionFrame = Frame(self.mFrame, bg='green', width=950, height=300)
        self.questionFrame.grid(row=0, column=0, columnspan=3)
        self.headerFrame = Frame(self.questionFrame, bg='red', pady=10)
        self.headerFrame.pack(fill=X)
        # Header Label
        self.headerLabel = Label(self.headerFrame, text='Create Assessment', font='Arial 20 bold', bg='blue', fg='white')
        self.headerLabel.pack()
        # Input
        self.inputFrame = Frame(self.questionFrame, bg='orange')
        self.inputFrame.pack(fill=X)
        # Question
        Label(self.inputFrame, text='Question: ', font='Arial 12 bold', bg='orange').grid(row=0, column=0, sticky=E, padx=5, pady=5)
        self.questionEntry = Entry(self.inputFrame, width=75, font='Arial 12')
        self.questionEntry.grid(row=0, column=1, columnspan=5, padx=5, pady=5)
        # Options
        Label(self.inputFrame, text='Options: ', font='Arial 12 bold', bg='orange').grid(row=1, column=0, sticky=E, padx=5, pady=5)
        self.optionA = Entry(self.inputFrame, width=14, font='Arial 12')
        self.optionB = Entry(self.inputFrame, width=14, font='Arial 12')
        self.optionC = Entry(self.inputFrame, width=14, font='Arial 12')
        self.optionD = Entry(self.inputFrame, width=14, font='Arial 12')
        self.optionA.grid(row=1, column=1, pady=5)
        self.optionB.grid(row=1, column=2, pady=5)
        self.optionC.grid(row=1, column=3, pady=5)
        self.optionD.grid(row=1, column=4, pady=5)
        # Answer
        Label(self.inputFrame, text='Answer: ', font='Arial 12 bold', bg='orange').grid(row=2, column=0, sticky=E, padx=5, pady=5)
        self.answerEntry = Entry(self.inputFrame, font='Arial 12', width=30)
        self.answerEntry.grid(row=2, column=1, columnspan=2, sticky=E, pady=5)
        # CHoose Subject
        Label(self.inputFrame, text='Choose Subject', font='Arial 12 bold', bg='orange').grid(row=2, column=3, sticky=E)
        self.chooseSubject = ttk.Combobox(self.inputFrame, font='Arial 12', width=14, state='readonly', values=["English", "Mathematics", "Science"])
        self.chooseSubject.grid(row=2, column=4, sticky=E)
        self.chooseSubject.current(0)
        # Add Button
        self.addBtn = Button(self.inputFrame, text="Add Quiz", bg="#4682b4", fg="white", font=("Arial", 12), padx=10, pady=5, command=addQuiz)
        self.addBtn.grid(row=2, column=5, padx=5, pady=10)

        self.displayQuiz = Frame(self.mFrame)
        self.displayQuiz.grid(row=1, column=0)

        displayQuiz()
    def chooseSubj(self):
        self.destroy()
        def english():
            self.destroy()
            topFrame = Frame(self.mFrame, bg='red')
            topFrame.grid(row=0, column=0, columnspan=2)
            Label(topFrame, font='Arial 12', text='Timer').grid(row=0, column=0)
            questionFrame = Frame(self.mFrame, bg='red', width=400, height=400)
            questionFrame.grid(row=1, column=0, padx=50, pady=50)

            answerFrame = Frame(self.mFrame, bg='blue', width=400, height=400)
            answerFrame.grid(row=1, column=1, padx=50, pady=50)
        # math
        def math():
            self.destroy()
            topFrame = Frame(self.mFrame, bg='red')
            topFrame.grid(row=0, column=0, columnspan=2)
            Label(topFrame, font='Arial 12', text='Timer').grid(row=0, column=0)
            questionFrame = Frame(self.mFrame, bg='red', width=400, height=400)
            questionFrame.grid(row=1, column=0, padx=50, pady=50)

            answerFrame = Frame(self.mFrame, bg='blue', width=400, height=400)
            answerFrame.grid(row=1, column=1, padx=50, pady=50)
        # science
        def science():
            self.destroy()
            topFrame = Frame(self.mFrame, bg='red')
            topFrame.grid(row=0, column=0, columnspan=2)
            Label(topFrame, font='Arial 12', text='Timer').grid(row=0, column=0)
            questionFrame = Frame(self.mFrame, bg='red', width=400, height=400)
            questionFrame.grid(row=1, column=0, padx=50, pady=50)

            answerFrame = Frame(self.mFrame, bg='blue', width=400, height=400)
            answerFrame.grid(row=1, column=1, padx=50, pady=50)

        picMath = PhotoImage(file='teacher_icon.png')
        self.mFrame.config(bg='#9f149f')
        Label(self.mFrame, font='Arial 32 bold', text='CHOOSE SUBJECT').grid(row=0, column=0, columnspan=3)
        Button(self.mFrame, font='Arial 14', text='English', width=20, cursor='hand2', command=english).grid(row=1, column=0, padx=50, pady=50)
        Button(self.mFrame, font='Arial 14', text='Mathematics', width=20, cursor='hand2', command=math).grid(row=1, column=1, padx=50, pady=50)
        Button(self.mFrame, font='Arial 14', text='Science', width=20, cursor='hand2', command=science).grid(row=1, column=2, padx=50, pady=50)
    def viewScore(self):
        self.destroy()
        Label(self.mFrame, font='Times 20 bold', text='VIEW SCORE', fg='blue').pack()
        self.mFrame.config(bg='#740074')
    def logOut(self):
        if messagebox.askyesno('Confirmation', 'Are you sure you want to log Out?'):
            self.window.destroy()
            logIn_window = Tk()
            logIn(logIn_window)
            logIn_window.mainloop()
        else:
            messagebox.showwarning('Cancelled', 'Log Out Failed')
            self.window.deiconify()
            return

class teacherDashboard():
    def __init__(self, window):
        self.window = window
        self.window.title("Student Mastery Assessment and Review Tool")
        self.window.geometry("1430x700+50+50")
        self.window.config(bg="#481054")
        self.window.resizable(0, 0)
        # background photo
        self.bgphoto = PhotoImage(file='teacher_bg.png') # background image
        background = Label(self.window, image=self.bgphoto, bg='#A786EF')
        background.place(x=0, y=0, relwidth=1, relheight=1)# background picture location
        # Update Time
        def update_time():
            time_label.config(text=strftime("%I:%M:%S %p"))
            date_label.config(text=strftime("%m/%d/%Y"))
            self.window.after(1000, update_time)
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
        welcome_label = Label(footer_frame, text="Welcome: Admin", bg="#BE90D4", font=("Arial", 10))
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
        self.mFrame = Frame(self.window, bg='red', bd=6, relief=RIDGE)
        self.mFrame.pack(side=LEFT, padx=20, pady=20, fill=BOTH, expand=True)
        # Add styled buttons
        self.btn1 = Button(self.button_frame, text="Home", font=("Arial", 14), bg="#BE90D4", fg="black", width=20, height=2, padx=3, pady=3, command=self.homeDash)
        self.btn2 = Button(self.button_frame, text="Create Assessment", font=("Arial", 14), bg="#b65ecc", fg="black", width=20, height=2, padx=3, pady=3, command=self.createAssessment)
        self.btn3 = Button(self.button_frame, text="View Assessment", font=("Arial", 14), bg="#8E44AD", fg="black", width=20, height=2, padx=3, pady=3, command=self.viewAssessment)
        self.btn4 = Button(self.button_frame, text="View Score and Feedback", font=("Arial", 14), bg="#8E44AD", fg="black", width=20, height=2, padx=3, pady=3, command=self.viewScore)
        self.btn5 = Button(self.button_frame, text="Log Out", font=("Arial", 14), bg="#8E44AD", fg="white", width=20, height=2, padx=3, pady=3, command=self.logOut)
        # Arrange buttons in the button frame (vertically)
        self.btn5.pack(padx=10, pady=10, side=BOTTOM)
        self.btn4.pack(padx=10, pady=10, side=BOTTOM)
        self.btn3.pack(padx=10, pady=10, side=BOTTOM)
        self.btn2.pack(padx=10, pady=10, side=BOTTOM)
        self.btn1.pack(padx=10, pady=10, side=BOTTOM)

        self.homeDash()
    def destroy(self):
        for widget in self.mFrame.winfo_children():
            widget.destroy()
    def homeDash(self):
        self.destroy()
        self.mainbg = PhotoImage(file='homebg1.png') # background image
        Frame(self.mFrame, bg='#741687', width=1001, height=262).pack(fill=X)
        Frame(self.mFrame, bg='#b24bb2', width=1001, height=262).pack(fill=X)
        bgFrame = Frame(self.mFrame, bg='orange')
        bgFrame.place(relx=.95, rely=.43, relwidth=.9, relheight=.75, anchor=E)
        Label(bgFrame, image=self.mainbg).place(x=0, y=0, relwidth=1, relheight=1)
        Frame(self.mFrame, bg='#af44e2').place(relx=.5, rely=.7, relwidth=.5, relheight=.5, anchor=CENTER)
        self.mFrame.config(bg='#ca64fb')
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
        # Add english question to database
        def english():
            def addEnglish():
                subject = "English"
                question = self.questionEntry.get()
                optionA = self.optionA.get()
                optionB = self.optionB.get()
                optionC = self.optionC.get()
                optionD = self.optionD.get()
                answer = self.answerEntry.get()
                if not subject or not question or not optionA or not optionB or not optionC or not optionD or not answer:
                    messagebox.showerror("Error", "All fields are required!")
                    return
                else:
                    if messagebox.askyesno('Confirmation', 'Are you sure you want to add this english question?'):
                        smartDatabase.createAssessment(subject, question, optionA, optionB, optionC, optionD, answer)
                        clearInput()
                    else:
                        messagebox.showerror('Cancelled', 'You failed to add quiz')
                        return
            # Config to change its command depending on the subject
            self.addBtn.config(command=addEnglish)
            self.editBtn.config(command=addEnglish)
        # Add math question to database
        def math():
            def addMath():
                subject = "Math"
                question = self.questionEntry.get()
                optionA = self.optionA.get()
                optionB = self.optionB.get()
                optionC = self.optionC.get()
                optionD = self.optionD.get()
                answer = self.answerEntry.get()
                if not subject or not question or not optionA or not optionB or not optionC or not optionD or not answer:
                    messagebox.showerror("Error", "All fields are required!")
                    return
                else:
                    if messagebox.askyesno('Confirmation', 'Are you sure you want to add this math question?'):
                        smartDatabase.createAssessment(subject, question, optionA, optionB, optionC, optionD, answer)
                        clearInput()
                    else:
                        messagebox.showerror('Cancelled', 'You failed to add quiz')
                        return
            self.addBtn.config(command=addMath)
            self.editBtn.config(command=addMath)
        # add science question to database
        def science():
            def addScience():
                subject = "Science"
                question = self.questionEntry.get()
                optionA = self.optionA.get()
                optionB = self.optionB.get()
                optionC = self.optionC.get()
                optionD = self.optionD.get()
                answer = self.answerEntry.get()
                if not subject or not question or not optionA or not optionB or not optionC or not optionD or not answer:
                    messagebox.showerror("Error", "All fields are required!")
                    return
                else:
                    if messagebox.askyesno('Confirmation', 'Are you sure you want to add this science question?'):
                        smartDatabase.createAssessment(subject, question, optionA, optionB, optionC, optionD, answer)
                        clearInput()
                    else:
                        messagebox.showerror('Cancelled', 'You failed to add quiz')
                        return
            self.addBtn.config(command=addScience)
            self.editBtn.config(command=addScience)
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
        self.headerLabel.pack(side=LEFT, padx=(350, 0))
        # Edit button
        self.editBtn = Button(self.headerFrame, text="EDIT QUIZ", width=10, bg="#4682b4", fg="white", font=("Arial", 12), padx=10, pady=5, command=chooseFirst)
        self.editBtn.pack(side=RIGHT, padx=(0, 10))
        self.editID = Entry(self.headerFrame, width=10, font='Arial 12')
        self.editID.pack(side=RIGHT, padx=20, pady=20)
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
        self.addBtn = Button(self.answerFrame, text="ADD QUIZ", width=10, bg="#4682b4", fg="white", font=("Arial", 12), padx=10, pady=5, command=chooseFirst)
        self.addBtn.pack(side=RIGHT, padx=20, pady=20)
    # ======================================================================= VIEW ASSESSMENT =======================================================================
    def viewAssessment(self):
        self.destroy()
        self.mFrame.config(bg='#9f149f')
        # View English Questions
        def viewEnglish():
            subject = "English"
            for widget in self.questionScroll.winfo_children():
                widget.destroy()
            quiz = smartDatabase.displayAssessment(subject)
            for index, row in enumerate(quiz, start=1):
                print(f"Row {index}: {row}") 
                quizTxt = f"Subject:{row[1]}\n {row[0]} {row[2]}\n\t A) {row[3]}\t B) {row[4]}\t C) {row[5]}\t D) {row[6]}\t\n Answer: {row[7]}"
                label = Label(self.questionScroll, text=quizTxt, anchor="w", justify="left", bg="white", font=("Arial", 10), padx=10, pady=5)
                label.pack()
        # View Math Questions
        def viewMath():
            subject = "Math"
            for widget in self.questionScroll.winfo_children():
                widget.destroy()
            quiz = smartDatabase.displayAssessment(subject)
            for index, row in enumerate(quiz, start=1):
                print(f"Row {index}: {row}")
                quizTxt = f"Subject:{row[1]}\n {row[0]} {row[2]}\n\t A) {row[3]}\t B) {row[4]}\t C) {row[5]}\t D) {row[6]}\t\n Answer: {row[7]}"
                label = Label(self.questionScroll, text=quizTxt, anchor="w", justify="left", bg="white", font=("Arial", 10), padx=10, pady=5)
                label.pack(fill="x", padx=5, pady=2)
        # View Science Questions
        def viewScience():
            subject = "Science"
            for widget in self.questionScroll.winfo_children():
                widget.destroy()
            quiz = smartDatabase.displayAssessment(subject)
            for index, row in enumerate(quiz, start=1):
                print(f"Row {index}: {row}")
                quizTxt = f"Subject:{row[1]}\n {row[0]} {row[2]}\n\t A) {row[3]}\t B) {row[4]}\t C) {row[5]}\t D) {row[6]}\t\n Answer: {row[7]}"
                label = Label(self.questionScroll, text=quizTxt, anchor="w", justify="left", bg="white", font=("Arial", 10), padx=10, pady=5)
                label.pack(fill="x", padx=5, pady=2)
            self.myCanvas.configure(scrollregion=self.myCanvas.bbox("all"))
        # Buttons
        self.buttonFrame = Frame(self.mFrame, bg='#b24bb2')
        self.buttonFrame.pack(fill=X, pady=(0, 30))
        Label(self.buttonFrame, font='Arial 32 bold', text='CHOOSE SUBJECT', bg='#b24bb2').pack(pady=(0, 20))
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
        self.questionScroll = Frame(self.myCanvas)
        self.myCanvas.create_window((0, 0), window=self.questionScroll, anchor="nw")
        self.questionScroll.bind("<Configure>", lambda e: self.myCanvas.configure(scrollregion=self.myCanvas.bbox("all")))
    def viewScore(self):
        self.destroy()
        Label(self.mFrame, font='Times 20 bold', text='VIEW SCORE', fg='blue').pack()
        self.mFrame.config(bg='#740074')
    def logOut(self):
        if messagebox.askyesno('Confirmation', 'Are you sure you want to log Out?'):
            self.window.destroy()
            logIn_window = Tk()
            logIn(logIn_window)
            logIn_window.mainloop()
        else:
            messagebox.showwarning('Cancelled', 'Log Out Failed')
            self.window.deiconify()
            return

window = Tk()
app = Smart(window)
window.mainloop()