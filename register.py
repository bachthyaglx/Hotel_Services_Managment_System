# Import the required libraries
from cgitb import text
from tkinter import *
from tkinter import ttk, messagebox
from tokenize import String
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import ImageTk,Image
import sqlite3
import re

class User_Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
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
        self.root.config(bg="black")
        
        # Left image
        self.left=Image.open("E:\Thesis\house\hotel_images\login_background.jpg")
        self.left=self.left.resize((450,250),Image.ANTIALIAS)
        self.left_resized=ImageTk.PhotoImage(self.left)
        left_resized=Label(self.root,image=self.left_resized,bg="black").place(x=0,y=180)
        
        # Create a frame for input info
        frame1=Label(self.root,bg="black")
        frame1.place(x=290,y=20,width=700,height=610)
        
        # Create entry for frame
        title=Label(frame1,text="REGISTER",font=("time new roman",15,"bold"),fg="yellow",bg="black").place(x=50,y=0)
        
        # Row 1
        self.var_firstname=StringVar()
        f_name=Label(frame1,text="First Name",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=50,y=50)
        txt_fname=Entry(frame1,font=("times new roman",15),textvariable=self.var_firstname).place(x=50,y=80,width=250)
        
        self.var_lastname=StringVar()
        l_name=Label(frame1,text="Last Name",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=370,y=50)
        txt_lname=Entry(frame1,font=("times new roman",15),textvariable=self.var_lastname).place(x=370,y=80,width=250)
 
        # Row 2
        self.var_gender=StringVar()
        email=Label(frame1,text="Gender",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=50,y=110)
        txt_gender=ttk.Combobox(frame1,font=("times new roman",12),textvariable=self.var_gender,state='readonly',justify=CENTER)
        txt_gender["value"]=("Male","Female","Other")
        txt_gender.place(x=50,y=140,width=250)
        
        self.var_maritial=StringVar()
        maritial=Label(frame1,text="Maritial Status",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=370,y=110)
        txt_maritial=ttk.Combobox(frame1,font=("times new roman",12),textvariable=self.var_maritial,state='readonly',justify=CENTER)
        txt_maritial["value"]=("Single","Cohabitation","Maried","Widow","Divorced","Living apart","Engaged")
        txt_maritial.place(x=370,y=140,width=250)
        
        # Row 3
        self.var_nationality=StringVar()
        question=Label(frame1,text="Nationality",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=50,y=170)
        combo_nationality=AutocompleteCombobox(frame1,font=("times new roman",12),textvariable=self.var_nationality,justify=CENTER)
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
        combo_nationality.place(x=50,y=200,width=250)

        self.var_id=StringVar()
        id=Label(frame1,text="Security ID",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=370,y=170)
        txt_id=Entry(frame1,font=("times new roman",15),textvariable=self.var_id).place(x=370,y=200,width=250)

        # Row 4
        self.var_email=StringVar()
        self.email=Label(frame1,text="Email",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=50,y=230)
        self.txt_email=Entry(frame1,font=("times new roman",12),textvariable=self.var_email).place(x=50,y=260,width=250)
        
        self.var_phone=StringVar()
        phone=Label(frame1,text="Phone",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=370,y=230)
        txt_phone=Entry(frame1,font=("times new roman",12),textvariable=self.var_phone).place(x=370,y=260,width=250)

        # Row 5
        self.var_city=StringVar()
        password=Label(frame1,text="City",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=50,y=290)
        txt_city=Entry(frame1,font=("times new roman",12),textvariable=self.var_city).place(x=50,y=320,width=250)
        
        self.var_postcode=StringVar()
        cpassword=Label(frame1,text="Postcode",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=370,y=290)
        txt_postcode=Entry(frame1,font=("times new roman",12),textvariable=self.var_postcode).place(x=370,y=320,width=250)        
        
        # Row 6
        self.var_address=StringVar()
        password=Label(frame1,text="Address",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=50,y=350)
        txt_password=Entry(frame1,font=("times new roman",12),textvariable=self.var_address).place(x=50,y=380,width=250)

        # Row 7
        self.var_password=StringVar()
        password=Label(frame1,text="Password",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=50,y=410)
        txt_password=Entry(frame1,show="*",font=("times new roman",12),textvariable=self.var_password).place(x=50,y=440,width=250)
        
        self.var_confirm=StringVar()
        confirm=Label(frame1,text="Confirm password",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=370,y=410)
        txt_confirm=Entry(frame1,show="*",font=("times new roman",12),textvariable=self.var_confirm).place(x=370,y=440,width=250)      
        
        # Terms & conditions
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Hereby Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="black",font=("times time roman",10,"italic","bold"),fg="red").place(x=45,y=480)
        
        # Button register
        btn_register=Button(frame1,text="Register now",command=self.register,font=("times new roman",18,"bold"),cursor="hand2",bg="yellow")
        btn_register.place(x=50,y=520)
        
        # Button login
        btn_login=Button(self.root,text="Login",command=self.sign_in,font=("times new roman",15,"bold"),cursor="hand2",bg="lightblue")
        btn_login.place(x=155,y=295,width=110)
    
    # Clear all entry 
    def clear(self):
        self.var_firstname.set("")
        self.var_lastname.set("")
        self.var_gender.set("")
        self.var_maritial.set("")
        self.var_nationality.set("")
        self.var_id.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_city.set("")
        self.var_postcode.set("")
        self.var_address.set("")
        self.var_password.set("")
        self.var_confirm.set("")
        self.var_chk.set("")

    # Switch to login mainpage
    def sign_in(self):
        self.root.destroy()
    
    # Register new customer
    def register(self):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        valid_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@a-z]+[.]\w{2,3}$'
        mess=""
        if(self.var_firstname.get()=="" or 
           self.var_lastname.get()=="" or 
           self.var_gender.get()=="" or 
           self.var_maritial.get()=="" or 
           self.var_nationality.get()=="" or 
           self.var_id.get()=="" or 
           self.var_email.get()=="" or 
           self.var_phone.get()=="" or 
           self.var_city.get()=="" or 
           self.var_postcode.get()=="" or 
           self.var_address.get()=="" or 
           self.var_password.get()=="" or 
           self.var_confirm.get()==""):
            messagebox.showwarning("Warning","Please enter all field",parent=self.root)
        else:        
            if(self.var_firstname.get()!="" and (regex.search(self.var_firstname.get()) or self.var_firstname.get().isdigit()==True)): 
                text="Firstname only accepts alphabets [a-z]\n\n"
                mess=mess+text
            if(self.var_lastname.get()!="" and (regex.search(self.var_lastname.get()) or self.var_lastname.get().isdigit()==True)):
                text="Lastname only accepts alphabets [a-z]\n\n"
                mess=mess+text 
            if(self.var_id.get()!=""):
                con=sqlite3.connect("E:\Thesis\house\database\house.db")
                cur=con.cursor()
                cur.execute("SELECT * FROM customer WHERE Security_ID=?",(self.var_id.get(),))
                result=cur.fetchone()
                if(result!=None):
                    text="ID is existed. Please enter another one\n\n"
                    mess=mess+text                 
            if(self.var_email.get()!=""):
                if(not re.search(valid_email,self.var_email.get())):
                    text="Email is un-valid, must be, ex: abcd@gmail.com, abcd.efs@centria.fi\n\n"   
                    mess=mess+text
                else:
                    con=sqlite3.connect("E:\Thesis\house\database\house.db")
                    cur=con.cursor()
                    cur.execute("SELECT * FROM customer WHERE Email=?",(self.var_email.get(),))
                    result=cur.fetchone()
                    if(result!=None):
                        text="Email is existed. Please enter another one or login\n\n"
                        mess=mess+text   
            if(self.var_phone.get()!="" and ((not self.var_phone.get().isdigit()) or (len(self.var_phone.get())<9 or len(self.var_phone.get())>15) or self.var_phone.get()[0]!='+')):
                text="Phone number only accept numbers [0-9] and length is 10, ex: +258 0xxxxxx\n\n"   
                mess=mess+text
            if(self.var_postcode.get()!="" and (not self.var_postcode.get().isdigit())):
                text="Postcode only contains numbers [0-9]\n\n"
                mess=mess+text
            if(self.var_password.get()!="" and (len(self.var_password.get())<8 or (re.search('[0-9]',self.var_password.get()) is None) or (re.search('[a-z]',self.var_password.get()) is None) or self.var_password.get()!=self.var_confirm.get())):
                text="Password must be at least 8 characters [a-z] and [0-9]\nPassword and confirm password must be same\n\n"   
                mess=mess+text
            if(self.var_chk.get()==0):
                text="Please agree the Terms & Conditions"   
                mess=mess+text
            if(mess!=""):
                messagebox.showwarning("Warning",str(mess),parent=self.root)        
            else:
                try:
                    con=sqlite3.connect("E:\Thesis\house\database\house.db")
                    cur=con.cursor()  
                    cur.execute("INSERT INTO customer(Firstname,Lastname,Gender,Martial_Status,Nationality,Security_ID,Email,Phone,City,Postcode,Address,Password) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (self.var_firstname.get(),
                        self.var_lastname.get(),
                        self.var_gender.get(),
                        self.var_maritial.get(),
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
                    con.commit()
                    self.clear()
                    con.close()
                    messagebox.showinfo("Successfully","Account has been registered",parent=self.root)
                    self.root.destroy()                    
                except Exception as es:
                    messagebox.showerror("Error",f"Something went wrong:{str(es)}",parent=self.root)
                                
if __name__ == "__main__":                 
    root=Tk()
    obj=User_Register(root) 
    root.mainloop()