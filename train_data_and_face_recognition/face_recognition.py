from tkinter import*
from PIL import Image, ImageTk
import mysql.connector
import cv2
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x785+0+0')
        self.root.title('Face Recognition System')

        # top label
        lbl_face = Label(self.root, text='FACE RECOGNITION', font=("times new roman", 35, "bold"), bg='white', fg='green')
        lbl_face.place(x=0, y=0, width=1530, height=45)

        # image1
        left_top_face = Image.open(r"../All_Images/face_detector1.jpg")
        left_top_face = left_top_face.resize((650, 700), Image.LANCZOS)
        self.left_picImage2_face = ImageTk.PhotoImage(left_top_face)

        left_label_face = Label(self.root, image=self.left_picImage2_face)
        left_label_face.place(x=0, y=55, width=650, height=700)

        # image2
        right_top_face = Image.open(r"../All_Images/face_recognition_img2.jpg")
        right_top_face = right_top_face.resize((950, 700), Image.LANCZOS)
        self.right_picImage2_face = ImageTk.PhotoImage(right_top_face)

        right_label_face = Label(self.root, image=self.right_picImage2_face)
        right_label_face.place(x=650, y=55, width=950, height=700)

        # button
        btn = Button(right_label_face,command=self.face_recog, text="Face Recognition", cursor="hand2", font=("times new roman", 18, "bold"), fg="white", bg="dark green")
        btn.place(x=365, y=620, width=200, height=40)

    # =============  attendance =================
    def mark_attendance(self, Enroll, Name, Dept):
        with open("Shivam.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_List = []
            for line in myDataList:
                entry = line.split(',')
                name_List.append(entry[0])
            if (Enroll not in name_List) and (Name not in name_List) and (Dept not in name_List):
                ctime = datetime.now()
                d1 = ctime.strftime("%d/%m/%Y")
                dtString = ctime.strftime("%H:%M:%S")
                f.writelines(f"\n{Enroll},{Name},{Dept},{dtString},{d1}, Present")


    # ============= Face Recognition ============
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img,(x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))
                try:
                    conn = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='Shes123@',
                        database='major_project_facial_recognition'
                    )
                    myCursor = conn.cursor()
                    myCursor.execute("select Name from student_details where Student_id="+str(id))
                    data_fetch_name = myCursor.fetchone()
                    data_fetch_name = "+".join(data_fetch_name)

                    myCursor.execute("select Roll from student_details where Student_id=" + str(id))
                    data_fetch_roll = myCursor.fetchone()
                    data_fetch_roll = "+".join(data_fetch_roll)

                    myCursor.execute("select Dep from student_details where Student_id=" + str(id))
                    data_fetch_dep = myCursor.fetchone()
                    data_fetch_dep = "+".join(data_fetch_dep)

                    if confidence > 80:
                        cv2.putText(img, f"Roll:{data_fetch_roll}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0,255), 2)
                        cv2.putText(img, f"Name:{data_fetch_name}", (x, y-35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0,255), 2)
                        cv2.putText(img, f"Dep:{data_fetch_dep}", (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0,245), 2)
                        self.mark_attendance(data_fetch_roll, data_fetch_name, data_fetch_dep)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                except Exception as e:
                    print(e)
                coord = [x, y, w, y]
            return coord

        def recognize(img, clf, face_cascade):
            coord = draw_boundary(img, face_cascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            try:
                ret, img = video_cap.read()
                img = recognize(img, clf, face_cascade)
                cv2.imshow("Welcome to face recognition", img)

                if cv2.waitKey(1) == 13:
                    break
            except Exception as e:
                print(e)
                # pass
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()