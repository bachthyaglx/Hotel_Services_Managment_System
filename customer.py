from tkinter import *
from PIL import Image, ImageTk 
from tkinter import ttk
from tkinter import messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox
import sqlite3
from sqlite3 import Error
import os

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer")
        
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
        
        text=Label(main_frame,text="Add Customer Details",font=("times new roman",15,"bold"),bg="black",fg="gold")
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
        self.var_city=StringVar()
        self.var_postcode=StringVar()
        self.var_address=StringVar()
        self.var_password=StringVar()
        self.var_search=StringVar()
        self.var_txt=StringVar()
        
        #------------Label and entrys on LEFT side---------------#
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",13,"bold"))
        labelframeleft.place(x=3,y=30,width=287,height=447)
        
        lbl_firstname=Label(labelframeleft,text="Firstname",font=("times new roman",12),padx=2,pady=5)
        lbl_firstname.grid(row=0,column=0,sticky=W)
        entry_firstname=ttk.Entry(labelframeleft,textvariable=self.var_firstname,width=22,font=("times new roman",12))
        entry_firstname.grid(row=0,column=1)

        lbl_lastname=Label(labelframeleft,text="Lastname",font=("times new roman",12),padx=2,pady=5)
        lbl_lastname.grid(row=1,column=0,sticky=W)
        entry_lastname=ttk.Entry(labelframeleft,textvariable=self.var_lastname,width=22,font=("times new roman",12))
        entry_lastname.grid(row=1,column=1)
         
        lbl_gender=Label(labelframeleft,text="Gender",font=("times new roman",12),padx=2,pady=5)
        lbl_gender.grid(row=2,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("times new roman",12),width=20,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.grid(row=2,column=1)

        lbl_martial=Label(labelframeleft,text="Martial Status",font=("times new roman",12),padx=2,pady=5)
        lbl_martial.grid(row=3,column=0,sticky=W)
        combo_martial=ttk.Combobox(labelframeleft,textvariable=self.var_martial,font=("times new roman",12),width=20,state="readonly")
        combo_martial["value"]=("Single","Cohabitation","Maried","Widow","Divorced","Living apart","Engaged")
        combo_martial.grid(row=3,column=1)
                
        lbl_nationality=Label(labelframeleft,text="Nationality",font=("times new roman",12),padx=2,pady=5)
        lbl_nationality.grid(row=4,column=0,sticky=W)
        combo_nationality=AutocompleteCombobox(labelframeleft,textvariable=self.var_nationality,font=("times new roman",12),width=20)
        combo_lists=[
            "Afghanistan",
            "Åland Islands",
            "Albania",
            "Algeria",
            "American Samoa",
            "Andorra",
            "Angola",
            "Anguilla",
            "Antarctica",
            "Antigua & Barbuda",
            "Argentina",
            "Armenia",
            "Aruba",
            "Australia",
            "Austria",
            "Azerbaijan",
            "Bahamas",
            "Bahrain",
            "Bangladesh",
            "Barbados",
            "Belarus",
            "Belgium",
            "Belize",
            "Benin",
            "Bermuda",
            "Bhutan",
            "Bolivia",
            "Bonaire",
            "Bosnia & Herzegovina",
            "Botswana",
            "Bouvet Island",
            "Brazil",
            "British Indian Ocean Territory",
            "United States Minor Outlying Islands",
            "Virgin Islands (British)",
            "Virgin Islands (US)",
            "Brunei Darussalam",
            "Bulgaria",
            "Burkina Faso",
            "Burundi",
            "Cambodia",
            "Cameroon",
            "Canada",
            "Cabo Verde",
            "Cayman Islands",
            "Central African",
            "Chad",
            "Chile",
            "China",
            "Christmas Island",
            "Cocos Islands",
            "Colombia",
            "Comoros",
            "Congo",
            "Cook Islands",
            "Costa Rica",
            "Croatia",
            "Cuba",
            "Curaçao",
            "Cyprus",
            "Czech",
            "Denmark",
            "Djibouti",
            "Dominica",
            "Dominican Republic",
            "Ecuador",
            "Egypt",
            "El Salvador",
            "Equatorial Guinea",
            "Eritrea",
            "Estonia",
            "Ethiopia",
            "Falkland Islands",
            "Faroe Islands",
            "Fiji",
            "Finland",
            "France",
            "French Guiana",
            "French Polynesia",
            "French Southern Territories",
            "Gabon",
            "Gambia",
            "Georgia",
            "Germany",
            "Ghana",
            "Gibraltar",
            "Greece",
            "Greenland",
            "Grenada",
            "Guadeloupe",
            "Guam",
            "Guatemala",
            "Guernsey",
            "Guinea",
            "Guinea-Bissau",
            "Guyana",
            "Haiti",
            "Heard Island & McDonald Islands",
            "Holy See",
            "Honduras",
            "Hongkong",
            "Hungary",
            "Iceland",
            "India",
            "Indonesia",
            "Côte d'Ivoire",
            "Iran",
            "Iraq",
            "Ireland",
            "Isle of Man",
            "Israel",
            "Italy",
            "Jamaica",
            "Japan",
            "Jersey",
            "Jordan",
            "Kazakhstan",
            "Kenya",
            "Kiribati",
            "Kuwait",
            "Kyrgyzstan",
            "Lao",
            "Latvia",
            "Lebanon",
            "Lesotho",
            "Liberia",
            "Libya",
            "Liechtenstein",
            "Lithuania",
            "Luxembourg",
            "Macao",
            "Macedonia",
            "Madagascar",
            "Malawi",
            "Malaysia",
            "Maldives",
            "Mali",
            "Malta",
            "Marshall Islands",
            "Martinique",
            "Mauritania",
            "Mauritius",
            "Mayotte",
            "Mexico",
            "Micronesia",
            "Moldova",
            "Monaco",
            "Mongolia",
            "Montenegro",
            "Montserrat",
            "Morocco",
            "Mozambique",
            "Myanmar",
            "Namibia",
            "Nauru",
            "Nepal",
            "Netherlands",
            "New Caledonia",
            "New Zealand",
            "Nicaragua",
            "Niger",
            "Nigeria",
            "Niue",
            "Norfolk Island",
            "North Korea",
            "Northern Mariana Islands",
            "Norway",
            "Oman",
            "Pakistan",
            "Palau",
            "Palestine",
            "Panama",
            "Papua New Guinea",
            "Paraguay",
            "Peru",
            "Philippines",
            "Pitcairn",
            "Poland",
            "Portugal",
            "Puerto Rico",
            "Qatar",
            "Republic of Kosovo",
            "Réunion",
            "Romania",
            "Russian Federation",
            "Rwanda",
            "Saint Barthélemy",
            "Saint Helena",
            "Saint Kitts & Nevis",
            "Saint Lucia",
            "Saint Martin",
            "Saint Pierre & Miquelon",
            "Saint Vincent & Grenadines",
            "Samoa",
            "San Marino",
            "Sao Tome & Principe",
            "Saudi Arabia",
            "Senegal",
            "Serbia",
            "Seychelles",
            "Sierra Leone",
            "Singapore",
            "Sint Maarten",
            "Slovakia",
            "Slovenia",
            "Solomon Islands",
            "Somalia",
            "South Africa",
            "South Georgia & South Sandwich Islands",
            "South Korea",
            "South Sudan",
            "Spain",
            "Sri Lanka",
            "Sudan",
            "Suriname",
            "Svalbard & Jan Mayen",
            "Swaziland",
            "Sweden",
            "Switzerland",
            "Syrian Arab",
            "Taiwan",
            "Tajikistan",
            "Tanzania",
            "Thailand",
            "Timor-Leste",
            "Togo",
            "Tokelau",
            "Tonga",
            "Trinidad & Tobago",
            "Tunisia",
            "Turkey",
            "Turkmenistan",
            "Turks & Caicos Islands",
            "Tuvalu",
            "Uganda",
            "Ukraine",
            "United Arab Emirates",
            "United Kingdom",
            "United States",
            "Uruguay",
            "Uzbekistan",
            "Vanuatu",
            "Venezuela",
            "Vietnam",
            "Wallis & Futuna",
            "Western Sahara",
            "Yemen",
            "Zambia",
            "Zimbabwe"
        ]
        combo_nationality.set_completion_list(combo_lists)
        combo_nationality.grid(row=4,column=1)
        
        lbl_id=Label(labelframeleft,text="Security ID",font=("times new roman",12),padx=2,pady=5)
        lbl_id.grid(row=5,column=0,sticky=W)
        self.entry_id=ttk.Entry(labelframeleft,textvariable=self.var_id,width=22,font=("times new roman",12))
        self.entry_id.grid(row=5,column=1) 
        
        lbl_email=Label(labelframeleft,text="Email",font=("times new roman",12),padx=2,pady=5)
        lbl_email.grid(row=6,column=0,sticky=W)
        self.entry_email=ttk.Entry(labelframeleft,textvariable=self.var_email,width=22,font=("times new roman",12))
        self.entry_email.grid(row=6,column=1)         
        
        lbl_phone=Label(labelframeleft,text="Phone",font=("times new roman",12),padx=2,pady=5)
        lbl_phone.grid(row=7,column=0,sticky=W)
        entry_phone=ttk.Entry(labelframeleft,textvariable=self.var_phone,width=22,font=("times new roman",12))
        entry_phone.grid(row=7,column=1)  
        
        lbl_city=Label(labelframeleft,text="City",font=("times new roman",12),padx=2,pady=5)
        lbl_city.grid(row=8,column=0,sticky=W)
        entry_city=ttk.Entry(labelframeleft,textvariable=self.var_city,width=22,font=("times new roman",12))
        entry_city.grid(row=8,column=1)      

        lbl_postcode=Label(labelframeleft,text="Postcode",font=("times new roman",12),padx=2,pady=5)
        lbl_postcode.grid(row=9,column=0,sticky=W)
        entry_postcode=ttk.Entry(labelframeleft,textvariable=self.var_postcode,width=22,font=("times new roman",12))
        entry_postcode.grid(row=9,column=1) 
                
        lbl_address=Label(labelframeleft,text="Address",font=("times new roman",12),padx=2,pady=5)
        lbl_address.grid(row=10,column=0,sticky=W)
        entry_address=ttk.Entry(labelframeleft,textvariable=self.var_address,width=22,font=("times new roman",12))
        entry_address.grid(row=10,column=1)
                 
        lbl_address=Label(labelframeleft,text="Password",font=("times new roman",12),padx=2,pady=5)
        lbl_address.grid(row=11,column=0,sticky=W)
        entry_address=ttk.Entry(labelframeleft,textvariable=self.var_password,width=22,font=("times new roman",12))
        entry_address.grid(row=11,column=1)
                
        #--------------------btns on BOTTOM side------------------------#
        btn_frame=Frame(labelframeleft,bd=0, relief=RIDGE)
        btn_frame.place(x=0,y=396,width=275,height=28)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_button,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=4)
        
        btnAdd=Button(btn_frame,text="Update",command=self.update_button,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=1,padx=1)

        btnAdd=Button(btn_frame,text="Delete",command=self.delete_button,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=2,padx=1)                
        
        btnAdd=Button(btn_frame,text="Reset",command=self.reset_button,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=3,padx=1)
        
        #----------------Search Boxes on TOP side-------------------#      
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",13,"bold"))  
        table_frame.place(x=290,y=30,width=517,height=447)

        lblSearchBy=Label(table_frame,font=("arial",10,"bold"),text="Search By",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        combo_search=ttk.Combobox(table_frame,textvariable=self.var_search,font=("arial",10),width=11,state="readonly")
        combo_search["value"]=("Firstname","Lastname","Gender","Martial_Status","Nationality","Security_ID","Email","Phone","City","Postcode","Address","Password")
        combo_search.grid(row=0,column=1,padx=2)
        
        txtSearch=ttk.Entry(table_frame,textvariable=self.var_txt,font=("arial",10),width=26)
        txtSearch.grid(row=0,column=2,padx=2)
        
        #----------------Btns on TOP side-----------------#
        btnSearch=Button(table_frame,text="Search",command=self.search_button,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShowAll=Button(table_frame,text="Show All",command=self.show_all_button,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnShowAll.grid(row=0,column=4,padx=1)
        
        #----------Create Treeview on RIGHT side-----------#
        details_table=Frame(table_frame,bd=1,relief=RIDGE)
        details_table.place(x=-1,y=30,width=510,height=393)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.cust_details_table=ttk.Treeview(details_table,column=("Firstname","Lastname","Gender","Martial_Status","Nationality","Security_ID","Email","Phone","City","Postcode","Address","Password"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)
        
        self.cust_details_table.column("Firstname",width=65)
        self.cust_details_table.column("Lastname",width=65)
        self.cust_details_table.column("Gender",width=60)
        self.cust_details_table.column("Martial_Status",width=90)
        self.cust_details_table.column("Nationality",width=80)
        self.cust_details_table.column("Security_ID",width=80)
        self.cust_details_table.column("Email",width=160)
        self.cust_details_table.column("Phone",width=80)
        self.cust_details_table.column("City",width=80)
        self.cust_details_table.column("Postcode",width=60)
        self.cust_details_table.column("Address",width=150)
        self.cust_details_table.column("Password",width=90)
        
        self.cust_details_table.heading("Firstname",text="Firstname")
        self.cust_details_table.heading("Lastname",text="Lastname")
        self.cust_details_table.heading("Gender",text="Gender")
        self.cust_details_table.heading("Martial_Status",text="Martial Status")
        self.cust_details_table.heading("Nationality",text="Nationality")
        self.cust_details_table.heading("Security_ID",text="Security ID")
        self.cust_details_table.heading("Email",text="Email")
        self.cust_details_table.heading("Phone",text="Phone")
        self.cust_details_table.heading("City",text="City")
        self.cust_details_table.heading("Postcode",text="Postcode")
        self.cust_details_table.heading("Address",text="Address")
        self.cust_details_table.heading("Password",text="Password")

        ttk.Style().configure("Treeview.Heading",font=("Arial",9,"bold"))
        self.cust_details_table["show"]="headings"
        
        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.sql_fetch_data()
    
    #-----Fetch data from SQL to Tkinter Treeview-----# 
    def sql_fetch_data(self): 
        conn = sqlite3.connect("E:\Thesis\house\database\house.db")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM customer")
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
            self.var_martial.set(row[3])
            self.var_nationality.set(row[4])
            self.var_id.set(row[5])
            self.var_email.set(row[6])
            self.var_phone.set(row[7])
            self.var_city.set(row[8])
            self.var_postcode.set(row[9])
            self.var_address.set(row[10])
            self.var_password.set(row[11])
        #----Disable entries email and ID------#
        self.entry_id.config(state="readonly")
        self.entry_email.config(state="readonly")     
    
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
        self.var_city.set("")
        self.var_postcode.set("")
        self.var_address.set("")
        self.var_password.set("")
        self.var_search.set("")
        self.var_txt.set("")
    
    #----Insert data from entry boxes to SQL----#    
    def sql_insert_data(self): 
        try:
            conn = sqlite3.connect("E:\Thesis\house\database\house.db")
            my_cursor=conn.cursor()
            my_cursor.execute("INSERT INTO customer(Firstname,Lastname,Gender,Martial_Status,Nationality,Security_ID,Email,Phone,City,Postcode,Address,Password) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                (self.var_firstname.get(),
                 self.var_lastname.get(),
                 self.var_gender.get(),
                 self.var_martial.get(),
                 self.var_nationality.get(),
                 self.var_id.get(),
                 self.var_email.get(),
                 self.var_phone.get(),
                 self.var_city.get(),
                 self.var_postcode.get(), 
                 self.var_address.get(),
                 self.var_password.get()                            
                )
            )
            conn.commit()
            self.sql_fetch_data()
            self.clear()
            conn.close()
            messagebox.showinfo("Successfully","Customer has been added",parent=self.root)      
        except Exception as es:
            messagebox.showerror("Error",f"Something went wrong:{str(es)}",parent=self.root)
    
    #----Modify data from entry boxes, update to SQL----#
    def sql_update_data(self):
        try:
            conn = sqlite3.connect("E:\Thesis\house\database\house.db")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE customer SET Firstname=?,Lastname=?,Gender=?,Martial_Status=?,Nationality=?,Email=?,Phone=?,City=?,Postcode=?,Address=?,Password=? WHERE Security_ID=?",
                (self.var_firstname.get(),
                self.var_lastname.get(),
                self.var_gender.get(),
                self.var_martial.get(),
                self.var_nationality.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_city.get(),
                self.var_postcode.get(), 
                self.var_address.get(),
                self.var_password.get(),
                self.var_id.get()                           
                )
            )
            conn.commit()
            self.sql_fetch_data()
            self.clear()        
            conn.close()
            messagebox.showinfo("Update","Customer details have been updated",parent=self.root)                       
        except Exception as es:
            messagebox.showerror("Error",f"Something went wrong:{str(es)}",parent=self.root) 
    
    #----Delete data from entry boxes, update to SQL---#
    def sql_delete_data(self):
        if(self.var_firstname=="" or self.var_firstname.get()=="" or self.var_lastname.get()=="" or self.var_firstname.get()=="" or self.var_gender.get()=="" or self.var_nationality.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_id.get()=="" or self.var_city.get()=="" or self.var_postcode.get()=="" or self.var_address.get()=="" or self.var_password.get()==""):
            messagebox.showwarning("House Management System","Please choose a row to delete",parent=self.root)
        else:
            mess_delete=messagebox.askyesno("House Management System","Are you sure to delete this customer?",parent=self.root)
            if(mess_delete==1):
                x=self.cust_details_table.selection()       
                #------------Create List to delete--------#
                self.ids_to_delete=[]
                #------------Add selections to Ids_delete-------#
                for record in x:
                    self.ids_to_delete.append(self.cust_details_table.item(record,"values")[5])
                #----------Delete from Treeview-------#           
                for record in x:
                    self.cust_details_table.delete(record)  
                #-----------Execute Delete SQL---------#
                conn = sqlite3.connect("E:\Thesis\house\database\house.db")
                my_cursor=conn.cursor()
                my_cursor.executemany("DELETE FROM customer WHERE Security_ID=?",[(i, ) for i in self.ids_to_delete]) #[(i, )->(1, ) (2, ) (3, ) (5, )]...#                      
                conn.commit() 
                self.sql_fetch_data()
                self.clear()
                conn.close()
            
    def add_button(self):
        if(self.var_firstname=="" or self.var_firstname.get()=="" or self.var_lastname.get()=="" or self.var_firstname.get()=="" or self.var_gender.get()=="" or self.var_nationality.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_id.get()=="" or self.var_city.get()=="" or self.var_postcode.get()=="" or self.var_address.get()=="" or self.var_password.get()==""):
            messagebox.showwarning("Warning","All fields are required",parent=self.root)
        else:
            self.sql_insert_data()
    
    def update_button(self):
        if(self.var_firstname=="" or self.var_firstname.get()=="" or self.var_lastname.get()=="" or self.var_firstname.get()=="" or self.var_gender.get()=="" or self.var_nationality.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_id.get()=="" or self.var_city.get()=="" or self.var_postcode.get()=="" or self.var_address.get()=="" or self.var_password.get()==""):
            messagebox.showwarning("Warning","Fill the empty fields",parent=self.root)
        else:
            self.sql_update_data()    
    
    def delete_button(self):
        self.sql_delete_data()
            
    def reset_button(self):
        self.clear()
        self.entry_id.config(state="normal")
        self.entry_email.config(state="normal")
    
    def search_button(self):
        if self.var_search.get()!="" and self.var_txt.get()!="":
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            conn = sqlite3.connect("E:\Thesis\house\database\house.db")
            my_cursor=conn.execute("SELECT * FROM customer WHERE " + str(self.var_search.get()) + " LIKE ?", (str(self.var_txt.get()) + '%',))   
            rows=my_cursor.fetchall()
            if(len(rows)!=0):
                for data in rows:
                    self.cust_details_table.insert("",END,values=data)  
            my_cursor.close()
            conn.close()
        else:
            messagebox.showwarning("Warning","Fill both fields",parent=self.root)    
    
    def show_all_button(self):
        self.sql_fetch_data()    
        
if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
    