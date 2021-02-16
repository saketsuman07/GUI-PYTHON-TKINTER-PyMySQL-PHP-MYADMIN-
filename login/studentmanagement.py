from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class student:
    def __init__(self,root):
        self.root=root
        self.root.title("student management")

        self.root.geometry("1350x700+0+0")
        title=Label(self.root,text="student management system",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="red",fg="green")
        title.pack(side=TOP,fill=X)
        #allvariables
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.contact_var=StringVar()
        self.gender_var=StringVar()
        self.dob_var=StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()








        Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_frame.place(x=20,y=100,width=450,height=600)
        #manage frame
        m_title=Label(Manage_frame,text="Manage student",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
        #roll
        lbl_roll=Label(Manage_frame,text="Roll no:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(Manage_frame,textvariable=self.Roll_No_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        #name
        lbl_name = Label(Manage_frame, text="Name:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_frame,textvariable=self.name_var, bd=5, relief=GROOVE, font=("times new roman", 15, "bold"))
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")
        #email
        lbl_Email = Label(Manage_frame, text="Email:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_frame,textvariable=self.email_var, bd=5, relief=GROOVE, font=("times new roman", 15, "bold"))
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")



        #gender
        lbl_Gender = Label(Manage_frame, text="Gender:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(Manage_frame,textvariable=self.gender_var,font=("times new roman", 13, "bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)


        #contact
        lbl_Contact = Label(Manage_frame, text="Contact:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_Contact = Entry(Manage_frame,textvariable=self.contact_var, bd=5, relief=GROOVE, font=("times new roman", 15, "bold"))
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")
        #dob
        lbl_Dob = Label(Manage_frame, text="D.O.B:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_Dob = Entry(Manage_frame,textvariable=self.dob_var, bd=5, relief=GROOVE, font=("times new roman", 15, "bold"))
        txt_Dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")
        #address
        lbl_address = Label(Manage_frame, text="Address:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_Address=Text(Manage_frame,width=30,height=4,font=("",10))
        self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        #btnframe
        btn_frame = Frame(Manage_frame, bd=4, relief=RIDGE, bg="crimson")
        btn_frame.place(x=15, y=500, width=420)
        Add_btn=Button(btn_frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updata_btn=Button(btn_frame,text="Updata",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        delete_btn=Button(btn_frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clear_btn=Button(btn_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)


        #details frame

        details_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        details_frame.place(x=500, y=100, width=800, height=580)
        lbl_Search = Label(details_frame, text="Search by", bg="crimson", fg="white",
                            font=("times new roman", 20, "bold"))
        lbl_Search.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        combo_search = ttk.Combobox(details_frame,textvariable=self.search_by,width=10, font=("times new roman", 13, "bold"), state="readonly")
        combo_search['values'] = ("Roll_no", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)
        txt_Search = Entry(details_frame,textvariable=self.search_txt, bd=5, relief=GROOVE,width=15, font=("times new roman", 10, "bold"))
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        searchbtn = Button(details_frame, text="Search", width=10,pady=5,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(details_frame, text="Show all", width=10,pady=5,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)


   #table frame
        table_frame = Frame(details_frame, bd=4, relief=RIDGE, bg="crimson")
        table_frame.place(x=10, y=70, width=760, height=500)
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.Student_table=ttk.Treeview(table_frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=50)
        self.Student_table.column("name",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            con = pymysql.connect(host="localhost", user="saket", password="areyoucrazy#76", database="stm")
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                              self.name_var.get(),
                                                                              self.email_var.get(),
                                                                              self.gender_var.get(),
                                                                              self.contact_var.get(),
                                                                              self.dob_var.get(),
                                                                              self.txt_Address.get('1.0', END)

                                                                              ))
            con.commit()
            self.fetch_data()
            messagebox.showinfo("success", "registerd succesfull", parent=self.root)
            self.clear()
            con.close()

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="saket", password="areyoucrazy#76", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
            con.close()
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0",END)
    def get_cursor(self,ev):

        corsor_row=self.Student_table.focus()
        content=self.Student_table.item(corsor_row)
        row=content['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END,row[6])
    def update_data(self):
        con = pymysql.connect(host="localhost", user="saket", password="areyoucrazy#76", database="stm")
        cur = con.cursor()
        cur.execute("update  students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s", (
                                                                          self.name_var.get(),
                                                                          self.email_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.contact_var.get(),
                                                                          self.dob_var.get(),
                                                                          self.txt_Address.get('1.0', END),
                                                                          self.Roll_No_var.get()



                                                                          ))
        con.commit()
        self.fetch_data()
        messagebox.showinfo("success", "Updated succesfully", parent=self.root)
        self.clear()
        con.close()

    def delete_data(self):
            con = pymysql.connect(host="localhost", user="saket", password="areyoucrazy#76", database="stm")
            cur = con.cursor()
            cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
            con.commit()

            con.close()
            self.fetch_data()
            messagebox.showinfo("success", "Deleted succesfull", parent=self.root)
            self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="saket", password="areyoucrazy#76", database="stm")
        cur = con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
            con.close()












root=Tk()
ob=student(root)



root.mainloop()