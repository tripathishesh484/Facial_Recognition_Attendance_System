from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
from help_box.helpDesk import Help
from time import sleep
import os


class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.geometry('730x630+400+70')
        self.root.title('ChatBot')
        self.root.bind('<Return>', self.enter_func)

        # main frame
        main_frame = Frame(self.root, bd=4, bg="powder blue", width=610)
        main_frame.pack()

        # image chat
        img_chat = Image.open(r"../All_Images/chat.jpg")
        img_chat = img_chat.resize((200, 70), Image.LANCZOS)
        self.left_picImage2_chat = ImageTk.PhotoImage(img_chat)

        left_img_chat = Label(main_frame, image=self.left_picImage2_chat, bd=3, relief=RAISED, anchor='nw', width=700, compound=LEFT, text="CHAT ME", font=("times new roman", 20, "bold"), fg='green', bg='white')
        left_img_chat.pack(side=TOP)

        # scrollbar
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=("arial", 14), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        # inserting start txt
        self.text.insert(END, '\n\n'+"Bot : I am a Bot AI. How may i help you ?")
        # button frame
        btn_frame = Frame(self.root, bd=4, width=730, bg='white')
        btn_frame.pack()

        # label
        label = Label(btn_frame, text="Type something :", font=("arial", 14, "bold"), bg='white', fg="blue")
        label.grid(row=0, column=0, padx=5, sticky=W)

        # Entry field
        self.entry=StringVar()
        self.entry1 = Entry(btn_frame, textvariable=self.entry, width=37, font=("times new roman", 16))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)

        self.button = Button(btn_frame, command=self.send, width=7, text='Send >>', font=("arial", 15, "bold"), bg='green')
        self.button.grid(row=0, column=2, padx=5, sticky=W)

        self.but_clear_data = Button(btn_frame, command=self.clear, width=9, text='Clear Data', font=("arial", 15, "bold"), bg='red', fg="white")
        self.but_clear_data.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ""
        self.label_1 = Label(btn_frame, text=self.msg, font=("arial", 14, "bold"), bg='white', fg="red")
        self.label_1.grid(row=1, column=1, padx=5, sticky=W)

    # ===========   function to talk with bot
    def enter_func(self, event=""):
        self.button.invoke()
        self.entry.set("")

    def clear(self):
        self.text.delete('1.0', END)
        self.entry.set("")

    def send(self):
        send = '\n\t\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END, '\n'+send)

        self.text.yview(END)

        if self.entry.get() == "":
            self.msg = 'Please enter some input'
            self.label_1.config(text=self.msg, fg='red')
        else:
            self.msg = ""
            self.label_1.config(text=self.msg, fg="red")

        if self.entry.get().lower() == 'hello':
            self.text.insert(END, '\n\n'+"Bot : Hii")
        elif self.entry.get().lower() == 'how are you' or self.entry.get().lower() == 'how are you ?' or self.entry.get().lower() == 'how are you?':
            self.text.insert(END, '\n\n'+"Bot : fine and you")
        elif self.entry.get().lower() == 'who created you' or self.entry.get().lower() == 'who created you ?' or self.entry.get().lower() == 'who created you?':
            self.text.insert(END, '\n\n'+"Bot : Shesh Mani Tripathi created me by using python")
        elif self.entry.get().lower() == 'what is your name' or self.entry.get().lower() == 'what is your name ?' or self.entry.get().lower() == 'what is your name?':
            self.text.insert(END, '\n\n'+"Bot : My name is Bot")
        elif self.entry.get().lower() == 'bye' or self.entry.get().lower() == 'bye bye' or self.entry.get().lower() == 'bye bot':
            self.text.insert(END, '\n\n'+"Bot : Thank you for talking with us. I hope you like this BYE .......")
        elif self.entry.get() == 'help':
            self.text.insert(END, '\n\n' + "Bot : Please wait and contact in this Email for more info......")
            self.help_data()
        else:
            self.text.insert(END, '\n\n'+"Bot : Sorry! I didn't get it!")
        self.entry.set("")

    # help desk function
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.call_fun = Help(self.new_window)


if __name__ == '__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()