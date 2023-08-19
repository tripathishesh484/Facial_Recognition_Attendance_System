from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x785+0+0')
        self.root.title('help box')

        # top label
        title_lbl_developer = Label(self.root, text='HELP', font=("times new roman", 35, "bold"), bg='white', fg='blue')
        title_lbl_developer.place(x=0, y=0, width=1530, height=45)

        left_top_developer = Image.open(r"../All_Images/help_img.jpeg")
        left_top_developer = left_top_developer.resize((1530, 720), Image.LANCZOS)
        self.left_picImage2_developer = ImageTk.PhotoImage(left_top_developer)

        left_label_developer = Label(self.root, image=self.left_picImage2_developer)
        left_label_developer.place(x=0, y=55, width=1530, height=720)

        # help info
        dev_help1 = Label(left_label_developer, text="Email: tripathishesh484@gmail.com", font=("times new roman", 20, "bold"), bg='white', fg="blue")
        dev_help1.place(x=540, y=130)

        dev_help1 = Label(left_label_developer, text="Email: princesinghssm123@gmail.com", font=("times new roman", 20, "bold"), bg='white', fg="red")
        dev_help1.place(x=540, y=170)

        dev_help1 = Label(left_label_developer, text="Email: sanskarupadhyay63@gmail.com", font=("times new roman", 20, "bold"), bg='white', fg="green")
        dev_help1.place(x=540, y=210)


if __name__ == '__main__':
    root = Tk()
    obj = Help(root)
    root.mainloop()