# Import the required libraries
from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import pymysql

class Register:
    # Function to create window tkinter with background properties
    def __init__(self,root):
        self.root=root
        # Set title of tkinter frame
        self.root.title("Registration Window") 
        # Set the geometry of tkinter frame
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="black")
        # Define image
        self.bg=Image.open("E:/Thesis/login_database/images/background.jpg")
        self.bg=self.bg.resize((970,700),Image.ANTIALIAS)
        # Add image inside root
        self.bg_resized=ImageTk.PhotoImage(self.bg)
        bg_resized=Label(self.root,image=self.bg_resized,bg="black").place(x=380,y=0)

        # Create a canvas
        #my_canvas = Canvas(self.root, width=700, height=800, bd=0, highlightthickness=0)
        #my_canvas.pack(fill=BOTH, expand=True)
        # Set image in canvas
        #my_canvas.create_image(0, 0, image=bg, anchor="nw")
        
        # Left image
        self.left=Image.open("E:/Thesis/login_database/images/login.jpg")
        self.left=self.left.resize((400,496),Image.ANTIALIAS)
        self.left_resized=ImageTk.PhotoImage(self.left)
        left_resized=Label(self.root,image=self.left_resized,bg="black").place(x=80,y=100)
        
        # Create a frame for input info
        frame1=Frame(self.root, bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        
        # Create entry for frame
        title=Label(frame1,text="REGISTER HERE",font=("time new roman",24,"bold"),bg="white",fg="green").place(x=50,y=30)
        
        # Row 1
        self.var_fname=StringVar()
        f_name=Label(frame1,text="First Name",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_fname).place(x=50,y=130,width=250)

        self.var_lname=StringVar()
        l_name=Label(frame1,text="Last Name",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_lname).place(x=370,y=130,width=250)
 
        # Row 2
        self.var_email=StringVar()
        email=Label(frame1,text="Email",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_email).place(x=50,y=200,width=250)
        
        self.var_contact=StringVar()
        contact=Label(frame1,text="Contact No.",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_contact).place(x=370,y=200,width=250)

        # Row 3
        self.var_cmb_quest=StringVar()
        question=Label(frame1,text="Security Question",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),textvariable=self.var_cmb_quest,state='readonly',justify=CENTER)
        cmb_quest['values']=("Select","Your First Pet Name","Your Birthday","Your Birth Place","Your Best Friend Name")
        cmb_quest.place(x=50,y=270,width=250)
        cmb_quest.current(0)

        self.var_answer=StringVar()
        answer=Label(frame1,text="Answer",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_answer).place(x=370,y=270,width=250)

        # Row 4
        self.var_password=StringVar()
        password=Label(frame1,text="Password",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_password).place(x=50,y=340,width=250)
        
        self.var_cpassword=StringVar()
        cpassword=Label(frame1,text="Confirm Password",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_cpassword).place(x=370,y=340,width=250)

        # Terms & conditions
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times time roman",10,"italic","bold")).place(x=50,y=380)
        
        # Button register
        self.btn_img=Image.open("E:/Thesis/login_database/images/register.jpg")
        self.btn_img=self.btn_img.resize((250,50), Image.ANTIALIAS)
        self.btn=ImageTk.PhotoImage(self.btn_img)
        btn_register=Button(frame1,image=self.btn,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)
        
        # Button login
        btn_login=Button(self.root,text="Sign In",command=self.login_window,font=("times new roman",22,"bold"),bd=0,cursor="hand2",bg="lightblue").place(x=217,y=350,width=180)
    
    # Function to check data input and submit data to database
    def register_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_cmb_quest.get()=="Select" or self.var_answer.get()=="" or self.var_password.get()=="" or self.var_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.var_password.get()!=self.var_cpassword.get():
            messagebox.showerror("Error","Password and Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please agree our Terms & Conditions",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("Select * from employee where email=%s",self.var_email.get())
                # Store the terminal output to a variable
                row=cur.fetchone() 
                if row!=None:
                    messagebox.showerror("Error","User already existed. Please try with another email",parent=self.root)       
                else:
                    cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.var_fname.get(),
                                 self.var_lname.get(),
                                 self.var_contact.get(),
                                 self.var_email.get(),
                                 self.var_cmb_quest.get(),
                                 self.var_answer.get(),
                                 self.var_password.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Confirmation","Successfully Registered",parent=self.root)
                    self.clear()
            except Exception as es: #??
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    # Function to clear info on boxes after submitted data to database
    def clear(self):
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_password.set("")
        self.var_cpassword.set("")
        self.var_cmb_quest.set("")
        self.var_answer.set("")

    # Switch to login mainpage
    def login_window(self):
        self.root.destroy()
        import login
        
# Create an instance of Tkinter Frame
root=Tk()
#Show features of tkinter from Register()
obj=Register(root) 
# Run program until close manually 
root.mainloop()