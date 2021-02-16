from tkinter import*
from tkinter import ttk,messagebox
from PIL import ImageTk,Image

import pymysql
class login:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.bg=ImageTk.PhotoImage(file = "images/home.jpg")

        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #leftimage
        self.left = ImageTk.PhotoImage(file="images/kkr.jpg")

        left=Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)
        #frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        title=Label(frame1,text="Registere Here",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        #techbotimage
        self.right = ImageTk.PhotoImage(file="images/tep.png")

        right = Label(frame1, image=self.right,bg="white").place(x=400, y=30, width=200, height=55)
        #variable
        #self.var_fname=StringVar() second option

        fname = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white",
                      fg="gray").place(x=50, y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)
        #lastname
        lname = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white",
                      fg="gray").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)
        #CONTACT
        contact = Label(frame1, text="Contact no", font=("times new roman", 15, "bold"), bg="white",
                      fg="gray").place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)
        # email
        email = Label(frame1, text="Email-ID", font=("times new roman", 15, "bold"), bg="white",
                      fg="gray").place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)
        # row3
        question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white",
                        fg="gray").place(x=50, y=240)
        self.cmb_question = ttk.Combobox(frame1, font=("times new roman", 13),state='readonly',justify=CENTER)
        self.cmb_question['values']=("Slect","your first teacher name","your birth place","your frndname")
        self.cmb_question.place(x=50, y=270, width=250)
        self.cmb_question.current(0)
        # anser
        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white",
                      fg="gray").place(x=370, y=240)
        self.txt_ans = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_ans.place(x=370, y=270, width=250)
        # row4
        paasssword = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white",
                        fg="gray").place(x=50, y=310)
        self.txt_pasword = Entry(frame1,show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_pasword.place(x=50, y=340, width=250)
        # cpassword
        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                      fg="gray").place(x=370, y=310)
        self.txt_cpassword = Entry(frame1,show="* ",font=("times new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=370, y=340, width=250)
        self.txt_title=Label(frame1,text="Already have a Account?",bg="white",fg="#800857", font=("times new roman", 13)).place(x=370,y=380)
        #btn login
        btn_login = Button(frame1, text="Login Now", bg="red",command=self.login_window, font=("times new roman", 15), bd=0,
                              cursor="hand2", ).place(x=370, y=420)


        #check
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I agree Terms&conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman" ,12)).place(x=50,y=380)
        #self.btn_img=ImageTk.PhotoImage(file = "images/btn.png")
        btn_register=Button(frame1,text="Register Now",bg="green",font=("times new roman",15),bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)

    def login_window(self):
        self.root.destroy()
        import registration
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.txt_pasword.delete(0,END)
        self.cmb_question.current(0)
        self.txt_ans.delete(0,END)
    def register_data(self):

            if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.txt_contact.get()=="" or self.txt_pasword.get()=="" or self.txt_cpassword.get()=="" or self.txt_ans.get()=="" or self.cmb_question.get()=="Select":

                messagebox.showerror("Error","All Fields are required",parent=self.root)
            elif self.txt_pasword.get()!= self.txt_cpassword.get():
                messagebox.showerror("Error", "Password dont match", parent=self.root)
            elif self.var_chk.get()==0:
                messagebox.showerror("Error", "Agree terms &conditions", parent=self.root)
            else:
                try:
                    con=pymysql.connect(host="localhost",user="Saket Suman",password="areyoucrazy#76",database="employ")
                    cur=con.cursor()
                    cur.execute("select * from employ where email=%s",self.txt_email.get())
                    row=cur.fetchone()
                    print(row)
                    if row !=None:
                        messagebox.showerror("Error", "User already Exists try other email", parent=self.root)
                    else:
                        cur.execute(
                            "insert into employ (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                            (self.txt_fname.get(),
                             self.txt_lname.get(),
                             self.txt_contact.get(),
                             self.txt_email.get(),
                             self.cmb_question.get(),
                             self.txt_ans.get(),
                             self.txt_pasword.get()

                             )

                            )
                        con.commit()
                        con.close()


                        messagebox.showinfo("success", "registerd succesfull", parent=self.root)
                        self.clear()
                except Exception as es:
                    messagebox.showerror("Error", f"error due to:{str(es)}", parent=self.root)







       # btn1 = Button(self.root, text="Sign In", bg="white", font=("times new roman", 15), bd=0, cursor="hand2").place(
           # x=250, y=460)
       # btn1 = Label(self.root, text="Mr Techbot",  font=("times new roman", 15)).place(
            #x=250, y=400)







root=Tk()
obj=login(root)





root.mainloop()
