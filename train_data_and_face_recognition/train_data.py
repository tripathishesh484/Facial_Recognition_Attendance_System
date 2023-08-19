from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x785+0+0')
        self.root.title('Train Data')

        # top label
        title_lbl_train = Label(self.root, text='TRAIN DATA SET', font=("times new roman", 35, "bold"), bg='white', fg='RED')
        title_lbl_train.place(x=0, y=0, width=1530, height=45)

        left_top_train = Image.open(r"../All_Images/facialrecognition.png")
        left_top_train = left_top_train.resize((1530, 325), Image.LANCZOS)
        self.left_picImage2_train = ImageTk.PhotoImage(left_top_train)

        left_label_train = Label(self.root, image=self.left_picImage2_train)
        left_label_train.place(x=0, y=55, width=1530, height=325)

        # button
        btn = Button(self.root, text="TRAIN DATA", cursor="hand2", font=("times new roman", 30, "bold"), fg="white", bg="red", command=self.train_Classifier)
        btn.place(x=0, y=380, width=1530, height=60)

        # bottom label
        left_bottom_train = Image.open(r"../All_Images/opencv_face_reco_more_data.jpg")
        left_bottom_train = left_bottom_train.resize((1530, 325), Image.LANCZOS)
        self.bottom_picImage2_train = ImageTk.PhotoImage(left_bottom_train)

        bottom_label_train = Label(self.root, image=self.bottom_picImage2_train)
        bottom_label_train.place(x=0, y=440, width=1530, height=325)

    def train_Classifier(self):
        data_dir = (r"D:/face_recognition_data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')   # convert into greyscale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow('Training', imageNp)
            if cv2.waitKey(1) == 13:
                break

        ids = np.array(ids)

        # ========== train the classifier and save ============
        classifier_var = cv2.face.LBPHFaceRecognizer_create()
        classifier_var.train(faces, ids)

        classifier_var.write("classifier.xml")
        cv2.destroyAllWindows()

        messagebox.showinfo('Result', 'Training dataset completed!', parent=self.root)


if __name__ == '__main__':
    root = Tk()
    obj = Train(root)
    root.mainloop()