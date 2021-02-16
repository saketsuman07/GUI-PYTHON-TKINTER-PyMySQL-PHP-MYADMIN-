from tkinter import*
from PIL import ImageTk,Image
class app:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.bg=ImageTk.PhotoImage(file = "images/home.jpg")

        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)



root=Tk()
obj=app(root)





root.mainloop()