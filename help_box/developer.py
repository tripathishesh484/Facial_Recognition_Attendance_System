from tkinter import*
from PIL import Image, ImageTk


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x785+0+0')
        self.root.title('Developer Details')

        # top label
        title_lbl_developer = Label(self.root, text='DEVELOPER', font=("times new roman", 35, "bold"), bg='white', fg='blue')
        title_lbl_developer.place(x=0, y=0, width=1530, height=45)

        left_top_developer = Image.open(r"../All_Images/dev.jpg")
        left_top_developer = left_top_developer.resize((1530, 720), Image.LANCZOS)
        self.left_picImage2_developer = ImageTk.PhotoImage(left_top_developer)

        left_label_developer = Label(self.root, image=self.left_picImage2_developer)
        left_label_developer.place(x=0, y=55, width=1530, height=720)

        # ================= Sheshmani Frame
        sheshmani_frame = Frame(left_label_developer, bd=2, bg="white")
        sheshmani_frame.place(x=70, y=50, width=400, height=600)

        # Sheshmani image
        right_sheshmani_img = Image.open(r"../All_Images/sheshmani_pic.jpg")
        right_sheshmani_img = right_sheshmani_img.resize((200, 200), Image.LANCZOS)
        self.right_picImage2_img = ImageTk.PhotoImage(right_sheshmani_img)

        right_label_img = Label(sheshmani_frame, image=self.right_picImage2_img)
        right_label_img.place(x=100, y=0, width=200, height=200)

        # Sheshmani info
        dev_sheshmani = Label(sheshmani_frame, text="Hello, my name is Shesh Mani Tripathi.", font=("times new roman", 15, "bold"), bg='white', fg="purple")
        dev_sheshmani.place(x=20, y=210)

        # =======================  Sanskar Frame
        sanskar_frame = Frame(left_label_developer, bd=2, bg="white")
        sanskar_frame.place(x=570, y=50, width=400, height=600)

        right_sanskar_img = Image.open(r"../All_Images/sanskar.jpg")
        right_sanskar_img = right_sanskar_img.resize((200, 200), Image.LANCZOS)
        self.right_picImage2_img1 = ImageTk.PhotoImage(right_sanskar_img)

        right_label_img1 = Label(sanskar_frame, image=self.right_picImage2_img1)
        right_label_img1.place(x=100, y=0, width=200, height=200)

        # Sanskar info
        dev_sanskar = Label(sanskar_frame, text="Hello, my name is Sanskar Upadhyay.", font=("times new roman", 15, "bold"), bg='white', fg="purple")
        dev_sanskar.place(x=30, y=210)

        # ==================  Prince Frame
        prince_frame = Frame(left_label_developer, bd=2, bg="white")
        prince_frame.place(x=1070, y=50, width=400, height=600)

        # prince img
        right_prince_img = Image.open(r"../All_Images/prince.jpg")
        right_prince_img = right_prince_img.resize((200, 200), Image.LANCZOS)
        self.right_picImage2_img2 = ImageTk.PhotoImage(right_prince_img)

        right_label_img2 = Label(prince_frame, image=self.right_picImage2_img2)
        right_label_img2.place(x=100, y=0, width=200, height=200)

        # Prince info
        dev_prince = Label(prince_frame, text="Hello, my name is Prince Kumar.", font=("times new roman", 15, "bold"), bg='white', fg="purple")
        dev_prince.place(x=50, y=210)



if __name__ == '__main__':
    root = Tk()
    obj = Developer(root)
    root.mainloop()