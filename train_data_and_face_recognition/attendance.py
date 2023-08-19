from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog


mydata = []
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x785+0+0')
        self.root.title('Attendance Details')

        # ================== variable =======
        self.var_enroll = StringVar()
        self.var_name = StringVar()
        self.var_dept = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()

        # image1
        left_top_face = Image.open(r"../All_Images/smart-attendance.jpg")
        left_top_face = left_top_face.resize((780, 200), Image.LANCZOS)
        self.left_picImage2_face = ImageTk.PhotoImage(left_top_face)

        left_label_face = Label(self.root, image=self.left_picImage2_face)
        left_label_face.place(x=0, y=0, width=780, height=200)

        # image2
        right_top_face = Image.open(r"../All_Images/clgPic.jpg")
        right_top_face = right_top_face.resize((780, 200), Image.LANCZOS)
        self.right_picImage2_face = ImageTk.PhotoImage(right_top_face)

        right_label_face = Label(self.root, image=self.right_picImage2_face)
        right_label_face.place(x=780, y=0, width=780, height=200)

        # background image
        img3 = Image.open(r"../All_Images/wp2551980.jpg")
        img3 = img3.resize((1530, 675), Image.LANCZOS)
        self.picImage3 = ImageTk.PhotoImage(img3)

        lb3 = Label(self.root, image=self.picImage3)
        lb3.place(x=0, y=200, width=1530, height=675)

        # title label
        lbl_face = Label(self.root, text='ATTENDANCE MANAGEMENT SYSTEM', font=("times new roman", 35, "bold"), bg='white', fg='green')
        lbl_face.place(x=0, y=200, width=1530, height=45)

        # main frame
        main_frame = Frame(lb3, bd=2)
        main_frame.place(x=20, y=50, width=1480, height=530)

        # left label frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"), bg="white")
        left_frame.place(x=10, y=10, width=730, height=510)

        # left label image
        left_img2 = Image.open(r"../All_Images/left_image_stuDetails.jpeg")
        left_img2 = left_img2.resize((720, 130), Image.LANCZOS)
        self.left_picImage2 = ImageTk.PhotoImage(left_img2)

        left_lb2 = Label(left_frame, image=self.left_picImage2)
        left_lb2.place(x=5, y=0, width=720, height=130)

        # left label inside frame
        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=135, width=720, height=400)

        # ============= Label and entry ===========
        # Student Enrollment
        student_roll_label = Label(left_inside_frame, text="Student Enroll:", font=("times new roman", 13, "bold"), bg='white')
        student_roll_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        student_roll_entry = ttk.Entry(left_inside_frame, textvariable=self.var_enroll, width=20, font=("times new roman", 13, "bold"))
        student_roll_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student name
        student_name_label = Label(left_inside_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg='white')
        student_name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        student_name_entry = ttk.Entry(left_inside_frame, textvariable=self.var_name, width=20, font=("times new roman", 13, "bold"))
        student_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Student Dept
        student_dept_label = Label(left_inside_frame, text="Dept:", font=("times new roman", 13, "bold"), bg='white')
        student_dept_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        student_dept_entry = ttk.Entry(left_inside_frame, textvariable=self.var_dept, width=20, font=("times new roman", 13, "bold"))
        student_dept_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # attendance time
        student_time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 13, "bold"), bg='white')
        student_time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        student_time_entry = ttk.Entry(left_inside_frame, textvariable=self.var_time, width=20, font=("times new roman", 13, "bold"))
        student_time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # attendance date
        student_date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 13, "bold"), bg='white')
        student_date_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        student_date_entry = ttk.Entry(left_inside_frame, textvariable=self.var_date, width=20, font=("times new roman", 13, "bold"))
        student_date_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # attendance status
        student_attenStatus_label = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 13, "bold"), bg='white')
        student_attenStatus_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        student_attenStatus_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_attendance, font=("times new roman", 13, "bold"), width=18, state='readonly')
        student_attenStatus_combo["values"] = ('Select Status', 'Present', 'Absent')
        student_attenStatus_combo.current(0)
        student_attenStatus_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg='white')
        btn_frame.place(x=0, y=300, width=715, height=40)

        import_btn = Button(btn_frame, width=17, text='Import CSV', command=self.importCsv, font=("times new roman", 13, "bold"), bg='blue', fg='white')
        import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, width=17, text='Export CSV', command=self.export_Csv, font=("times new roman", 13, "bold"), bg='blue', fg='white')
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, width=17, text='Update', font=("times new roman", 13, "bold"), bg='blue', fg='white')
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, command=self.reset_data, width=17, text='Reset', font=("times new roman", 13, "bold"), bg='blue', fg='white')
        reset_btn.grid(row=0, column=3)

        # ========> right label frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance", font=("times new roman", 12, "bold"), bg="white")
        right_frame.place(x=750, y=10, width=720, height=510)

        # table frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg='white')
        table_frame.place(x=5, y=5, width=710, height=445)

        # ============= > scroll bar table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("Enrollment", "Name", "Department", "Time", "Date", "Attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Enrollment", text="Enrollment no.")
        self.AttendanceReportTable.heading("Name", text="Student Name")
        self.AttendanceReportTable.heading("Department", text="Department")
        self.AttendanceReportTable.heading("Time", text="Time")
        self.AttendanceReportTable.heading("Date", text="Date")
        self.AttendanceReportTable.heading("Attendance", text="Attendance Status")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("Enrollment", width=100)
        self.AttendanceReportTable.column("Name", width=100)
        self.AttendanceReportTable.column("Department", width=100)
        self.AttendanceReportTable.column("Time", width=100)
        self.AttendanceReportTable.column("Date", width=100)
        self.AttendanceReportTable.column("Attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # =========== fetch data ===========
    def fetch_data(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # ==================== import csv file data =========
    def importCsv(self):
        global mydata
        mydata.clear()
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
        with open(filename) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    # ============== export csv file data ===========
    def export_Csv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", 'No Record Found! to export.', parent=self.root)
                return False
            filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
            with open(filename, mode="w", newline="\n") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success", "Data "+os.path.basename(filename)+" Export Successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Due to {str(e)}", parent=self.root)

    # =========== update ===========
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)

        rows = content['values']

        self.var_enroll.set(rows[0])
        self.var_name.set(rows[1])
        self.var_dept.set(rows[2])
        self.var_time.set(rows[3])
        self.var_date.set(rows[4])
        self.var_attendance.set(rows[5])

    # ======================== reset data ===============
    def reset_data(self):
        self.var_enroll.set("")
        self.var_name.set("")
        self.var_dept.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")


if __name__ == '__main__':
    root = Tk()
    obj = Attendance(root)
    root.mainloop()