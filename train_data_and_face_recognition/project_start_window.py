from registerPage.login_Register import*
from train_data_and_face_recognition.front_view_of_main_page import Face_Recognition_System


def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # first image
        img = Image.open(r"../All_Images/Stanford.jpg")
        img = img.resize((510, 130), Image.LANCZOS)
        self.picImage = ImageTk.PhotoImage(img)

        lb = Label(self.root, image=self.picImage)
        lb.place(x=0, y=0, width=510, height=130)

        # second image
        img1 = Image.open(r"../All_Images/facialrecognition.png")
        img1 = img1.resize((510, 130), Image.LANCZOS)
        self.picImage1 = ImageTk.PhotoImage(img1)

        lb1 = Label(self.root, image=self.picImage1)
        lb1.place(x=510, y=0, width=510, height=130)

        # third image
        img2 = Image.open(r"../All_Images/u.jpg")
        img2 = img2.resize((510, 130), Image.LANCZOS)
        self.picImage2 = ImageTk.PhotoImage(img2)

        lb2 = Label(self.root, image=self.picImage2)
        lb2.place(x=1020, y=0, width=510, height=130)

        # bg image
        img1_bg = Image.open(r"../All_Images/login_bg_img.jpeg")
        img1_bg = img1_bg.resize((1530, 720), Image.LANCZOS)
        self.picImage1_bg = ImageTk.PhotoImage(img1_bg)

        lb1_bg = Label(self.root, image=self.picImage1_bg)
        lb1_bg.place(x=0, y=120, width=1530, height=720)

        title_lbl = Label(lb1_bg, text='FACE RECOGNITION ATTENDANCE SYSTEM', font=("times new roman", 35, "bold"), bg='white', fg='red')
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # frame
        frame1 = Frame(self.root, bg="black")
        frame1.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"../All_Images/login_icon.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lbl_img1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame1, text="Get Started", font=("times new roman",20,"bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        #label for user name
        username_lbl=Label(frame1, text="Email", font=("times new roman", 20, "bold"), fg="white", bg="black")
        username_lbl.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame1, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=190, width=270)

        # label for user pass
        userpass_lbl = Label(frame1, text="Password", font=("times new roman", 20, "bold"), fg="white", bg="black")
        userpass_lbl.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame1, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=265, width=270)

        #icon image
        img2 = Image.open(r"../All_Images/login_icon.png")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lbl_img2.place(x=650, y=329, width=25, height=25)

        img3 = Image.open(r"../All_Images/lock_icon.jpg")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lbl_img3.place(x=650, y=403, width=25, height=25)

        #login button
        login_btn = Button(frame1, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red", command=self.login)
        login_btn.place(x=110,y=310, width=120, height=35)

        #register button
        register_btn = Button(frame1, text="New User Register", font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black", command=self.register_window)
        register_btn.place(x=16, y=360, width=160)

        # forget pass button
        forget_btn = Button(frame1, text="Forget Password", font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black", command=self.forget_pass_window)
        forget_btn.place(x=10, y=384, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "all field required")
        else:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Shes123@',
                database='major_project_facial_recognition'
            )
            myCursor = conn.cursor()
            myCursor.execute("select * from register_details where user_email=%s and user_password=%s", (
                                                                                                         self.txtuser.get(),
                                                                                                         self.txtpass.get()
                                                                                                         ))
            row = myCursor.fetchone()
            if row == None:
                messagebox.showinfo('Error', 'Invalid email or password')
            else:
                open_main = messagebox.askyesno('Asked', 'Access only Admin')
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # reset password function
    def reset_pass_func(self):
        if self.selectQuestion1.get() == "Select":
            messagebox.showerror('Error', 'Select the security questions.')
        elif self.security_entry1.get() == "":
            messagebox.showerror('Error', 'Please enter the answer')
        elif self.new_pass_entry.get() == "":
            messagebox.showerror('Error', 'Please entered the new password.')
        else:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Shes123@',
                database='major_project_facial_recognition'
            )
            myCursor = conn.cursor()
            query = 'select * from register_details where user_email = %s and user_SecurityQ=%s and user_SecurityA=%s'
            value = (self.txtuser.get(), self.selectQuestion1.get(), self.security_entry1.get())
            myCursor.execute(query, value)
            data = myCursor.fetchone()
            if data == None:
                messagebox.showerror('Error', 'Please entered correct info!')
            else:
                query = 'update register_details set user_password = %s where user_email=%s'
                value = (self.new_pass_entry.get(), self.txtuser.get())
                myCursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo('Success', 'Password changed successfully !', parent=self.root2)
                self.root2.destroy()

    # forget password function
    def forget_pass_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror('Error', 'Please enter Email to reset password')
        else:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Shes123@',
                database='major_project_facial_recognition'
            )
            myCursor = conn.cursor()
            query = "select * from register_details where user_email = %s"
            value = (self.txtuser.get(), )
            myCursor.execute(query, value)
            data = myCursor.fetchone()
            if data == None:
                messagebox.showerror('Error', 'Please entered valid email.')
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title('Forget Password')
                self.root2.geometry('340x450+610+170')

                lbl = Label(self.root2, text='Forget Password', font=("times new roman", 20, "bold"), fg='red', bg='white')
                lbl.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, 'bold'),bg='white', fg="green")
                security_Q.place(x=50, y=80)

                self.selectQuestion1 = ttk.Combobox(self.root2, font=("times new roman", 15, 'bold'), state="readonly")
                self.selectQuestion1["values"] = ("Select", "Your Birth Place", "Your Nick Name", "Your Father Name", "Your Mother Name", "Your Pet Name","Your School Name")
                self.selectQuestion1.place(x=50, y=110, width=250)
                self.selectQuestion1.current(0)

                security_A1 = Label(self.root2, text='Security Answer', font=("times new roman", 15, "bold"), bg='white', fg='green')
                security_A1.place(x=50, y=150)

                self.security_entry1 = ttk.Entry(self.root2, font=("times new roman", 15, 'bold'))
                self.security_entry1.place(x=50, y=180, width=250)

                new_pass = Label(self.root2, text='Enter New Password', font=("times new roman", 15, "bold"), bg='white', fg='green')
                new_pass.place(x=50, y=220)

                self.new_pass_entry = ttk.Entry(self.root2, font=("times new roman", 15, 'bold'))
                self.new_pass_entry.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset", font=("times new roman", 15, 'bold'), fg="white", bg="green", command=self.reset_pass_func)
                btn.place(x=140, y=290)


if __name__ == '__main__':
    main()