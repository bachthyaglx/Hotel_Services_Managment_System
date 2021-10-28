from tkinter import *
from tkinter import font
from PIL import Image, ImageTk, ImageDraw
from datetime import *
import time
from math import *
from time import strftime
import pymysql
from tkinter import messagebox, ttk

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="black")

        #----------Background Colors---------------
        left_lbl=Label(self.root,bg="black",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)
        
        self.theme=ImageTk.PhotoImage(file="E:/login_database/images/theme.jpg")
        right_lbl=Label(self.root,image=self.theme,bg="black")
        right_lbl.place(x=610,y=0)

        #-----------Login Frames----------------
        login_frame=Frame(self.root,bg="black")
        login_frame.place(x=193,y=100,width=542,height=500)

        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="black",fg="#08A3D2").place(x=250,y=50)
        
        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="black",fg="lightgray").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=290,height=35)

        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="black",fg="lightgray").place(x=250,y=250)
        self.txt_pass_=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_pass_.place(x=250,y=280,width=290,height=35)

        # Create button register, login, forget password
        btn_reg=Button(login_frame,text="Register new account?",command=self.register_window,font=("times new roman",13),bg="black",bd=0,fg="#B00857",cursor="hand2").place(x=250,y=320)
        btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman",20,"bold"),fg="white",bg="#B00857",cursor="hand2").place(x=250,y=360,height=40,width=180)        
        btn_forget=Button(login_frame,text="Forget password?",command=self.forget,font=("times new roman",13),bg="black",bd=0,fg="red",cursor="hand2").place(x=415,y=320)
        
        #-----------Clock Frame-------------
        self.lbl=Label(self.root,bg="black",bd=0)
        self.lbl.place(x=90,y=120,height=450,width=350)
        self.working()
        self.digital_clock()

    # Function to create clock frame
    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),"black")
        draw=ImageDraw.Draw(clock)

        # Create clock image
        bg=Image.open("E:/login_database/images/clock_background.jpg")
        bg=bg.resize((350,350),Image.ANTIALIAS)
        clock.paste(bg,(20,35))

        # Formula to rotate the clock
        # angle_in_radians = angle_in_degrees*math.pi/180
        # line_length = 100
        # center_x = 250
        # center_y = 250
        # end_x = center_x + line_length*math.cos(angle_in_radians)
        # end_y = center_y + line_length*math.sin(angle_in_radians)
        
        # Create hour line image
        # x1,y1,x2,xy2
        origin=200,190
        draw.line((origin,200+80*sin(radians(hr)),190-50*cos(radians(hr))),fill="red",width=5)
        # Create min line image
        draw.line((origin,200+80*sin(radians(min_)),190-80*cos(radians(min_))),fill="yellow",width=3)
        # Create sec line image
        draw.line((origin,200+65*sin(radians(sec_)),190-100*cos(radians(sec_))),fill="white",width=2)
        # Create the center point of clock
        draw.ellipse((195,187,205,200),fill="lightgreen")
        clock.save("E:/login_database/images/clock_new.jpg")
    
    # Function to create function of clock
    def working(self):
        h=datetime.now().time().hour  
        m=datetime.now().time().minute  
        s=datetime.now().time().second 

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360

        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="E:/login_database/images/clock_new.jpg")
        self.lbl.config(image=self.img)
        # time delay of 1000 milliseconds
        self.lbl.after(200,self.working)

    # Create digital clock
    def digital_clock(self):   
        #time format --- Date day/month/year \n hour:min:sec 
        time_string=strftime('%A %d/%m/%y\n%H:%M:%S') 
        digi_lbl=Label(self.root,font=("times new roman",20,"bold"),bg="black",fg="#12ff05")
        digi_lbl.place(x=160,y=550,height=55,width=200)
        digi_lbl.config(text=time_string)
        # time delay of 1000 milliseconds 
        digi_lbl.after(200,self.digital_clock)
    
    # Switch to register mainpage
    def register_window(self):
        self.root.destroy()
        import register

    # Switch to forget password mainpage
    def forget(self):
        self.root1=Toplevel()
        self.root1.title("Forget Password")
        self.root1.geometry("350x450+443+120")
        self.root1.config(bg="white")
        # ???
        self.root1.focus_force()
        self.root1.grab_set()

        t=Label(self.root1,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)

        email=Label(self.root1,text="Email",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=70)
        self.txt_email=Entry(self.root1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=50,y=100,width=250)

        self.var_cmb_quest=StringVar()
        question=Label(self.root1,text="Security Question",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=150)
        cmb_quest=ttk.Combobox(self.root1,font=("times new roman",13),textvariable=self.var_cmb_quest,state='readonly',justify=CENTER)
        cmb_quest['values']=("Select","Your First Pet Name","Your Birthday","Your Birth Place","Your Best Friend Name")
        cmb_quest.place(x=50,y=180,width=250)
        cmb_quest.current(0)

        answer=Label(self.root1,text="Answer",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=230)
        self.txt_answer=Entry(self.root1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=50,y=260,width=250)

        new_pass=Label(self.root1,text="New Password",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_new_pass=Entry(self.root1,font=("times new roman",15),bg="lightgray")
        self.txt_new_pass.place(x=50,y=340,width=250)

        btn_change_password=Button(self.root1,command=self.forget_password,text="Reset Password",bg="green",fg="white",font=("Times New Roman",15,"bold")).place(x=100,y=390)
    
    # Function to execute/check forget password
    def forget_password(self):
        if self.txt_email.get()=="" or self.var_cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",(self.txt_email.get()))
                # Store the terminal output to a variable 
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid email. Please register new account!",parent=self.root)
                else:
                    cur.execute("update employee set question=%s,answer=%s,password=%s where email=%s",
                                (self.var_cmb_quest.get(),
                                 self.txt_answer.get(),
                                 self.txt_new_pass.get(),
                                 self.txt_email.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Confirmation","Changed password successfully",parent=self.root)
                    self.root1.destroy()
                    self.reset()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    
    # Function to reset boxes
    def reset(self):
        self.var_cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)   
        
    # Create login with database
    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",(self.txt_email.get(),self.txt_pass_.get()))
                # Store the terminal output to a variable 
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME or PASSWORD",parent=self.root)
                else:
                    messagebox.showinfo("Success","Wellcome",parent=self.root)
                    self.root.destroy() 
                    # import file database management 
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

root=Tk()
obj=Login(root)
root.mainloop()