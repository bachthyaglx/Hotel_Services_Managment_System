from tkinter import *
from tkinter import ttk

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,bd=10,text="Human Management System", font=("times new roman",40,"bold"),bg="blue",fg="black")
        # Set title on middle top window
        title.pack(side=TOP,fill=X)

        #-------Manage Frame-----------#
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=560)

        m_title=title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20) #Columnspan ??

        lbl_roll=title=Label(Manage_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w") #sticky ??

        txt_roll=title=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w") #sticky ??

        lbl_name=title=Label(Manage_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w") #sticky ??

        txt_name=title=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w") #sticky ??

        lbl_email=title=Label(Manage_Frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w") #sticky ??

        txt_email=title=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w") #sticky ??

        lbl_email=title=Label(Manage_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=4,column=0,pady=10,padx=20,sticky="w") #sticky ??

        combo_gender=ttk.Combobox(Manage_Frame,font=("times new roman",15))
        combo_gender['values']=("Select","Male","Female","Other")
        combo_gender.place(width=80,height=30,x=165,y=262)
        combo_gender.current(0)

        lbl_contact=title=Label(Manage_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w") #sticky ??

        txt_dob=title=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=5,column=1,pady=10,padx=20,sticky="w") #sticky ??

        lbl_address=title=Label(Manage_Frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_address.grid(row=6,column=0,pady=10,padx=20,sticky="w") #sticky ??

        txt_address=title=Text(Manage_Frame,font=("times new roman",10,"bold"),width=30,height=4,relief=GROOVE)
        txt_address.grid(row=6,column=1,pady=10,padx=20,sticky="w") #sticky ??
        
        #------Button Frame------
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=10,y=450,width=430)
        
        Addbtn=Button(btn_Frame,text="Add",width=10).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn=Button(btn_Frame,text="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn=Button(btn_Frame,text="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)

        #------Detail Frame------
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=800,height=560)

        lbl_search=Label(Detail_Frame,text="Search by",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w") #sticky ??

        combo_search=ttk.Combobox(Detail_Frame,width=10,font=("times new roman",15,"bold"),state="readonly")
        combo_search['values']=("Roll","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)
        
        txt_search=title=Entry(Detail_Frame,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w") #sticky ??

        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10) 
        
        #-----------Table Frame---------
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=480)
        
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL) #orient ??
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL) #orient ??
        Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X) #??
        scroll_y.pack(side=RIGHT,fill=Y) #??
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading("roll",text="Roll No.")
        Student_table.heading("name",text="Name")
        Student_table.heading("email",text="Email")
        Student_table.heading("gender",text="Gender")
        Student_table.heading("contact",text="Contact")
        Student_table.heading("dob",text="D.O.B")
        Student_table.heading("address",text="Address")
        Student_table['show']='headings'
        Student_table.column("roll",width=100)
        Student_table.column("name",width=100)
        Student_table.column("email",width=100)
        Student_table.column("gender",width=100)
        Student_table.column("contact",width=100)
        Student_table.column("dob",width=100)
        Student_table.column("address",width=150)
        Student_table.pack(fill=BOTH,expand=1)
        

root=Tk()
obj=Student(root)
root.mainloop()
