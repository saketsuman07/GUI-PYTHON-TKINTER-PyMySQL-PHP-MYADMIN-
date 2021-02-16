from tkinter import  *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
class register:


    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.bg = ImageTk.PhotoImage(file="images/home.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)





        # leftimage
        self.left = ImageTk.PhotoImage(file="images/kkr.jpg")

        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)
        # frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)
        title = Label(frame1, text="Login Here", font=("times new roman", 20, "bold"), bg="white",
                      fg="green").place(x=50, y=30)
        #fram2
        frame2=Frame(frame1,bg="red")
        frame2.place(x=400,y=120,width=250,height=300)
        title2 = Label(frame1, text="Login Here", font=("times new roman", 20, "bold"), bg="white",
                      fg="green").place(x=460, y=120)

        # techbotimage
        self.right = ImageTk.PhotoImage(file="images/tep.png")

        right = Label(frame1, image=self.right, bg="white").place(x=400, y=30, width=200, height=55)
        # email
        email = Label(frame1, text="Email-ID", font=("times new roman", 15, "bold"), bg="white",
                      fg="gray").place(x=50, y=100)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=50, y=130, width=250)
        paasssword = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white",
                           fg="gray").place(x=50, y=200)
        self.txt_pasword = Entry(frame1, show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_pasword.place(x=50, y=230, width=250)
        btn_register = Button(frame1, text="Register new account?",command=self.register_window, bg="white",fg="#800857", font=("times new roman", 15), bd=0,
                           cursor="hand2", ).place(x=50, y=280)
        btn_login = Button(frame1, text="Login Now",command=self.login, bg="blue", font=("times new roman", 15),

                              cursor="hand2", ).place(x=50, y=320)

    def register_window(self):
        self.root.destroy()
        import login


    def login(self):
        if self.txt_email.get()=="" or self.txt_pasword.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="Saket Suman", password="areyoucrazy#76",
                                      database="employ")
                cur = con.cursor()
                cur.execute("select * from employ where email=%s and password=%s",(self.txt_email.get(),self.txt_pasword.get()))
                row = cur.fetchone()
                print(row)
                if row == None:
                    messagebox.showerror("Error", "Invalid USERNAME and Password", parent=self.root)

                else:
                    messagebox.showinfo("success", "welcome", parent=self.root)
                    self.root.destroy()
                    import studentmanagement
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"error due to:{str(es)}", parent=self.root)


root=Tk()
obj=register(root)





root.mainloop()
