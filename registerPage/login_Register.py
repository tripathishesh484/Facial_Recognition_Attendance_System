from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x785+0+0")

        # ------------   variable   -------------
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_SecurityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_cnfpass = StringVar()
        self.var_check = IntVar()

        # ------------    bg image      ------------------
        self.bg = ImageTk.PhotoImage(file=r"../All_Images/register_background.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # -------     left image       ----------
        reg_imgbg = Image.open(r"../All_Images/left_register_image.jpg")
        reg_imgbg = reg_imgbg.resize((470, 550), Image.LANCZOS)
        self.bgImg = ImageTk.PhotoImage(reg_imgbg)
        left_lbl = Label(self.root, image=self.bgImg)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # ------      main frame    -------------
        frame = Frame(self.root, bg='white')
        frame.place(x=520, y=100, width=800, height=550)

        reg_lbl = Label(frame, text='REGISTER HERE', font=("times new roman", 25, 'bold'), fg='dark green', bg='white')
        reg_lbl.place(x=20, y=20)

        # -------    label and entry  --------------

        #  -------    row1       ----------
        fname = Label(frame, text="First Name", font=("times new roman", 15, 'bold'), bg='white', fg='red')
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, 'bold'))
        fname_entry.place(x=50, y=130, width=250)

        lname = Label(frame, text="Last Name", font=("times new roman", 15, 'bold'), bg='white', fg="red")
        lname.place(x=370, y=100)

        lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, 'bold'))
        lname_entry.place(x=370, y=130, width=250)

        # -------     row2    ------------
        contact = Label(frame, text="Contact No", font=("times new roman", 15, 'bold'), bg='white', fg="red")
        contact.place(x=50, y=170)

        contact_entry = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, 'bold'))
        contact_entry.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, 'bold'), bg='white', fg="red")
        email.place(x=370, y=170)

        email_entry = ttk.Entry(frame, textvariable=self.var_email,font=("times new roman", 15, 'bold'))
        email_entry.place(x=370, y=200, width=250)

        # -------       row3    ------------
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, 'bold'), bg='white', fg="red")
        security_Q.place(x=50, y=240)

        selectQuestion=ttk.Combobox(frame, textvariable=self.var_SecurityQ,font=("times new roman", 15, 'bold'),state="readonly")
        selectQuestion["values"]=("Select", "Your Birth Place", "Your Nick Name", "Your Father Name", "Your Mother Name", "Your Pet Name", "Your School Name")
        selectQuestion.place(x=50, y=270, width=250)
        selectQuestion.current(0)

        security_A = Label(frame, text='Security Answer', font=("times new roman", 15, "bold"), bg='white', fg='red')
        security_A.place(x=370, y=240)

        security_entry = ttk.Entry(frame, textvariable=self.var_SecurityA,font=("times new roman", 15, 'bold'))
        security_entry.place(x=370, y=270, width=250)

        # -------      row 4        -------------
        pswd = Label(frame, text="Password", font=("times new roman", 15, 'bold'), bg='white', fg="red")
        pswd.place(x=50, y=310)

        pswd_entry = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15, 'bold'))
        pswd_entry.place(x=50, y=340, width=250)

        cnf_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, 'bold'), bg='white', fg="red")
        cnf_pswd.place(x=370, y=310)

        cnf_pswd_entry = ttk.Entry(frame, textvariable=self.var_cnfpass, font=("times new roman", 15, 'bold'))
        cnf_pswd_entry.place(x=370, y=340, width=250)

        #  ---------     checkbutton       -----------
        checkbutton = Checkbutton(frame, variable=self.var_check, text="I agree The Terms & Conditions", font=("times new roman", 12, 'bold'), onvalue=1, offvalue=0, fg='red')
        checkbutton.place(x=50, y=380)

        # ------     Button       -------------
        img = Image.open("../All_Images/register_image_pic.jpeg")
        img = img.resize((200, 55), Image.LANCZOS)
        self.reg_img = ImageTk.PhotoImage(img)
        button = Button(frame, image=self.reg_img, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), fg="white", activebackground='blue', bg='black',command=self.register_data)
        button.place(x=50, y=430, width=200)

        img1 = Image.open("../All_Images/login_now_btn.jpeg")
        img1 = img1.resize((200, 55), Image.LANCZOS)
        self.reg_img1 = ImageTk.PhotoImage(img1)
        button = Button(frame, image=self.reg_img1, command=self.return_login, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), fg= "white", activebackground='blue', bg='black')
        button.place(x=370, y=430, width=200)

        #   function declaration
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_SecurityQ.get() == "Select":
            messagebox.showinfo('Error', 'all field are required.')
        elif self.var_pass.get() != self.var_cnfpass.get():
            messagebox.showinfo('Error', "password and confirm password must be same.")
        elif self.var_check.get() == 0:
            messagebox.showinfo('Error', 'Please agree our terms and condition.')
        elif len(self.var_contact.get()) != 10:
            messagebox.showinfo('Error', 'please entered a correct contact number.')
        else:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Shes123@',
                database='major_project_facial_recognition'
            )
            myCursor = conn.cursor()
            query = "select * from register_details where user_email = %s"
            value = (self.var_email.get(),)
            myCursor.execute(query, value)
            row = myCursor.fetchone()
            if row != None:
                messagebox.showerror('Error', 'User already exist ,please try another email')
            else:
                myCursor.execute("insert into register_details values(%s,%s,%s,%s,%s,%s,%s)", (self.var_fname.get(),
                                                                                               self.var_lname.get(),
                                                                                               self.var_contact.get(),
                                                                                               self.var_email.get(),
                                                                                               self.var_SecurityQ.get(),
                                                                                               self.var_SecurityA.get(),
                                                                                               self.var_pass.get()
                                                                                               ))
                conn.commit()
                conn.close()
                messagebox.showinfo('Success', 'Register successfully!')

    def return_login(self):
        self.root.destroy()


if __name__ == '__main__':
    root = Tk()
    app = Register(root)
    root.mainloop()