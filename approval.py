from opcode import stack_effect
from tkinter import *
from PIL import Image, ImageTk 
from tkinter import ttk
from tkinter import messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox
import sqlite3
from sqlite3 import Error
import os

class Room_Approval:
    def __init__(self,root):
        self.root=root
        
        #-------------Size of main window-----------------#
        window_width=810
        window_height=480
        
        #-------Position of main window on desktop--------#
        screen_width=self.root.winfo_screenwidth()
        x=(screen_width/2) - (window_width/2)
        self.root.geometry(f"{window_width}x{window_height}+{int(x+82)}+{int(162)}")
        self.root.resizable(False,False)
        
        #-------Disable draging window-------#
        self.root.overrideredirect(True)

        #---Create new text and button to close window---#
        main_frame=Frame(self.root,bg="white",bd=1,relief=RIDGE)
        main_frame.place(x=0,y=0,width=810,height=30)
        
        text=Label(main_frame,text="Room Approval Management",font=("times new roman",15,"bold"),bg="black",fg="gold")
        text.place(x=-1,y=-2,height=30,width=781)
        
        btn=Button(main_frame,text="X",bg="red",command=self.root.destroy)
        btn.place(x=780,y=-2,height=30,width=30)

        #-------Variables for entry boxes-------#
        self.var_firstname=StringVar()
        self.var_lastname=StringVar()
        self.var_gender=StringVar()
        self.var_id=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_bookdate=StringVar()
        self.var_moveindate=StringVar()
        self.var_budgetmin=StringVar()
        self.var_budgetmax=StringVar()
        self.var_typehouse=StringVar()
        self.var_apartment=StringVar()    
        self.var_house=IntVar()
        self.var_room=IntVar()
        self.var_apartmentaddress=StringVar()
        self.var_fee=StringVar()
        self.var_search=StringVar()
        self.var_txt=StringVar()
        
        #------------Label and entrys on LEFT side---------------#
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Approval Details",padx=2,font=("times new roman",13,"bold"))
        labelframeleft.place(x=3,y=30,width=287,height=447)        

        lbl_firstname=Label(labelframeleft,text="Firstname",font=("arial",10),padx=2,pady=5)
        lbl_firstname.grid(row=0,column=0,sticky=W)
        self.entry_firstname=ttk.Entry(labelframeleft,textvariable=self.var_firstname,width=20,font=("arial",10))
        self.entry_firstname.grid(row=0,column=1)

        lbl_lastname=Label(labelframeleft,text="Lastname",font=("arial",10),padx=2,pady=5)
        lbl_lastname.grid(row=1,column=0,sticky=W)
        self.entry_lastname=ttk.Entry(labelframeleft,textvariable=self.var_lastname,width=20,font=("arial",10))
        self.entry_lastname.grid(row=1,column=1)
         
        lbl_gender=Label(labelframeleft,text="Gender",font=("arial",10),padx=2,pady=5)
        lbl_gender.grid(row=2,column=0,sticky=W)
        self.combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",10),width=7,state="readonly")
        self.combo_gender["value"]=("Male","Female","Other")
        self.combo_gender.grid(row=2,column=1,sticky=W,padx=2)
                
        lbl_id=Label(labelframeleft,text="Security ID",font=("arial",10,),padx=2,pady=5)
        lbl_id.grid(row=3,column=0,sticky=W)
        self.entry_id=ttk.Entry(labelframeleft,textvariable=self.var_id,width=20,font=("arial",10))
        self.entry_id.grid(row=3,column=1) 

        lbl_email=Label(labelframeleft,text="Email",font=("arial",10,),padx=2,pady=5)
        lbl_email.grid(row=4,column=0,sticky=W)
        self.entry_email=ttk.Entry(labelframeleft,textvariable=self.var_email,width=20,font=("arial",10))
        self.entry_email.grid(row=4,column=1)  
                
        lbl_phone=Label(labelframeleft,text="Phone",font=("arial",10,),padx=2,pady=5)
        lbl_phone.grid(row=5,column=0,sticky=W)
        self.entry_phone=ttk.Entry(labelframeleft,textvariable=self.var_phone,width=20,font=("arial",10))
        self.entry_phone.grid(row=5,column=1)  
        
        lbl_phone=Label(labelframeleft,text="---  --- --- ---  ---  --- --- ---  ---  --- --- ---  ---",font=("arial",12,"bold"),padx=2)
        lbl_phone.place(x=2,y=179)    

        lbl_moveindate=Label(labelframeleft,text="Move-in Date",font=("arial",10,),padx=2)
        lbl_moveindate.grid(row=6,column=0,sticky=W,pady=(30,0))
        self.entry_moveindate=ttk.Entry(labelframeleft,textvariable=self.var_moveindate,width=20,font=("arial",10))
        self.entry_moveindate.grid(row=6,column=1,pady=(30,0)) 
                
        lbl_budget=Label(labelframeleft,text="Budget (€)",font=("arial",10))
        lbl_budget.grid(row=7,column=0,sticky=W,padx=1,pady=5)
        self.entry_budgetmin=ttk.Entry(labelframeleft,textvariable=self.var_budgetmin,width=6,font=("arial",10))
        self.entry_budgetmin.grid(row=7,column=1,sticky=W)
        lbl_range=Label(labelframeleft,text="-",font=("arial",13))
        lbl_range.place(x=185,y=235) 
        self.entry_budgetmax=ttk.Entry(labelframeleft,textvariable=self.var_budgetmax,width=6,font=("arial",10))
        self.entry_budgetmax.place(x=210,y=237)

        self.checkbutton_typehouse=ttk.Combobox(labelframeleft,textvariable=self.var_typehouse,font=("arial",10),state="readonly",width=14)
        self.checkbutton_typehouse["value"]=("Type_House","Shared_2h_House","Shared_3h_House","Family_1h_House","Family_2h_House")
        self.checkbutton_typehouse.grid(row=8,column=0,sticky=W,padx=4,pady=(5,5))
        self.checkbutton_typehouse.current(0)

        self.checkbutton_apartment=ttk.Combobox(labelframeleft,textvariable=self.var_apartment,font=("arial",10),state="readonly",width=14)
        self.checkbutton_apartment["value"]=("Apartment","Building A","Building B","Building C","Building D","Building E","Building F")
        self.checkbutton_apartment.grid(row=8,column=1,sticky=W,padx=4,pady=(5,5))
        self.checkbutton_apartment.current(0)
            
        lbl_house=Label(labelframeleft,text="House Number",font=("arial",10),pady=5)
        lbl_house.grid(row=9,column=0,sticky=W,padx=1)
        self.combo_house=Entry(labelframeleft,textvariable=self.var_house,font=("arial",10),width=4)
        self.combo_house.place(x=95,y=301)

        lbl_room=Label(labelframeleft,text="Room Number",font=("arial",10),pady=5)
        lbl_room.grid(row=9,column=1,sticky=W,padx=(12,4))
        self.combo_room=Entry(labelframeleft,textvariable=self.var_room,font=("arial",10),width=4)
        self.combo_room.place(x=233,y=301)

        lbl_apartmentaddress=Label(labelframeleft,text="Apartment Address",font=("arial",10),pady=5)
        lbl_apartmentaddress.grid(row=10,column=0,sticky=W,padx=1)
        self.combo_apartmentaddress=Entry(labelframeleft,textvariable=self.var_apartmentaddress,font=("arial",10),width=21)
        self.combo_apartmentaddress.place(x=125,y=330)

        lbl_fee=Label(labelframeleft,text="Fee (€)",font=("arial",10),pady=5)
        lbl_fee.grid(row=11,column=0,sticky=W,padx=1)
        self.combo_fee=Entry(labelframeleft,textvariable=self.var_fee,font=("arial",10),width=7)
        self.combo_fee.place(x=125,y=359)
                                      
        #--------------------btns on BOTTOM side------------------------#
        btn_frame=Frame(labelframeleft,bd=0, relief=RIDGE)
        btn_frame.place(x=0,y=396,width=275,height=28)
                
        btnAdd=Button(btn_frame,text="Update",command=self.update_button,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=(25,15))
        
        btnAdd=Button(btn_frame,text="Remove",command=self.delete_button,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=1,padx=0)            
        
        btnAdd=Button(btn_frame,text="Reset",command=self.reset_button,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=2,padx=15)
        
        #----------------Search Boxes on TOP side-------------------#      
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Approval Management",padx=2,font=("times new roman",13,"bold"))  
        table_frame.place(x=290,y=30,width=517,height=447)

        lblSearchBy=Label(table_frame,font=("arial",10,"bold"),text="Search By",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        combo_search=ttk.Combobox(table_frame,textvariable=self.var_search,font=("arial",10),width=11,state="readonly")
        combo_search["value"]=("Firstname","Lastname","Gender","Security_ID","Email","Phone","Move_in_Date","Budget_Min","Budget_Max","Type_House","Apartment","House","Room","Apartment_Address","Fee")
        combo_search.grid(row=0,column=1,padx=2)
        
        txtSearch=ttk.Entry(table_frame,textvariable=self.var_txt,font=("arial",10),width=26)
        txtSearch.grid(row=0,column=2,padx=2)
        
        #----------------Btns on TOP side-----------------#
        btnSearch=Button(table_frame,text="Search",command=self.search_button,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShowAll=Button(table_frame,text="Show All",command=self.show_all_button,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnShowAll.grid(row=0,column=4,padx=1)
        
        #----------Create Treeview on RIGHT side-----------#
        details_table2=Frame(table_frame,bd=1,relief=RIDGE)
        details_table2.place(x=-1,y=30,width=510,height=393)
        
        scroll_x=ttk.Scrollbar(details_table2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table2,orient=VERTICAL)
        
        self.cust_details_table=ttk.Treeview(details_table2,column=("Firstname","Lastname","Gender","Security_ID","Email","Phone","Move_in_Date","Budget_Min","Budget_Max","Type_House","Apartment","House","Room","Apartment_Address","Fee"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)
        
        self.cust_details_table.column("Firstname",width=65)
        self.cust_details_table.column("Lastname",width=65)
        self.cust_details_table.column("Gender",width=60)
        self.cust_details_table.column("Security_ID",width=80)
        self.cust_details_table.column("Email",width=160)
        self.cust_details_table.column("Phone",width=80)
        self.cust_details_table.column("Move_in_Date",width=90)
        self.cust_details_table.column("Budget_Min",width=75)
        self.cust_details_table.column("Budget_Max",width=75)
        self.cust_details_table.column("Type_House",width=75)
        self.cust_details_table.column("Apartment",width=75)
        self.cust_details_table.column("House",width=45)
        self.cust_details_table.column("Room",width=40)
        self.cust_details_table.column("Apartment_Address",width=130)
        self.cust_details_table.column("Fee",width=40)
        
        self.cust_details_table.heading("Firstname",text="Firstname")
        self.cust_details_table.heading("Lastname",text="Lastname")
        self.cust_details_table.heading("Gender",text="Gender")
        self.cust_details_table.heading("Security_ID",text="Security ID")
        self.cust_details_table.heading("Email",text="Email")
        self.cust_details_table.heading("Phone",text="Phone")
        self.cust_details_table.heading("Move_in_Date",text="Move-in Date")
        self.cust_details_table.heading("Budget_Min",text="Budget Min")
        self.cust_details_table.heading("Budget_Max",text="Budget Max")
        self.cust_details_table.heading("Apartment",text="Apartment")
        self.cust_details_table.heading("Type_House",text="Type House")
        self.cust_details_table.heading("House",text="House")
        self.cust_details_table.heading("Room",text="Room")
        self.cust_details_table.heading("Apartment_Address",text="Apartment_Address")
        self.cust_details_table.heading("Fee",text="Fee")
        
        ttk.Style().configure("Treeview.Heading",font=("Arial",9,"bold"))
        self.cust_details_table["show"]="headings"
        self.cust_details_table.pack(fill=BOTH,expand=1)
        
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.sql_fetch_data()
    
    #-----Fetch data from SQL to Tkinter Treeview-----# 
    def sql_fetch_data(self): 
        conn = sqlite3.connect("E:\Thesis\house\database\house.db")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM renting")
        #----Call/save/take data rows/tuple from SQL----#
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            #-------Delete all rows on Treeview/Create blanks Treeview-----#
            self.cust_details_table.delete(*self.cust_details_table.get_children()) #---*self.ACBD: return list of tuple (rows); get_children(): return list of IDs----#
            #-------Insert data rows/Fetch data/tuple to blanks Treeview------#
            for i in rows:
                self.cust_details_table.insert("",END,value=i)
        conn.commit()
        conn.close()    
    
    #----Fill data into entry boxes-----#  
    def get_cursor(self,event):
        #---------Grab record numbers-----------#
        select_row=self.cust_details_table.focus()
        #---------Grab record values------------#
        content=self.cust_details_table.item(select_row)
        row=content["values"]
        #---------Output entry boxes--------#
        if(row):
            self.var_firstname.set(row[0])
            self.var_lastname.set(row[1])
            self.var_gender.set(row[2])
            self.var_id.set(row[3])
            self.var_email.set(row[4])
            self.var_phone.set(row[5])
            self.var_moveindate.set(row[6])
            self.var_budgetmin.set(row[7])
            self.var_budgetmax.set(row[8])
            self.var_typehouse.set(row[9])   
            self.var_apartment.set(row[10])                                   
            self.var_house.set(row[11])
            self.var_room.set(row[12])
            self.var_apartmentaddress.set(row[13])
            self.var_fee.set(row[14])
        self.entry_firstname.config(state="readonly")
        self.entry_lastname.config(state="readonly")   
        self.combo_gender.config(state="disable")
        self.entry_id.config(state="readonly")   
        self.entry_email.config(state="readonly")   
        self.entry_phone.config(state="readonly")   
        self.combo_apartmentaddress.config(state="readonly")   
        self.combo_fee.config(state="readonly")                                

    #------------------------Btn Search------------------------#
    def search_button(self):
        if self.var_search.get()!="" and self.var_txt.get()!="":
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            conn = sqlite3.connect("E:\Thesis\house\database\house.db")
            my_cursor=conn.execute("SELECT * FROM renting WHERE " + str(self.var_search.get()) + " LIKE ?", (str(self.var_txt.get()) + '%',))   
            rows=my_cursor.fetchall()
            if(len(rows)!=0):
                for data in rows:
                    self.cust_details_table.insert("",END,values=data)  
            my_cursor.close()
            conn.close()
        else:
            messagebox.showwarning("Search","Fill both fields")    
                        
    #---Clear data from entry boxes---#
    def clear(self):
        self.var_firstname.set("")
        self.var_lastname.set("")
        self.var_gender.set("")
        self.var_id.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_bookdate.set("")
        self.var_moveindate.set("") 
        self.var_budgetmin.set("") 
        self.var_budgetmax.set("")
        self.var_typehouse.set("Type_House")
        self.var_apartment.set("Apartment")
        self.var_house.set("")
        self.var_room.set("")
        self.var_apartmentaddress.set("")
        self.var_fee.set("")
        self.var_search.set("")
        self.var_txt.set("")
                
    #----Modify data from entry boxes, update to SQL----#
    def sql_update_data(self):
        if(self.var_firstname.get()=='None' or self.var_firstname.get()==""):
            messagebox.showwarning("Warning","Please choose a customer",parent=self.root)                          
        else:
            try:
                conn = sqlite3.connect("E:\Thesis\house\database\house.db")
                my_cursor=conn.cursor()
                my_cursor.execute("UPDATE renting SET Firstname=NULL,Lastname=NULL,Gender=NULL,Security_ID=NULL,Email=NULL,Phone=NULL,Move_in_Date=NULL,Budget_Min=NULL,Budget_Max=NULL WHERE Security_ID=?",
                    (
                    self.var_id.get(),                  
                    )
                )
                conn.commit()            
                my_cursor.execute("UPDATE renting SET Firstname=?,Lastname=?,Gender=?,Security_ID=?,Email=?,Phone=?,Move_in_Date=?,Budget_Min=?,Budget_Max=? WHERE (Type_House=? AND Apartment=? AND House=? AND Room=?)",
                    (self.var_firstname.get(),
                    self.var_lastname.get(),
                    self.var_gender.get(),
                    self.var_id.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_moveindate.get(),
                    self.var_budgetmin.get(), 
                    self.var_budgetmax.get(),
                    self.var_typehouse.get(),
                    self.var_apartment.get(),
                    self.var_house.get(),
                    self.var_room.get()                     
                    )
                )
                conn.commit()
                self.sql_fetch_data()
                self.clear()        
                conn.close()
                messagebox.showinfo("Update","Customer details have been updated",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Warning",f"Something went wrong:{str(es)}",parent=self.root)             
    
    #----Delete data from entry boxes, update to SQL---#
    def sql_delete_data(self):
        if(self.var_firstname.get()=="None" or self.var_firstname.get()==""):
            messagebox.showwarning("Warning","Please choose a customer to remove their renting",parent=self.root)
        else:
            mess_delete=messagebox.askyesno("House Management System","Are you sure to remove this customer from house?",parent=self.root)
            if(mess_delete==1):
                conn = sqlite3.connect("E:\Thesis\house\database\house.db")
                my_cursor=conn.cursor()
                my_cursor.execute("UPDATE renting SET Firstname=NULL,Lastname=NULL,Gender=NULL,Security_ID=NULL,Email=NULL,Phone=NULL,Move_in_Date=NULL,Budget_Min=NULL,Budget_Max=NULL WHERE Security_ID=?",
                                  (
                                    self.var_id.get(),                                       
                                  )                       
                                 )                      
                conn.commit() 
                self.sql_fetch_data()
                self.clear()
                conn.close()
            messagebox.showinfo("Delete Succesfully","Customer booking was already removed",parent=self.root) 
    
    def update_button(self):
        self.sql_update_data()    
    
    def delete_button(self):
        self.sql_delete_data()
            
    def reset_button(self):
        self.clear()
    
    def search_button(self):
        if(self.var_search.get()!="" and self.var_txt.get()!=""):
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            conn = sqlite3.connect("E:\Thesis\house\database\house.db")
            my_cursor=conn.execute("SELECT * FROM renting WHERE " + str(self.var_search.get()) + " LIKE ?", (str(self.var_txt.get()) + '%',))   
            rows=my_cursor.fetchall()
            if(len(rows)!=0):
                for data in rows:
                    self.cust_details_table.insert("",END,values=data)  
            my_cursor.close()
            conn.close()
        else:
            messagebox.showwarning("Search","Fill both fields",parent=self.root)    

    #------------------Btn Show_All---------------#
    def show_all_button(self):
        self.sql_fetch_data() 
        
if __name__ == "__main__":
    root=Tk()
    obj=Room_Approval(root)
    root.mainloop()        