from distutils.command.config import config
from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from booking import Room_Booking
from approval import Room_Approval
from apartment import Apartment_Availability

class HouseManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Housing Management System")     
        #-------------Size of main window-----------------#
        window_width=960
        window_height=610
        
        #-------Position of main window on desktop--------#
        screen_width=self.root.winfo_screenwidth()
        screen_height=self.root.winfo_screenheight()
        
        x=(screen_width/2) - (window_width/2)
        y=(screen_height/2) - (window_height/2)
        
        self.root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(0)}")
        self.root.resizable(False,False)
        
        #-------------------Top------------------------#
        img1=Image.open("E:\Thesis\house\hotel_images\hotel-names.jpg")
        img1=img1.resize((810,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg1=Label(self.root,image=self.photoimg1,bd=1,relief=RIDGE)
        lblimg1.place(x=75,y=-50,width=960,height=200)
        
        #-------------------Logo-------------------------#
        img2=Image.open("E:\Thesis\house\hotel_images\hacker.jpg")
        img2=img2.resize((150,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg2=Label(self.root,image=self.photoimg2,bd=1,relief=RIDGE)
        lblimg2.place(x=0,y=0,width=150,height=100)

        #-------------------Title------------------------#
        lbl_title=Label(self.root,text="HOUSE MANAGEMENT SYSTEM",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=100,width=960,height=30)


        #-------------------Main Frame-------------------#
        main_frame=Frame(self.root,bd=1,relief=RIDGE)
        main_frame.place(x=0,y=130,width=960,height=480)
        
        #-------------------Menu-------------------------#
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=150)
        
        #-------------------btn Frame--------------------#
        #btn_frame=Frame(main_frame,bd=1,relief=RIDGE)
        #btn_frame.place(x=0,y=35,width=180,height=190)
        
        cust_btn=Button(main_frame,text="CUSTOMER",command=self.customer_list,font=("times new roman",10,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        cust_btn.place(x=0,y=30,width=150)
        
        room_btn=Button(main_frame,text="BOOKING",command=self.customer_order,font=("times new roman",10,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        room_btn.place(x=0,y=60,width=150)

        details_btn=Button(main_frame,text="APPROVAL",command=self.customer_approval,font=("times new roman",10,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        details_btn.place(x=0,y=90,width=150)
        
        report_btn=Button(main_frame,text="APARTMENTS",command=self.apartment_availability,font=("times new roman",10,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        report_btn.place(x=0,y=120,width=150)

        logout_btn=Button(main_frame,text="LOGOUT",command=self.log_out,font=("times new roman",10,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        logout_btn.place(x=0,y=150,width=150)

        #--------------------Right side image-----------------------#
        img3=Image.open("E:\Thesis\house\hotel_images\sealight.jpg")
        img3=img3.resize((810,480),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg3=Label(main_frame,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg3.place(x=150,y=0,width=810,height=480)
        
        #--------------------Down images-----------------------------#
        img4=Image.open("E:\Thesis\house\hotel_images\houseD.jpeg")
        img4=img4.resize((150,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        lblimg4=Label(main_frame,image=self.photoimg4,bd=1,relief=RIDGE)
        lblimg4.place(x=0,y=180,width=150,height=150)        

        img5=Image.open("E:\Thesis\house\hotel_images\houseE.jpg")
        img5=img5.resize((150,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        lblimg5=Label(main_frame,image=self.photoimg5,bd=1,relief=RIDGE)
        lblimg5.place(x=0,y=330,width=150,height=150)

    def customer_list(self):
        self.new_window=Toplevel(self.root)
        self.new_window.wm_attributes("-topmost", 1)
        self.app=Cust_Win(self.new_window)
    
    def customer_order(self):
        self.new_window=Toplevel(self.root)
        self.new_window.wm_attributes("-topmost", 1)
        self.app=Room_Booking(self.new_window)
        
    def customer_approval(self):
        self.new_window=Toplevel(self.root)
        self.new_window.wm_attributes("-topmost", 1)
        self.app=Room_Approval(self.new_window)
    
    def apartment_availability(self):
        self.new_window=Toplevel(self.root)
        self.new_window.wm_attributes("-topmost", 1)
        self.app=Apartment_Availability(self.new_window)
    
    def log_out(self):
        self.root.destroy()
        
           
if __name__ == "__main__":
    root=Tk()
    obj=HouseManagementSystem(root)
    root.mainloop()