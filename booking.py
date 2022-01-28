from distutils import command
from tkinter import *
from tokenize import String
from PIL import Image, ImageTk 
from tkinter import ttk
from tkinter import messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox
import sqlite3
from sqlite3 import Error
import os

class Room_Booking:
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
        
        text=Label(main_frame,text="Booking Management",font=("times new roman",15,"bold"),bg="black",fg="gold")
        text.place(x=-1,y=-2,height=30,width=781)
        
        btn=Button(main_frame,text="X",bg="red",command=self.root.destroy)
        btn.place(x=780,y=-2,height=30,width=30)
        
        #-------Variables for entry boxes-------#
        self.var_firstname=StringVar()
        self.var_lastname=StringVar()
        self.var_gender=StringVar()
        self.var_martial=StringVar()
        self.var_nationality=StringVar()
        self.var_id=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_bookdate=StringVar()
        self.var_moveindate=StringVar()
        self.var_2hshare=StringVar()
        self.var_3hshare=StringVar()
        self.var_1hfamily=StringVar()
        self.var_2hfamily=StringVar()
        self.var_budgetmin=StringVar()
        self.var_budgetmax=StringVar()
        self.var_budgetmin_entry=StringVar()
        self.var_budgetmax_entry=StringVar()
        self.var_buildingA=StringVar()
        self.var_buildingB=StringVar()
        self.var_buildingC=StringVar()
        self.var_buildingD=StringVar()
        self.var_buildingE=StringVar()
        self.var_buildingF=StringVar()
        self.var_typehouse=StringVar()
        self.var_apartment=StringVar()
        self.var_typehouse_entry=StringVar()
        self.var_apartment_entry=StringVar()        
        self.var_house=IntVar()
        self.var_room=IntVar()
        self.var_apartmentaddress=StringVar()
        self.var_search=StringVar()
        self.var_txt=StringVar()
        
        #------------Booking Details Frame---------------#
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Booking Details",padx=2,font=("times new roman",13,"bold"))
        labelframeleft.place(x=3,y=30,width=287,height=447)        

        lbl_firstname=Label(labelframeleft,text="Firstname",font=("arial",10),padx=2,pady=3)
        lbl_firstname.grid(row=0,column=0,sticky=W)
        self.entry_firstname=ttk.Entry(labelframeleft,textvariable=self.var_firstname,width=20,font=("arial",10))
        self.entry_firstname.grid(row=0,column=1)

        lbl_lastname=Label(labelframeleft,text="Lastname",font=("arial",10),padx=2,pady=3)
        lbl_lastname.grid(row=1,column=0,sticky=W)
        self.entry_lastname=ttk.Entry(labelframeleft,textvariable=self.var_lastname,width=20,font=("arial",10))
        self.entry_lastname.grid(row=1,column=1)
         
        lbl_gender=Label(labelframeleft,text="Gender",font=("arial",10),padx=2,pady=3)
        lbl_gender.grid(row=2,column=0,sticky=W)
        self.combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",10),width=7,state="readonly")
        self.combo_gender["value"]=("Male","Female","Other")
        self.combo_gender.grid(row=2,column=1,sticky=W,padx=2)
                
        lbl_id=Label(labelframeleft,text="Security ID",font=("arial",10,),padx=2,pady=3)
        lbl_id.grid(row=3,column=0,sticky=W)
        self.entry_id=ttk.Entry(labelframeleft,textvariable=self.var_id,width=20,font=("arial",10))
        self.entry_id.grid(row=3,column=1) 

        lbl_email=Label(labelframeleft,text="Email",font=("arial",10,),padx=2,pady=3)
        lbl_email.grid(row=4,column=0,sticky=W)
        self.entry_email=ttk.Entry(labelframeleft,textvariable=self.var_email,width=20,font=("arial",10))
        self.entry_email.grid(row=4,column=1)  
                
        lbl_phone=Label(labelframeleft,text="Phone",font=("arial",10,),padx=2,pady=3)
        lbl_phone.grid(row=5,column=0,sticky=W)
        self.entry_phone=ttk.Entry(labelframeleft,textvariable=self.var_phone,width=20,font=("arial",10))
        self.entry_phone.grid(row=5,column=1)  
        
        lbl_phone=Label(labelframeleft,text="---  --- --- ---  ---  --- --- ---  ---  --- --- ---  ---",font=("arial",12,"bold"),padx=2)
        lbl_phone.place(x=2,y=158)
               
        lbl_bookdate=Label(labelframeleft,text="Booking Date",font=("arial",10,))
        lbl_bookdate.grid(row=6,column=0,sticky=W,padx=2,pady=(30,0))
        self.entry_bookdate=ttk.Entry(labelframeleft,textvariable=self.var_bookdate,width=20,font=("arial",10))
        self.entry_bookdate.grid(row=6,column=1,padx=2,pady=(30,0))      

        lbl_moveindate=Label(labelframeleft,text="Move-in Date",font=("arial",10,),padx=2,pady=3)
        lbl_moveindate.grid(row=7,column=0,sticky=W)
        self.entry_moveindate=ttk.Entry(labelframeleft,textvariable=self.var_moveindate,width=20,font=("arial",10))
        self.entry_moveindate.grid(row=7,column=1) 

        self.checkbutton_2hshare=Checkbutton(labelframeleft,text="2h-shared house",variable=self.var_2hshare,onvalue="x",offvalue="",font=("arial",10),padx=2)
        self.checkbutton_2hshare.grid(row=8,column=0)

        self.checkbutton_3hshare=Checkbutton(labelframeleft,text="3h-shared house",variable=self.var_3hshare,onvalue="x",offvalue="",font=("arial",10))
        self.checkbutton_3hshare.grid(row=8,column=1,sticky=W)

        self.checkbutton_1hfamily=Checkbutton(labelframeleft,text="1h-family house",variable=self.var_1hfamily,onvalue="x",offvalue="",font=("arial",10),padx=2)
        self.checkbutton_1hfamily.grid(row=9,column=0,sticky=W)

        self.checkbutton_2hfamily=Checkbutton(labelframeleft,text="2h-family house",variable=self.var_2hfamily,onvalue="x",offvalue="",font=("arial",10),pady=3)
        self.checkbutton_2hfamily.grid(row=9,column=1,sticky=W)
        
        lbl_budget=Label(labelframeleft,text="Budget (€)",font=("arial",10),padx=2)
        lbl_budget.grid(row=10,column=0,sticky=W)
        self.entry_budgetmin=ttk.Entry(labelframeleft,textvariable=self.var_budgetmin,width=6,font=("arial",10))
        self.entry_budgetmin.grid(row=10,column=1,sticky=W)
        lbl_range=Label(labelframeleft,text="-",font=("arial",15))
        lbl_range.place(x=185,y=285) 
        self.entry_budgetmax=ttk.Entry(labelframeleft,textvariable=self.var_budgetmax,width=6,font=("arial",10))
        self.entry_budgetmax.place(x=210,y=290)

        self.checkbutton_buildingA=Checkbutton(labelframeleft,text="Building A",variable=self.var_buildingA,onvalue="x",offvalue="",font=("arial",10))
        self.checkbutton_buildingA.grid(row=11,column=0,sticky=W,padx=1)

        self.checkbutton_buildingB=Checkbutton(labelframeleft,text="Building B",variable=self.var_buildingB,onvalue="x",offvalue="",font=("arial",10))
        self.checkbutton_buildingB.place(x=90,y=312)

        self.checkbutton_buildingC=Checkbutton(labelframeleft,text="Building C",variable=self.var_buildingC,onvalue="x",offvalue="",font=("arial",10))
        self.checkbutton_buildingC.place(x=180,y=311)

        self.checkbutton_buildingD=Checkbutton(labelframeleft,text="Building D",variable=self.var_buildingD,onvalue="x",offvalue="",font=("arial",10),pady=3)
        self.checkbutton_buildingD.grid(row=12,column=0,sticky=W)
        
        self.checkbutton_buildingE=Checkbutton(labelframeleft,text="Building E",variable=self.var_buildingE,onvalue="x",offvalue="",font=("arial",10),padx=2)
        self.checkbutton_buildingE.place(x=89,y=340)

        self.checkbutton_buildingF=Checkbutton(labelframeleft,text="Building F",variable=self.var_buildingF,onvalue="x",offvalue="",font=("arial",10))
        self.checkbutton_buildingF.place(x=180,y=339)      

        lbl_house=Label(labelframeleft,text="House Number",font=("arial",10),padx=2)
        lbl_house.grid(row=13,column=0,sticky=W)
        self.combo_house=Entry(labelframeleft,textvariable=self.var_house,font=("arial",10),width=4)
        self.combo_house.place(x=95,y=369)

        lbl_room=Label(labelframeleft,text="Room Number",font=("arial",10))
        lbl_room.grid(row=13,column=1,sticky=W,padx=(20,4))
        self.combo_room=Entry(labelframeleft,textvariable=self.var_room,font=("arial",10),width=4)
        self.combo_room.place(x=240,y=369)
                      
        #--------------------btns on BOTTOM side------------------------#
        btn_frame=Frame(labelframeleft,bd=0, relief=RIDGE)
        btn_frame.place(x=0,y=396,width=275,height=28)
        
        btnAdd=Button(btn_frame,text="Approve",command=self.approve_button,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=15)
        
        btnAdd=Button(btn_frame,text="Cancel",command=self.cancel_button,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=1,padx=10)            
        
        btnAdd=Button(btn_frame,text="Reset",command=self.clear,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=3,padx=15)

    #-------------------------------------Booking Management System-------------------------------------------------#
        #----------------Search Boxes on TOP side-------------------#      
        table_frame1=LabelFrame(self.root,bd=2,relief=RIDGE,text="Waiting List",padx=2,font=("times new roman",12,"bold"))  
        table_frame1.place(x=290,y=30,width=517,height=1500)

        lblSearchBy=Label(table_frame1,font=("arial",10,"bold"),text="Search By",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        combo_search=ttk.Combobox(table_frame1,textvariable=self.var_search,font=("arial",10),width=11,state="readonly")
        combo_search["value"]=("Firstname","Lastname","Gender","Martial_Status","Nationality","Security_ID","Email","Phone","City","Postcode","Address","Password")
        combo_search.grid(row=0,column=1,padx=2)
        
        txtSearch=ttk.Entry(table_frame1,textvariable=self.var_txt,font=("arial",10),width=26)
        txtSearch.grid(row=0,column=2,padx=2)
        
        #----------------Btns on TOP side-----------------#        
        btnSearch1=Button(table_frame1,text="Search",command=self.search_button1,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnSearch1.grid(row=0,column=3,padx=1)
        
        btnShowAll1=Button(table_frame1,text="Show All",command=self.show_all_button1,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnShowAll1.grid(row=0,column=4,padx=1)
                
        #----------Create Treeview on RIGHT side-----------#
        details_table1=Frame(table_frame1,bd=1,relief=RIDGE)
        details_table1.place(x=-1,y=30,width=510,height=142)
        
        scroll_x1=ttk.Scrollbar(details_table1,orient=HORIZONTAL)
        scroll_y1=ttk.Scrollbar(details_table1,orient=VERTICAL)
        
        self.cust_details_table1=ttk.Treeview(details_table1,column=("Firstname","Lastname","Gender","Martial_Status","Nationality","Security_ID","Email","Phone","City","Postcode","Address","Password","Booking_Date","Move_in_Date","Shared_2h_House","Shared_3h_House","Family_1h_House","Family_2h_House","Budget_Min","Budget_Max","Building_A","Building_B","Building_C","Building_D","Building_E","Building_F"),xscrollcommand=scroll_x1.set,yscrollcommand=scroll_y1.set)
        scroll_x1.pack(side=BOTTOM,fill=X)
        scroll_y1.pack(side=RIGHT,fill=Y)
        
        scroll_x1.config(command=self.cust_details_table1.xview)
        scroll_y1.config(command=self.cust_details_table1.yview)
        
        self.cust_details_table1.column("Firstname",width=65)
        self.cust_details_table1.column("Lastname",width=65)
        self.cust_details_table1.column("Gender",width=50)
        self.cust_details_table1.column("Martial_Status",width=87)
        self.cust_details_table1.column("Security_ID",width=75)
        self.cust_details_table1.column("Nationality",width=70)
        self.cust_details_table1.column("Email",width=155)
        self.cust_details_table1.column("Phone",width=85)
        self.cust_details_table1.column("City",width=80)
        self.cust_details_table1.column("Postcode",width=80)
        self.cust_details_table1.column("Address",width=100)
        self.cust_details_table1.column("Password",width=75)
        self.cust_details_table1.column("Booking_Date",width=90)
        self.cust_details_table1.column("Move_in_Date",width=90)
        self.cust_details_table1.column("Shared_2h_House",width=110)
        self.cust_details_table1.column("Shared_3h_House",width=110)
        self.cust_details_table1.column("Family_1h_House",width=110)
        self.cust_details_table1.column("Family_2h_House",width=110)
        self.cust_details_table1.column("Budget_Min",width=75)
        self.cust_details_table1.column("Budget_Max",width=75)
        self.cust_details_table1.column("Building_A",width=70)
        self.cust_details_table1.column("Building_B",width=70)
        self.cust_details_table1.column("Building_C",width=70)
        self.cust_details_table1.column("Building_D",width=70)
        self.cust_details_table1.column("Building_E",width=70)
        self.cust_details_table1.column("Building_F",width=70)
        
        self.cust_details_table1.heading("Firstname",text="Firstname")
        self.cust_details_table1.heading("Lastname",text="Lastname")
        self.cust_details_table1.heading("Gender",text="Gender")
        self.cust_details_table1.heading("Martial_Status",text="Martial Status")
        self.cust_details_table1.heading("Security_ID",text="Security ID")
        self.cust_details_table1.heading("Nationality",text="Nationality")
        self.cust_details_table1.heading("Email",text="Email")
        self.cust_details_table1.heading("Phone",text="Phone")
        self.cust_details_table1.heading("City",text="City")
        self.cust_details_table1.heading("Postcode",text="Postcode")
        self.cust_details_table1.heading("Address",text="Address")
        self.cust_details_table1.heading("Password",text="Password")
        self.cust_details_table1.heading("Booking_Date",text="Booking Date")
        self.cust_details_table1.heading("Move_in_Date",text="Move-in Date")
        self.cust_details_table1.heading("Shared_2h_House",text="2h-shared House")
        self.cust_details_table1.heading("Shared_3h_House",text="3h-shared House")
        self.cust_details_table1.heading("Family_1h_House",text="1h-family House")
        self.cust_details_table1.heading("Family_2h_House",text="2h-family House")
        self.cust_details_table1.heading("Budget_Min",text="Budget Min")
        self.cust_details_table1.heading("Budget_Max",text="Budget Max")
        self.cust_details_table1.heading("Building_A",text="Building A")
        self.cust_details_table1.heading("Building_B",text="Building B")
        self.cust_details_table1.heading("Building_C",text="Building C")
        self.cust_details_table1.heading("Building_D",text="Building D")
        self.cust_details_table1.heading("Building_E",text="Building F")
        self.cust_details_table1.heading("Building_F",text="Building F")
        
        ttk.Style().configure("Treeview.Heading",font=("Arial",9,"bold"))
        self.cust_details_table1["show"]="headings"
        self.cust_details_table1.pack(fill=BOTH,expand=1)
        
        self.cust_details_table1.bind("<ButtonRelease-1>",self.get_cursor1)
        self.sql_fetch_data1()

    #---------------------------Approval Renting System------------------------------#    
        table_frame2=LabelFrame(self.root,bd=2,relief=RIDGE,text="Approval List",padx=2,font=("times new roman",12,"bold"))  
        table_frame2.place(x=290,y=227,width=517,height=1500)

        combo_search2_1=ttk.Combobox(table_frame2,textvariable=self.var_typehouse_entry,font=("arial",10),width=11,state="readonly")
        combo_search2_1["value"]=("Type_House","Shared_2h_House","Shared_3h_House","Family_1h_House","Family_2h_House")
        combo_search2_1.grid(row=0,column=0,padx=2)
        combo_search2_1.current(0)

        combo_search2_2=ttk.Combobox(table_frame2,textvariable=self.var_apartment_entry,font=("arial",10),width=9,state="readonly")
        combo_search2_2["value"]=("Apartment","Building A","Building B","Building C","Building D","Building E","Building F")
        combo_search2_2.grid(row=0,column=1,padx=2)
        combo_search2_2.current(0)
        
        combo_search2_3=ttk.Combobox(table_frame2,textvariable=self.var_budgetmin_entry,font=("arial",10),width=10)
        combo_search2_3["value"]=("Budget_Min")
        combo_search2_3.grid(row=0,column=2,padx=2)
        combo_search2_3.current(0)

        combo_search2_4=ttk.Combobox(table_frame2,textvariable=self.var_budgetmax_entry,font=("arial",10),width=11)
        combo_search2_4["value"]=("Budget_Max")
        combo_search2_4.grid(row=0,column=3,padx=2)
        combo_search2_4.current(0)
        
        #----------------Btns on TOP side-----------------#
        btnSearch2=Button(table_frame2,text="Search",command=self.search_button2,font=("arial",8,"bold"),bg="black",fg="gold",width=6)
        btnSearch2.grid(row=0,column=4,padx=1)
        
        btnShowAll2=Button(table_frame2,text="Show All",command=self.show_all_button2,font=("arial",8,"bold"),bg="black",fg="gold",width=7)
        btnShowAll2.grid(row=0,column=5,padx=1)
        
        #----------Create Treeview on RIGHT side-----------#
        details_table2=Frame(table_frame2,bd=1,relief=RIDGE)
        details_table2.place(x=-1,y=30,width=510,height=200)
        
        scroll_x=ttk.Scrollbar(details_table2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table2,orient=VERTICAL)
        
        self.cust_details_table2=ttk.Treeview(details_table2,column=("Firstname","Lastname","Gender","Security_ID","Email","Phone","Move_in_Date","Budget_Min","Budget_Max","Type_House","Apartment","House","Room","Apartment_Address","Fee"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.cust_details_table2.xview)
        scroll_y.config(command=self.cust_details_table2.yview)
        
        self.cust_details_table2.column("Firstname",width=65)
        self.cust_details_table2.column("Lastname",width=65)
        self.cust_details_table2.column("Gender",width=60)
        self.cust_details_table2.column("Security_ID",width=80)
        self.cust_details_table2.column("Email",width=160)
        self.cust_details_table2.column("Phone",width=80)
        self.cust_details_table2.column("Move_in_Date",width=90)
        self.cust_details_table2.column("Budget_Min",width=75)
        self.cust_details_table2.column("Budget_Max",width=75)
        self.cust_details_table2.column("Type_House",width=75)
        self.cust_details_table2.column("Apartment",width=75)
        self.cust_details_table2.column("House",width=45)
        self.cust_details_table2.column("Room",width=40)
        self.cust_details_table2.column("Apartment_Address",width=130)
        self.cust_details_table2.column("Fee",width=40)
        
        self.cust_details_table2.heading("Firstname",text="Firstname")
        self.cust_details_table2.heading("Lastname",text="Lastname")
        self.cust_details_table2.heading("Gender",text="Gender")
        self.cust_details_table2.heading("Security_ID",text="Security ID")
        self.cust_details_table2.heading("Email",text="Email")
        self.cust_details_table2.heading("Phone",text="Phone")
        self.cust_details_table2.heading("Move_in_Date",text="Move-in Date")
        self.cust_details_table2.heading("Budget_Min",text="Budget Min")
        self.cust_details_table2.heading("Budget_Max",text="Budget Max")
        self.cust_details_table2.heading("Apartment",text="Apartment")
        self.cust_details_table2.heading("Type_House",text="Type House")
        self.cust_details_table2.heading("House",text="House")
        self.cust_details_table2.heading("Room",text="Room")
        self.cust_details_table2.heading("Apartment_Address",text="Apartment_Address")
        self.cust_details_table2.heading("Fee",text="Fee")
        
        ttk.Style().configure("Treeview.Heading",font=("Arial",9,"bold"))
        self.cust_details_table2["show"]="headings"
        self.cust_details_table2.pack(fill=BOTH,expand=1)
        
        self.cust_details_table2.bind("<ButtonRelease-1>",self.get_cursor2)
        self.sql_fetch_data2()
        
    #-----Fetch data from SQL "customer" to Tkinter Treeview-----# 
    def sql_fetch_data1(self): 
        conn = sqlite3.connect("E:\Thesis\house\database\house.db")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM customer WHERE Shared_2h_House IN ('x') OR Shared_3h_House IN ('x') OR Family_1h_House IN ('x') OR Family_2h_House IN ('x') OR Building_A IN ('x') OR Building_B IN ('x') OR Building_C IN ('x') OR Building_D IN ('x') OR Building_E IN ('x') OR Building_F IN ('x')")
        #----Call/save/take data rows/tuple from SQL----#
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            #-------Delete all rows on Treeview/Create blanks Treeview-----#
            self.cust_details_table1.delete(*self.cust_details_table1.get_children()) #---*self.ACBD: return list of tuple (rows); get_children(): return list of IDs----#
            #-------Insert data rows/Fetch data/tuple to blanks Treeview------#
            for i in rows:
                self.cust_details_table1.insert("",END,value=i)
        conn.commit()
        conn.close()    
    
    #----Fill data from "customer" into entry boxes-----#  
    def get_cursor1(self,event):
        #---------Grab record numbers-----------#
        select_row=self.cust_details_table1.focus()
        #---------Grab record values------------#
        content=self.cust_details_table1.item(select_row)
        row=content["values"]
        #---------Output entry boxes--------#
        if(row):
            self.var_firstname.set(row[0])
            self.var_lastname.set(row[1])
            self.var_gender.set(row[2])
            self.var_id.set(row[5])
            self.var_email.set(row[6])
            self.var_phone.set(row[7])
            self.var_bookdate.set(row[12])
            self.var_moveindate.set(row[13])
            self.var_2hshare.set(row[14])
            self.var_3hshare.set(row[15])    
            self.var_1hfamily.set(row[16])  
            self.var_2hfamily.set(row[17])  
            self.var_budgetmin.set(row[18]) 
            self.var_budgetmax.set(row[19])
            self.var_buildingA.set(row[20]) 
            self.var_buildingB.set(row[21]) 
            self.var_buildingC.set(row[22]) 
            self.var_buildingD.set(row[23]) 
            self.var_buildingE.set(row[24]) 
            self.var_buildingF.set(row[25])
                
            self.var_budgetmin_entry.set(row[18])
            self.var_budgetmax_entry.set(row[19])
            #---Disable some entry boxes---#
            self.entry_firstname.config(state='readonly')
            self.entry_lastname.config(state='readonly')
            self.combo_gender.config(state='readonly')
            self.entry_id.config(state='readonly')
            self.entry_email.config(state='readonly')
            self.entry_phone.config(state='readonly')
            self.entry_bookdate.config(state='readonly')

    #----Fill data from "renting" into entry boxes-----#  
    def get_cursor2(self,event):
        #---------Grab record numbers-----------#
        select_row=self.cust_details_table2.focus()
        #---------Grab record values------------#
        content=self.cust_details_table2.item(select_row)
        row=content["values"]
        #---------Output entry boxes--------#
        if(row):
            if(row[9]=="Shared_2h_House"):
                self.var_2hshare.set("x")
                self.var_3hshare.set("")
                self.var_1hfamily.set("")
                self.var_2hfamily.set("")
            elif(row[9]=="Shared_3h_House"):
                self.var_2hshare.set("")
                self.var_3hshare.set("x")
                self.var_1hfamily.set("")
                self.var_2hfamily.set("")
            elif(row[9]=="Family_1h_House"):
                self.var_3hshare.set("")
                self.var_2hshare.set("")
                self.var_1hfamily.set("x")
                self.var_2hfamily.set("")
            elif(row[9]=="Family_2h_House"):
                self.var_3hshare.set("")
                self.var_2hshare.set("")
                self.var_1hfamily.set("")
                self.var_2hfamily.set("x")
            if(row[10]=="Building A"):
                self.var_buildingA.set("x")
                self.var_buildingB.set("")
                self.var_buildingC.set("")
                self.var_buildingD.set("")
                self.var_buildingE.set("")   
                self.var_buildingF.set("")                               
            elif(row[10]=="Building B"):
                self.var_buildingA.set("")
                self.var_buildingB.set("x")
                self.var_buildingC.set("")
                self.var_buildingD.set("")
                self.var_buildingE.set("")   
                self.var_buildingF.set("") 
            elif(row[10]=="Building C"):
                self.var_buildingA.set("")
                self.var_buildingB.set("")
                self.var_buildingC.set("x")
                self.var_buildingD.set("")
                self.var_buildingE.set("")   
                self.var_buildingF.set("")    
            elif(row[10]=="Building D"):
                self.var_buildingA.set("")
                self.var_buildingB.set("")
                self.var_buildingC.set("")
                self.var_buildingD.set("x")
                self.var_buildingE.set("")   
                self.var_buildingF.set("")
            elif(row[10]=="Building E"):
                self.var_buildingA.set("")
                self.var_buildingB.set("")
                self.var_buildingC.set("")
                self.var_buildingD.set("")
                self.var_buildingE.set("x")   
                self.var_buildingF.set("")      
            elif(row[10]=="Building F"):
                self.var_buildingA.set("")
                self.var_buildingB.set("")
                self.var_buildingC.set("")
                self.var_buildingD.set("")
                self.var_buildingE.set("")   
                self.var_buildingF.set("x")  
            self.var_house.set(row[11])
            self.var_room.set(row[12])                                                   
        #---Disable some entry boxes---#
        self.entry_firstname.config(state='readonly')
        self.entry_lastname.config(state='readonly')
        self.combo_gender.config(state='disabled')
        self.entry_id.config(state='readonly')
        self.entry_email.config(state='readonly')
        self.entry_phone.config(state='readonly')
        self.entry_bookdate.config(state='readonly')
        
    #-----Fetch data from SQL "order" to Tkinter Treeview-----# 
    def sql_fetch_data2(self): 
        conn = sqlite3.connect("E:\Thesis\house\database\house.db")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM renting")
        #----Call/save/take data rows/tuple from SQL----#
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            #-------Delete all rows on Treeview/Create blanks Treeview-----#
            self.cust_details_table2.delete(*self.cust_details_table2.get_children()) #---*self.ACBD: return list of tuple (rows); get_children(): return list of IDs----#
            #-------Insert data rows/Fetch data/tuple to blanks Treeview------#
            for i in rows:
                self.cust_details_table2.insert("",END,value=i)
        conn.commit()
        conn.close()    

    #----Modify data from entry boxes, update to SQL----#
    def sql_update_data(self):
        if(self.var_room.get()==1 and self.var_id.get()!=""):
            try:
                conn1=sqlite3.connect("E:\Thesis\house\database\house.db")
                my_cursor1=conn1.cursor()
                my_cursor1.execute("UPDATE renting SET Firstname=?,Lastname=?,Gender=?,Security_ID=?,Email=?,Phone=?,Move_in_Date=?,Budget_Min=?,Budget_Max=? WHERE (Type_House=? AND Apartment=? AND House=? AND Room=?)",
                    (self.var_firstname.get(),
                    self.var_lastname.get(),
                    self.var_gender.get(),
                    self.var_id.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_moveindate.get(),
                    self.var_budgetmin.get(), 
                    self.var_budgetmax.get(),
                    self.var_typehouse_entry.get(),
                    self.var_apartment_entry.get(),
                    self.var_house.get(),
                    self.var_room.get()      
                    )
                )
                conn1.commit()
                conn1.close()
                
                conn2=sqlite3.connect("E:\Thesis\house\database\house.db")
                my_cursor2=conn2.cursor()                
                my_cursor2.execute("UPDATE renting SET Gender=? WHERE (Type_House=? AND Apartment=? AND House=? AND (Room BETWEEN 1 AND 3))",
                    (
                    self.var_gender.get(),
                    self.var_typehouse_entry.get(),
                    self.var_apartment_entry.get(),
                    self.var_house.get()             
                    )
                )
                conn2.commit()
                conn2.close()
                
                conn3=sqlite3.connect("E:\Thesis\house\database\house.db")
                my_cursor3=conn3.cursor()                
                my_cursor3.execute("UPDATE customer SET Shared_2h_House=NULL,Shared_3h_House=NULL,Family_1h_House=NULL,Family_2h_House=NULL,Budget_Min=NULL,Budget_Max=NULL,Building_A=NULL,Building_B=NULL,Building_C=NULL,Building_D=NULL,Building_E=NULL,Building_F=NULL WHERE Security_ID=?",(self.var_id.get(),))
                conn3.commit()                                               
                self.sql_fetch_data1()
                self.sql_fetch_data2()     
                self.clear()   
                conn3.close()
                messagebox.showinfo("Update","Customer details have been updated",parent=self.root)                       
            except Exception as es:
                messagebox.showerror("Warning",f"Something went wrong:{str(es)}",parent=self.root)        
        elif((self.var_room.get()>=2 and self.var_room.get()<=3) and self.var_id.get()!=""):
            try:
                conn1=sqlite3.connect("E:\Thesis\house\database\house.db")
                my_cursor1=conn1.cursor()
                my_cursor1.execute("UPDATE renting SET Firstname=?,Lastname=?,Gender=?,Security_ID=?,Email=?,Phone=?,Move_in_Date=?,Budget_Min=?,Budget_Max=? WHERE (Type_House=? AND Apartment=? AND House=? AND Room=?)",
                    (self.var_firstname.get(),
                    self.var_lastname.get(),
                    self.var_gender.get(),
                    self.var_id.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_moveindate.get(),
                    self.var_budgetmin.get(), 
                    self.var_budgetmax.get(),
                    self.var_typehouse_entry.get(),
                    self.var_apartment_entry.get(),
                    self.var_house.get(),
                    self.var_room.get()      
                    )
                )
                conn1.commit()
                conn1.close()
                                
                conn3=sqlite3.connect("E:\Thesis\house\database\house.db")
                my_cursor3=conn3.cursor()                
                my_cursor3.execute("UPDATE customer SET Shared_2h_House=NULL,Shared_3h_House=NULL,Family_1h_House=NULL,Family_2h_House=NULL,Budget_Min=NULL,Budget_Max=NULL,Building_A=NULL,Building_B=NULL,Building_C=NULL,Building_D=NULL,Building_E=NULL,Building_F=NULL WHERE Security_ID=?",
                                   (
                                     self.var_id.get(),
                                   )
                                  )
                conn3.commit()                                               
                self.sql_fetch_data1()
                self.sql_fetch_data2()     
                self.clear()   
                conn3.close()
                messagebox.showinfo("Update","Customer booking has been approved")                       
            except Exception as es:
                messagebox.showerror("Error",f"Something went wrong:{str(es)}",parent=self.root) 
        else:
            messagebox.showwarning("Warning","Please choose a customer to approve their booking",parent=self.root) 
                               
    #------------------------Btn Search1------------------------#
    def search_button1(self):
        if(self.var_search.get()!="" and self.var_txt.get()!=""):
            self.cust_details_table1.delete(*self.cust_details_table1.get_children())
            conn = sqlite3.connect("E:\Thesis\house\database\house.db")
            my_cursor=conn.execute("SELECT * FROM customer WHERE " + str(self.var_search.get()) + " LIKE ?", (str(self.var_txt.get()) + '%',))   
            rows=my_cursor.fetchall()
            if(len(rows)!=0):
                for data in rows:
                    self.cust_details_table1.insert("",END,values=data)  
            my_cursor.close()
            conn.close()
        else:
            messagebox.showwarning("Search","Fill both fields",parent=self.root)    

    #-------------------------------Btn "Search" 2------------------------------#                
    def search_button2(self):
        if(self.var_typehouse_entry.get()!="Type_House" and self.var_apartment_entry.get()!="Apartment" and self.var_budgetmin_entry.get()!="Budget_Min" and self.var_budgetmax_entry.get()!="Budget_Max"):
            self.cust_details_table2.delete(*self.cust_details_table2.get_children())
            conn = sqlite3.connect("E:\Thesis\house\database\house.db")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT * FROM renting WHERE (Security_ID IS NULL AND (Gender=? or Gender IS NULL) AND Type_House=? AND Apartment=? AND Fee<=?)",
                                (self.var_gender.get(),
                                 self.var_typehouse_entry.get(),
                                 self.var_apartment_entry.get(),
                                 self.var_budgetmax_entry.get()
                                )
                            )
            rows = my_cursor.fetchall()
            if len(rows)!=0:
                #-------Insert data rows/Fetch data/tuple to blanks Treeview------#
                for i in range(len(rows)):
                    self.cust_details_table2.insert("",END,value=rows[i])
            conn.close()
        else:
            messagebox.showwarning("Warning","Fill all fields",parent=self.root)
    
    #-----------------Remove/Cancel data------------------#
    def sql_remove_data(self):
        if(self.var_firstname.get()!=""):
            try:
                conn=sqlite3.connect("E:\Thesis\house\database\house.db")
                my_cursor=conn.cursor()                
                my_cursor.execute("UPDATE customer SET Shared_2h_House=NULL,Shared_3h_House=NULL,Family_1h_House=NULL,Family_2h_House=NULL,Budget_Min=NULL,Budget_Max=NULL,Building_A=NULL,Building_B=NULL,Building_C=NULL,Building_D=NULL,Building_E=NULL,Building_F=NULL WHERE Security_ID=?",
                                  (
                                    self.var_id.get(),
                                  )
                                 )
                conn.commit()                                               
                self.sql_fetch_data1()   
                self.clear()   
                conn.close()
                messagebox.showinfo("Delete Successfully","Customer booking was already cancelled",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Something went wrong:{str(es)}",parent=self.root)                    
        else:   
            messagebox.showwarning("Warning","Please choose a customer to cancel their booking",parent=self.root)         
                                    
    #----------------Btn Show_All_1---------------#
    def show_all_button1(self):
        self.sql_fetch_data1() 
                    
    #----------Btn "Show All" for table "Booking Management"------------#                
    def show_all_button2(self):
        self.sql_fetch_data2()                     
    
    #---------------------------Btn Approve-------------------------#         
    def approve_button(self):
        self.sql_update_data()
    
    #-----------------Btn Cancel------------------#
    def cancel_button(self):
        self.sql_remove_data()
        
    #---Clear data from entry boxes---#
    def clear(self):
        self.var_firstname.set("")
        self.var_lastname.set("")
        self.var_gender.set("")
        self.var_martial.set("")
        self.var_nationality.set("")
        self.var_id.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_bookdate.set("")
        self.var_moveindate.set("")
        self.var_2hshare.set("")
        self.var_3hshare.set("")    
        self.var_1hfamily.set("")  
        self.var_2hfamily.set("")  
        self.var_budgetmin.set("") 
        self.var_budgetmax.set("")
        self.var_buildingA.set("") 
        self.var_buildingB.set("") 
        self.var_buildingC.set("") 
        self.var_buildingD.set("") 
        self.var_buildingE.set("") 
        self.var_buildingF.set("")
        self.var_house.set("0")
        self.var_room.set("0")
        self.var_search.set("")
        self.var_txt.set("")
        
        self.var_budgetmin_entry.set("Budget_Min") 
        self.var_budgetmax_entry.set("Budget_Max")
        self.var_typehouse_entry.set("Type_House")
        self.var_apartment_entry.set("Apartment")
               
if __name__ == "__main__":
    root=Tk()
    obj=Room_Booking(root)
    root.mainloop()        