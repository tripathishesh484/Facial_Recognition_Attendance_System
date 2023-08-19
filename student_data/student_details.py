from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

'''
Face Detection using Haar Cascades Algorithm
'''
class student_Details:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x785+0+0')
        self.root.title('Student Details')

        # ========  variable =======
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_stu_id = StringVar()
        self.var_stu_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # first image
        stu_img = Image.open(r"../All_Images/smart_attendance.jpg")
        stu_img = stu_img.resize((510, 130), Image.LANCZOS)
        self.stu_picImage = ImageTk.PhotoImage(stu_img)

        stu_lb = Label(self.root, image=self.stu_picImage)
        stu_lb.place(x=0, y=0, width=510, height=130)

        # second image
        stu_img1 = Image.open(r"../All_Images/face_recognition.png")
        stu_img1 = stu_img1.resize((510, 130), Image.LANCZOS)
        self.picImage1 = ImageTk.PhotoImage(stu_img1)

        lb1 = Label(self.root, image=self.picImage1)
        lb1.place(x=510, y=0, width=510, height=130)

        # third image
        stu_img2 = Image.open(r"../All_Images/clgPic.jpg")
        stu_img2 = stu_img2.resize((510, 130), Image.LANCZOS)
        self.stu_picImage2 = ImageTk.PhotoImage(stu_img2)

        stu_lb2 = Label(self.root, image=self.stu_picImage2)
        stu_lb2.place(x=1020, y=0, width=510, height=130)

        # background image
        img3 = Image.open(r"../All_Images/wp2551980.jpg")
        img3 = img3.resize((1530, 675), Image.LANCZOS)
        self.picImage3 = ImageTk.PhotoImage(img3)

        lb3 = Label(self.root, image=self.picImage3)
        lb3.place(x=0, y=130, width=1530, height=675)

        title_lbl = Label(lb3, text='STUDENT RECORD DETAILS', font=("times new roman", 35, "bold"), bg='white', fg='dark green')
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # main frame
        main_frame = Frame(lb3, bd=2)
        main_frame.place(x=20, y=50, width=1480, height=600)

        # left label frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman", 12,"bold"), bg="white")
        left_frame.place(x=10, y=10, width=730, height=580)

        # left label image
        left_img2 = Image.open(r"../All_Images/left_image_stuDetails.jpeg")
        left_img2 = left_img2.resize((720, 130), Image.LANCZOS)
        self.left_picImage2 = ImageTk.PhotoImage(left_img2)

        left_lb2 = Label(left_frame, image=self.left_picImage2)
        left_lb2.place(x=5, y=0, width=720, height=130)

        # current course
        current_course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"), bg="white")
        current_course_frame.place(x=5, y=135, width=720, height=115)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 13, "bold"), bg='white')
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 13, "bold"), width=20, state='readonly')
        dep_combo["values"] = ('Select Department', 'CSE', 'AIML', 'Civil', 'Mechanical', 'IT')
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 13, "bold"), bg='white')
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 13, "bold"), width=20, state='readonly')
        course_combo["values"] = ('Select Course', 'M.Tech', 'B.Tech')
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"), bg='white')
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 13, "bold"), width=20, state='readonly')
        year_combo["values"] = ('Select year', '2020-21', '2021-22', '2022-23', '2023-24', '2024-25')
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        Semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 13, "bold"), bg='white')
        Semester_label.grid(row=1, column=2, padx=10, sticky=W)

        Semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 13, "bold"), width=20, state='readonly')
        Semester_combo["values"] = ('Select Semester', '1', '2', '3', '4', '5', '6', '7', '8')
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # class student information label frame
        class_student_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"), bg="white")
        class_student_frame.place(x=5, y=250, width=720, height=300)

        # Student id
        student_id_label = Label(class_student_frame, text="Student ID:", font=("times new roman", 13, "bold"), bg='white')
        student_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        student_id_entry = ttk.Entry(class_student_frame, textvariable=self.var_stu_id, width=20, font=("times new roman", 13, "bold"))
        student_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student name
        student_name_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg='white')
        student_name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        student_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_stu_name, width=20, font=("times new roman", 13, "bold"))
        student_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        student_div_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 13, "bold"), bg='white')
        student_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        student_div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=("times new roman", 13, "bold"), width=18, state='readonly')
        student_div_combo["values"] = ('A', 'B', 'C', 'D' )
        student_div_combo.current(0)
        student_div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Student Enrollment
        student_roll_label = Label(class_student_frame, text="Student Enroll:", font=("times new roman", 13, "bold"), bg='white')
        student_roll_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        student_roll_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=("times new roman", 13, "bold"))
        student_roll_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        student_gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 13, "bold"), bg='white')
        student_gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        student_gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 13, "bold"), width=18, state='readonly')
        student_gender_combo["values"] = ('Male', 'Female', 'Other')
        student_gender_combo.current(0)
        student_gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Student DOB
        student_dob_label = Label(class_student_frame, text="DOB:", font=("times new roman", 13, "bold"), bg='white')
        student_dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        student_dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 13, "bold"))
        student_dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Student Email
        student_email_label = Label(class_student_frame, text="Email:", font=("times new roman", 13, "bold"), bg='white')
        student_email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        student_email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 13, "bold"))
        student_email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Student Phone
        student_phone_label = Label(class_student_frame, text="Mobile No.:", font=("times new roman", 13, "bold"), bg='white')
        student_phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        student_phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 13, "bold"))
        student_phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Student address
        student_address_label = Label(class_student_frame, text="Address:", font=("times new roman", 13, "bold"), bg='white')
        student_address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        student_address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 13, "bold"))
        student_address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher name
        student_teacher_label = Label(class_student_frame, text="Teacher Name:", font=("times new roman", 13, "bold"), bg='white')
        student_teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        student_teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 13, "bold"))
        student_teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radiobutton1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text='Take Photo Sample', value="yes")
        radiobutton1.grid(row=6, column=0)

        radiobutton2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text='No Photo Sample', value="no")
        radiobutton2.grid(row=6, column=1)

        # button frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg='white')
        btn_frame.place(x=0, y=200, width=715, height=40)

        save_btn = Button(btn_frame,command=self.add_data,  width=17, text='Save', font=("times new roman", 13, "bold"), bg='blue', fg='white')
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, width=17, command=self.update_data, text='Update', font=("times new roman", 13, "bold"), bg='blue', fg='white')
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, command=self.delete_data, width=17, text='Delete', font=("times new roman", 13, "bold"), bg='blue', fg='white')
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, command=self.reset_data, width=17, text='Reset', font=("times new roman", 13, "bold"), bg='blue', fg='white')
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg='white')
        btn_frame1.place(x=0, y=235, width=715, height=35)

        take_pic_sample_btn = Button(btn_frame1, command=self.generate_Dataset, width=35, text='Take Photo Sample', font=("times new roman", 13, "bold"), bg='blue', fg='white')
        take_pic_sample_btn.grid(row=0, column=0)

        update_pic_sample_btn = Button(btn_frame1, width=35, text='Update Photo Sample',font=("times new roman", 13, "bold"), bg='blue', fg='white')
        update_pic_sample_btn.grid(row=0, column=1)

        # ========> right label frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"), bg="white")
        right_frame.place(x=750, y=10, width=720, height=580)

        right_img2 = Image.open(r"../All_Images/gettyimages-1022573162.jpg")
        right_img2 = right_img2.resize((720, 130), Image.LANCZOS)
        self.right_picImage2 = ImageTk.PhotoImage(right_img2)

        right_lb2 = Label(right_frame, image=self.right_picImage2)
        right_lb2.place(x=5, y=0, width=720, height=130)

        # =====> Search System
        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"), bg="white")
        search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 13, "bold"), bg='red', fg='white')
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), width=15, state='readonly')
        search_combo["values"] = ('Select', 'Roll No.', 'Phone No.', 'Student Id')
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, width=12, text='Search', font=("times new roman", 13, "bold"), bg='blue', fg='white')
        search_btn.grid(row=0, column=3, padx=4)

        show_all_btn = Button(search_frame, width=12, text='Show All', font=("times new roman", 13, "bold"), bg='blue', fg='white')
        show_all_btn.grid(row=0, column=4, padx=4)

        # table frame
        table_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, bg='white')
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(table_frame, columns=('dep', 'course', 'year', 'sem', 'id', 'name', 'div', 'roll', 'gender', 'dob', 'email', 'phone', 'address', 'teacher', 'photo'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("dep", text='Department')
        self.Student_table.heading("course", text='Course')
        self.Student_table.heading("year", text='Year')
        self.Student_table.heading("sem", text='Semester')
        self.Student_table.heading("id", text='StudentId')
        self.Student_table.heading("name", text='Name')
        self.Student_table.heading("div", text='Division')
        self.Student_table.heading("roll", text='Enrollment no.')
        self.Student_table.heading("gender", text='Gender')
        self.Student_table.heading("dob", text='DOB')
        self.Student_table.heading("email", text='Email')
        self.Student_table.heading("phone", text='Phone')
        self.Student_table.heading("address", text='Address')
        self.Student_table.heading("teacher", text='Teacher')
        self.Student_table.heading("photo", text='PhotoSampleStatus')
        self.Student_table['show'] = "headings"

        self.Student_table.column('dep', width=100)
        self.Student_table.column('course', width=100)
        self.Student_table.column('year', width=100)
        self.Student_table.column('sem', width=100)
        self.Student_table.column('id', width=100)
        self.Student_table.column('name', width=100)
        self.Student_table.column('div', width=100)
        self.Student_table.column('roll', width=100)
        self.Student_table.column('gender', width=100)
        self.Student_table.column('dob', width=100)
        self.Student_table.column('email', width=100)
        self.Student_table.column('phone', width=100)
        self.Student_table.column('address', width=100)
        self.Student_table.column('teacher', width=100)
        self.Student_table.column('photo', width=150)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind('<ButtonRelease>', self.get_cursor)
        self.fetch_Data()

    # function declaration to add data in database
    def add_data(self):
        if self.var_dep.get() == 'Select Department' or self.var_semester.get() == 'Select Semester' or self.var_year.get()=='Select year' or self.var_course.get()=='Select Course' or self.var_stu_id.get()=='' or self.var_stu_id.get()=='':
            messagebox.showerror('Error', 'All fields are required.', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='Shes123@',
                    database='major_project_facial_recognition'
                )
                myCursor = conn.cursor()
                myCursor.execute("insert into student_details value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_stu_id.get(),
                                                                                                        self.var_stu_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get()))
                conn.commit()
                self.fetch_Data()
                conn.close()
                messagebox.showinfo('Success','Student details has been added successfully!', parent=self.root)
            except Exception as e:
                messagebox.showerror('Error', f"Due to: {str(e)}", parent=self.root)

    # inserting data in student table
    def fetch_Data(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Shes123@',
            database='major_project_facial_recognition'
        )
        myCursor = conn.cursor()
        myCursor.execute("Select * from student_details")
        data = myCursor.fetchall()
        if len(data) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for i in data:
                self.Student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # get cursor
    def get_cursor(self, event=""):
        cursor_focus = self.Student_table.focus()
        content = self.Student_table.item(cursor_focus)

        data = content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_stu_id.set(data[4])
        self.var_stu_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # update button function
    def update_data(self):
        if self.var_dep.get() == 'Select Department' or self.var_semester.get() == 'Select Semester' or self.var_year.get() == 'Select year' or self.var_course.get() == 'Select Course' or self.var_stu_id.get() == '' or self.var_stu_id.get() == '':
            messagebox.showerror('Error', 'All fields are required.', parent=self.root)
        else:
            try:
                update = messagebox.askyesno('Update','Do you want to update this student details', parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='Shes123@',
                        database='major_project_facial_recognition'
                    )
                    myCursor = conn.cursor()
                    myCursor.execute("update student_details set Dep=%s, Course=%s, Year=%s,Semester=%s, Name=%s, Division=%s, Roll=%s,Gender=%s ,Dob=%s, Email=%s,Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id = %s",(
                                     self.var_dep.get(),
                                     self.var_course.get(),
                                     self.var_year.get(),
                                     self.var_semester.get(),
                                     self.var_stu_name.get(),
                                     self.var_div.get(),
                                     self.var_roll.get(),
                                     self.var_gender.get(),
                                     self.var_dob.get(),
                                     self.var_email.get(),
                                     self.var_phone.get(),
                                     self.var_address.get(),
                                     self.var_teacher.get(),
                                     self.var_radio1.get(),
                                     self.var_stu_id.get()
                                     ))
                    conn.commit()
                    self.fetch_Data()
                    conn.close()

                else:
                    if not update:
                        return
                messagebox.showinfo('success', 'Student details successfully update completed', parent=self.root)

            except Exception as es:
                messagebox.showerror('Error', f'Due to: {str(es)}', parent=self.root)

    # delete btn funtion
    def delete_data(self):
        if self.var_stu_id.get() == '':
            messagebox.showerror('Error', 'StudentId must be required', parent=self.root)
        else:
            try:
                data = messagebox.askyesno('Confirmation', "Do you want to delete this Student details.", parent=self.root)
                if data > 0:
                    conn = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='Shes123@',
                        database='major_project_facial_recognition'
                    )
                    myCursor = conn.cursor()
                    sql = "delete from student_details where Student_id=%s"
                    var = (self.var_stu_id.get(), )
                    myCursor.execute(sql, var)
                    conn.commit()
                    self.fetch_Data()
                    conn.close()
                else:
                    if not data:
                        return

                messagebox.showinfo('Success','Student details deleted successfully', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due to: {str(es)}', parent=self.root)

    # reset button function
    def reset_data(self):
        self.var_dep.set('Select Department')
        self.var_course.set('Select Course')
        self.var_year.set('Select Year')
        self.var_semester.set('Select Semester')
        self.var_stu_id.set('')
        self.var_div.set('A')
        self.var_roll.set('')
        self.var_gender.set('Male')
        self.var_dob.set('')
        self.var_email.set('')
        self.var_phone.set('')
        self.var_address.set('')
        self.var_teacher.set('')
        self.var_radio1.set('')

    # generate data set or take a photo sample
    def generate_Dataset(self):
        if self.var_dep.get() == 'Select Department' or self.var_semester.get() == 'Select Semester' or self.var_year.get() == 'Select year' or self.var_course.get() == 'Select Course' or self.var_stu_id.get() == '' or self.var_stu_id.get() == '':
            messagebox.showerror('Error', 'All fields are required.', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='Shes123@',
                        database='major_project_facial_recognition'
                )
                myCursor = conn.cursor()
                myCursor.execute("Select * from student_details")
                myResult = myCursor.fetchall()
                id = 0
                for x in myResult:
                    id += 1
                myCursor.execute("update student_details set Dep=%s, Course=%s, Year=%s,Semester=%s, Name=%s, Division=%s, Roll=%s,Gender=%s ,Dob=%s, Email=%s,Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id = %s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_stu_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_stu_id.get() == id+1
                    ))
                conn.commit()
                self.fetch_Data()
                self.reset_data()
                conn.close()

                # load predefined data on frontalFace from opencv
                face_classifier = cv2.CascadeClassifier(
                    "../train_data_and_face_recognition/haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3 and minimum neighbor = 5
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                # open camera
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame_image = cap.read()
                    if face_cropped(my_frame_image) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame_image), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGRA2GRAY)
                        file_name_path = r"D:/face_recognition_data/"+str(self.var_stu_name.get())+"."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 50:
                        break
                cap.release()
                cv2.destroyAllWindows()
                self.var_stu_name.set("")
                messagebox.showinfo('Result', 'Generating dataset completed successfully.', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due to: {str(es)}', parent=self.root)


if __name__ == '__main__':
    root = Tk()
    obj = student_Details(root)
    root.mainloop()