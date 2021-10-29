from tkinter import *
from tkinter import ttk
from tkinter import font
import pymysql
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="black")

        title=Label(self.root,bd=10,text="Human Management System", font=("times new roman",40,"bold"),bg="white",fg="black")
        # Set title on middle top window
        title.pack(side=TOP,fill=X)

        #-------All Variables----------
        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        #-------Manage Frame-----------#
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#002d58")
        Manage_Frame.place(x=20,y=100,width=475,height=560)

        m_title=title=Label(Manage_Frame,text="Human Management",bg="#002d58",fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=3,pady=10) #Columnspan ??
        m_title.config(width=20)

        lbl_roll=title=Label(Manage_Frame,text="Roll No.",bg="#002d58",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w") #sticky ??

        txt_roll=title=Entry(Manage_Frame,textvariable=self.roll_no_var,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w") #sticky ??
        txt_roll.config(width=27)
        
        lbl_name=title=Label(Manage_Frame,text="Name",bg="#002d58",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w") #sticky ??

        txt_name=title=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w") #sticky ??
        txt_name.config(width=27)

        lbl_email=title=Label(Manage_Frame,text="Email",bg="#002d58",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w") #sticky ??

        txt_email=title=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w") #sticky ??
        txt_email.config(width=27)

        lbl_email=title=Label(Manage_Frame,text="Gender",bg="#002d58",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=4,column=0,pady=10,padx=20,sticky="w") #sticky ??

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",15))
        combo_gender['values']=("Select","Male","Female","Other")
        combo_gender.place(width=100,height=30,x=165,y=241)
        combo_gender.current(0)

        lbl_contact=title=Label(Manage_Frame,text="Contact",bg="#002d58",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w") #sticky ??

        txt_contact=title=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w") #sticky ??
        txt_contact.config(width=27)

        lbl_dob=title=Label(Manage_Frame,text="D.O.B",bg="#002d58",fg="white",font=("times new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w") #sticky ??

        txt_dob=title=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w") #sticky ??
        txt_dob.config(width=27)

        lbl_address=title=Label(Manage_Frame,text="Address",bg="#002d58",fg="white",font=("times new roman",20,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w") #sticky ??

        self.txt_address=title=Text(Manage_Frame,font=("times new roman",15),width=21,height=2.5,relief=GROOVE)
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w") #sticky ??
        self.txt_address.config(width=28)

        #------Button Frame------
        btn_Frame=Frame(Manage_Frame,bd=3,relief=RIDGE,bg="white")
        btn_Frame.place(x=10,y=505,width=445,height=40)
        
        Addbtn=Button(btn_Frame,text="Add",width=12,command=self.add,bg="#002d58",fg="white").grid(row=0,column=0,padx=8,pady=5)
        Updatebtn=Button(btn_Frame,text="Update",width=12,command=self.update,bg="#002d58",fg="white").grid(row=0,column=1,padx=8,pady=5)
        Deletebtn=Button(btn_Frame,text="Delete",width=12,command=self.delete_data,bg="#002d58",fg="white").grid(row=0,column=2,padx=8,pady=5)
        Clearbtn=Button(btn_Frame,text="Clear",width=12,command=self.clear,bg="#002d58",fg="white").grid(row=0,column=3,padx=8,pady=5)

        #------Detail Frame------
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#002d58")
        Detail_Frame.place(x=500,y=100,width=800,height=560)

        lbl_search=Label(Detail_Frame,text="Search by",bg="#002d58",fg="white",font=("times new roman",18,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w") #sticky ??

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",15,"bold"),state="readonly")
        combo_search['values']=("No","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)
        
        txt_search=title=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w") #sticky ??

        searchbtn=Button(Detail_Frame,command=self.search_data,text="Search",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,command=self.fetch_data,text="Show All",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10) 
        
        #-----------Table Frame---------
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#002d58")
        Table_Frame.place(x=10,y=55,width=760,height=490)
        
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL) #orient ??
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL) #orient ??
        #----???
        self.student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X) #??
        scroll_y.pack(side=RIGHT,fill=Y) #??
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll",text="No.")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("address",text="Address")
        self.student_table['show']='headings'
        self.student_table.column("roll",width=20)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=150)
        self.student_table.column("gender",width=50)
        self.student_table.column("contact",width=50)
        self.student_table.column("dob",width=50)
        self.student_table.column("address",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        #---- ??? -----
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    #-----Fuction adding data to database----
    def add(self):
        if self.roll_no_var.get()=="" or self.name_var=="" or self.email_var.get()=="" or self.contact_var=="" or self.gender_var.get()=="" or self.dob_var.get()=="" or self.txt_address=="":
            messagebox.showerror("Error","All fields are required")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="students")
            cur=con.cursor()
            cur.execute("insert into students (No,Name,Email,Gender,Contact,DOB,Address) values(%s,%s,%s,%s,%s,%s,%s)",
                        (self.roll_no_var.get(),
                         self.name_var.get(),
                         self.email_var.get(),
                         self.gender_var.get(),
                         self.contact_var.get(),
                         self.dob_var.get(),
                         self.txt_address.get('1.0',END) # ???
                        ))
            con.commit()
            self.fetch_data()
            con.close()
            self.clear()
            messagebox.showinfo("Success","Record has been inserted")

    #----Function fetching table from database on tkinter----
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="students")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            #----- ??? -----
            self.student_table.delete(*self.student_table.get_children())
            for i in rows:
                #---- ???
                self.student_table.insert('',END,values=i)
                con.commit()
        con.close()

    #-----Function clearing input on boxes----
    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete('1.0',END)

    #-----Cursor on row table and move data from table to blank boxes---
    def get_cursor(self,self_):
        #---???
        cursor_row=self.student_table.focus()
        #---???
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        #---?
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[6])

    #----Function updating row---
    def update(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="students")
        cur=con.cursor()
        cur.execute("update students set Name=%s,Email=%s,Gender=%s,Contact=%s,DOB=%s,Address=%s where No=%s",
                    (self.name_var.get(),
                     self.email_var.get(),
                     self.gender_var.get(),
                     self.contact_var.get(),
                     self.dob_var.get(),
                     self.txt_address.get('1.0',END), # ???
                     self.roll_no_var.get()
                    ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    #----Function deleting row----
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="students")
        cur=con.cursor()
        cur.execute("delete from students where No=%s",self.roll_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    #----Function searching data from database on tkinter----
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="students")
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" Like '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            #----- ??? -----
            self.student_table.delete(*self.student_table.get_children())
            for i in rows:
                #---- ???
                self.student_table.insert('',END,values=i)
                con.commit()
        con.close()    

root=Tk()
obj=Student(root)
root.mainloop()
