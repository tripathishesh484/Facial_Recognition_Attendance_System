import tkinter.messagebox
from tkinter import*
from PIL import Image, ImageTk
from student_data.student_details import student_Details
from train_data_and_face_recognition.train_data import Train
from train_data_and_face_recognition.face_recognition import Face_Recognition
from train_data_and_face_recognition.attendance import Attendance
from help_box.developer import Developer
from chatbot.chatbot import ChatBot
from time import strftime
import os


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x785+0+0')
        self.root.title('Face Recognition System')

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

        # background image
        img3 = Image.open(r"../All_Images/wp2551980.jpg")
        img3 = img3.resize((1530, 675), Image.LANCZOS)
        self.picImage3 = ImageTk.PhotoImage(img3)

        lb3 = Label(self.root, image=self.picImage3)
        lb3.place(x=0, y=130, width=1530, height=675)

        title_lbl = Label(lb3, text='FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE', font=("times new roman", 35, "bold"), bg='white', fg='red')
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # =============time ========
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl = Label(title_lbl, font=("times new roman", 14, 'bold'), bg="white", fg="blue")
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        # student button
        img4 = Image.open(r"../All_Images/gettyimages-1022573162.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.picImage4 = ImageTk.PhotoImage(img4)

        b1 = Button(lb3, image=self.picImage4, cursor="hand2", command=self.Stu_details)
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(lb3, text="Student Details", command=self.Stu_details, cursor="hand2", font=("times new roman", 15, "bold"), fg="white", bg="darkblue")
        b1_1.place(x=200, y=300, width=220, height=40)

        # detect face button
        img5 = Image.open(r"../All_Images/face_detector1.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.picImage5 = ImageTk.PhotoImage(img5)

        b2 = Button(lb3, image=self.picImage5, cursor="hand2", command=self.face_data)
        b2.place(x=500, y=100, width=220, height=220)

        b2_2 = Button(lb3, text="Face Detector", command=self.face_data, cursor="hand2", font=("times new roman", 15, "bold"), fg="white",bg="darkblue")
        b2_2.place(x=500, y=300, width=220, height=40)

        # Attendance face button
        img6 = Image.open(r"../All_Images/report.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.picImage6 = ImageTk.PhotoImage(img6)

        b3 = Button(lb3, image=self.picImage6, cursor="hand2", command=self.attendance_data)
        b3.place(x=800, y=100, width=220, height=220)

        b3_3 = Button(lb3, text="Attendance", command=self.attendance_data, cursor="hand2", font=("times new roman", 15, "bold"), fg="white",bg="darkblue")
        b3_3.place(x=800, y=300, width=220, height=40)

        # help desk button
        img7 = Image.open(r"../All_Images/chat.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.picImage7 = ImageTk.PhotoImage(img7)

        b3 = Button(lb3, image=self.picImage7, command=self.chatbot_data, cursor="hand2")
        b3.place(x=1100, y=100, width=220, height=220)

        b3_3 = Button(lb3, text="Help Desk", command=self.chatbot_data, cursor="hand2", font=("times new roman", 15, "bold"), fg="white",bg="darkblue")
        b3_3.place(x=1100, y=300, width=220, height=40)

        # Train face button
        img8 = Image.open(r"../All_Images/Train.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.picImage8 = ImageTk.PhotoImage(img8)

        b4 = Button(lb3, image=self.picImage8, cursor="hand2", command=self.train_data)
        b4.place(x=200, y=380, width=220, height=220)

        b4_4 = Button(lb3, text="Train Data", cursor="hand2", command=self.train_data, font=("times new roman", 15, "bold"), fg="white",bg="darkblue")
        b4_4.place(x=200, y=580, width=220, height=40)

        # photos face button
        img9 = Image.open(r"../All_Images/opencv_face_reco_more_data.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.picImage9 = ImageTk.PhotoImage(img9)

        b5 = Button(lb3, command=self.open_img, image=self.picImage9, cursor="hand2")
        b5.place(x=500, y=380, width=220, height=220)

        b5_5 = Button(lb3, command=self.open_img, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"), fg="white", bg="darkblue")
        b5_5.place(x=500, y=580, width=220, height=40)

        # Developer face button
        img10 = Image.open(r"../All_Images/Team-Management-Software-Development.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.picImage10 = ImageTk.PhotoImage(img10)

        b6 = Button(lb3, image=self.picImage10, command=self.develper_data, cursor="hand2")
        b6.place(x=800, y=380, width=220, height=220)

        b6_6 = Button(lb3, text="Developer", command=self.develper_data, cursor="hand2", font=("times new roman", 15, "bold"), fg="white",bg="darkblue")
        b6_6.place(x=800, y=580, width=220, height=40)

        # Exit button
        img11 = Image.open(r"../All_Images/exit.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.picImage11 = ImageTk.PhotoImage(img11)

        b7 = Button(lb3, image=self.picImage11, command=self.exit_button, cursor="hand2")
        b7.place(x=1100, y=380, width=220, height=220)

        b7_7 = Button(lb3, text="Exit", command=self.exit_button, cursor="hand2", font=("times new roman", 15, "bold"), fg="white",bg="darkblue")
        b7_7.place(x=1100, y=580, width=220, height=40)

    # =============== function for all button
    # photos function
    def open_img(self):
        os.startfile(r"D:\face_recognition_data")

    # function button
    def Stu_details(self):
        self.new_window = Toplevel(self.root)
        self.call_fun = student_Details(self.new_window)

    # train data button
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.call_fun = Train(self.new_window)

    # Face Recognition
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.call_fun = Face_Recognition(self.new_window)

    # attendance function
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.call_fun = Attendance(self.new_window)

    # developer function
    def develper_data(self):
        self.new_window = Toplevel(self.root)
        self.call_fun = Developer(self.new_window)

    # exit button function
    def exit_button(self):
        self.exit_button = tkinter.messagebox.askyesno("Face Recognization", " Are you sure want to exit!", parent=self.root)
        if self.exit_button > 0:
            self.root.destroy()
        else:
            return

    # chatbot helpdesk function
    def chatbot_data(self):
        self.new_window = Toplevel(self.root)
        self.call_fun = ChatBot(self.new_window)


if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()