from distutils.command.config import config
import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from booking import Room_Booking
from approval import Room_Approval
from apartment import Apartment_Availability
import os,os.path

class HouseManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Housing Management System")     
        #-------------Size of main window-----------------#
        self.window_width=960
        self.window_height=610
        
        #-------Position of main window on desktop--------#
        self.screen_width=self.root.winfo_screenwidth()
        self.screen_height=self.root.winfo_screenheight()
        
        self.x=(self.screen_width/2) - (self.window_width/2)
        self.y=(self.screen_height/2) - (self.window_height/2)
        
        self.root.resizable(False,False)
        
        #---------------Default not-existing window----------------#
        self.new_window=None
        
        #--------Run functionality of not-allow moving window-------#
        self.fix_pos()
        
        #-------------------------Top-------------------------#
        img1=Image.open("E:\Thesis\house\hotel_images\hotel-names.jpg")
        img1=img1.resize((810,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg1=Label(self.root,image=self.photoimg1,bd=1,relief=RIDGE)
        lblimg1.place(x=75,y=-50,width=960,height=200)
        
        #------------------------Logo-------------------------#
        img2=Image.open("E:/Thesis/house/hotel_images/user_icon.png")
        img2=img2.resize((100,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg2=Label(self.root,image=self.photoimg2,bd=1,relief=RIDGE)
        lblimg2.place(x=0,y=0,width=150,height=100)

        #-------------------Title------------------------#
        lbl_title=Label(self.root,text="HOUSE MANAGEMENT SYSTEM",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=100,width=962,height=30)
        
        lbl_user=Label(lbl_title,text="Hi ",font=("times new roman",12,"bold"),bg="black",fg="lightgreen")
        lbl_user.grid(row=0,column=0)
        
        #----------------Open file to read username and find firstname/lastname by that username-------------#
        if(os.path.exists("E:/Thesis/house/temp_username.txt")==True):
            self.file=open("E:/Thesis/house/temp_username.txt","r")
            content=self.file.read()
            self.file.close()
            con=sqlite3.connect("E:\Thesis\house\database\house.db")
            cur=con.cursor()
            cur.execute("SELECT Firstname,Lastname FROM customer WHERE Email=?",(content,))
            result=cur.fetchone()
            self.username=result[0] + " " + result[1]
            #---------------Label for username login----------------#
            lbl_user=Label(lbl_title,text=self.username,font=("times new roman",12,"bold","italic"),bg="black",fg="lightpink")
            lbl_user.grid(row=0,column=1)
        
        #-------------------Main Frame-------------------#
        main_frame=Frame(self.root,bd=1,relief=RIDGE,bg="black")
        main_frame.place(x=0,y=130,width=960,height=480)
        
        #-------------------Menu-------------------------#
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=150)
        
        #-------------------btn Frame--------------------#
        #btn_frame=Frame(main_frame,bd=1,relief=RIDGE)
        #btn_frame.place(x=0,y=35,width=180,height=190)
        
        profile_btn=Button(main_frame,text="PROFILE",command=self.customer_list,font=("times new roman",10,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        profile_btn.place(x=0,y=30,width=150)
        
        room_btn=Button(main_frame,text="BOOKING",command=self.customer_order,font=("times new roman",10,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        room_btn.place(x=0,y=60,width=150)

        invoice_btn=Button(main_frame,text="INVOICE",command=self.customer_approval,font=("times new roman",10,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        invoice_btn.place(x=0,y=90,width=150)
        
        status_btn=Button(main_frame,text="STATUS",command=self.customer_approval,font=("times new roman",10,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        status_btn.place(x=0,y=120,width=150)
        
        announcement_btn=Button(main_frame,text="ANNOUNCEMENT",command=self.log_out,font=("times new roman",10,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        announcement_btn.place(x=0,y=150,width=150)

        apartments_btn=Button(main_frame,text="APARTMENTS",command=self.apartment_availability,font=("times new roman",10,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        apartments_btn.place(x=0,y=180,width=150)
                
        logout_btn=Button(main_frame,text="LOGOUT",command=self.log_out,font=("times new roman",10,"bold"),bg="black",fg="gold",bd=4,cursor="hand2")
        logout_btn.place(x=0,y=210,width=150)

        #--------------------Right side image-----------------------#
        img3=Image.open("E:\Thesis\house\hotel_images\sealight.jpg")
        img3=img3.resize((810,480),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg3=Label(main_frame,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg3.place(x=150,y=0,width=810,height=480)
        
    #---------Not allow moving window---------#   
    def fix_pos(self):
        root.bind('<Configure>', self.stay_at)
        
    def stay_at(self,event):
        root.geometry(f"{self.window_width}x{self.window_height}+{int(self.x)}+{int(0)}")   
    
    #---------Manage buttons---------#    
    def customer_list(self):
        if(self.new_window!=None):
            self.new_window.destroy()
        self.new_window=Toplevel(self.root)
        self.new_window.wm_attributes("-topmost",1)
        self.app=Cust_Win(self.new_window)
        
    def customer_order(self):
        if(self.new_window!=None):
            self.new_window.destroy()
        self.new_window=Toplevel(self.root)
        self.new_window.wm_attributes("-topmost", 1)
        self.app=Room_Booking(self.new_window)
        
    def customer_approval(self):
        if(self.new_window!=None):
            self.new_window.destroy()        
        self.new_window=Toplevel(self.root)
        self.new_window.wm_attributes("-topmost", 1)
        self.app=Room_Approval(self.new_window)
    
    def apartment_availability(self):
        if(self.new_window!=None):
            self.new_window.destroy()        
        self.new_window=Toplevel(self.root)
        self.new_window.wm_attributes("-topmost", 1)
        self.app=Apartment_Availability(self.new_window)
    
    def log_out(self):
        if(os.path.exists("E:/Thesis/house/temp_username.txt")==True):
            os.remove("E:/Thesis/house/temp_username.txt")
        self.root.destroy()
           
if __name__ == "__main__":
    root=Tk()
    obj=HouseManagementSystem(root)
    root.mainloop()