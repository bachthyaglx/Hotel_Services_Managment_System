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
        self.root.configure(background='lightyellow')
        
        #-------Disable draging window-------#
        self.root.overrideredirect(True)
        
        #---Create new text and button to close window---#
        main_frame=Frame(self.root,bg="white",bd=1,relief=RIDGE)
        main_frame.place(x=0,y=0,width=810,height=30)
        
        text=Label(main_frame,text="Profile Management",font=("times new roman",15,"bold"),bg="black",fg="gold")
        text.place(x=-1,y=-2,height=30,width=781)
        
        btn=Button(main_frame,text="X",bg="red",command=self.root.destroy)
        btn.place(x=780,y=-2,height=30,width=30)
    
        #------------Label and entrys on LEFT side---------------#
        labelframeleft=LabelFrame(self.root,relief=RIDGE,text="Your Profile",padx=2,pady=2,fg="black",bg="lightblue",border=3,font=("times new roman",13,"bold"))
        labelframeleft.place(x=65,y=40,width=675,height=430)
        
        # Row 1
        self.var_firstname=StringVar()
        f_name=Label(labelframeleft,text="First Name",font=("time new roman",11,"bold"),fg="black",bg="lightblue").place(x=50,y=0)
        txt_fname=Entry(labelframeleft,font=("times new roman",11),textvariable=self.var_firstname).place(x=50,y=25,width=250)
        
        self.var_lastname=StringVar()
        l_name=Label(labelframeleft,text="Last Name",font=("time new roman",11,"bold"),fg="black",bg="lightblue").place(x=370,y=0)
        txt_lname=Entry(labelframeleft,font=("times new roman",11),textvariable=self.var_lastname).place(x=370,y=25,width=250)
 
        # Row 2
        self.var_gender=StringVar()
        email=Label(labelframeleft,text="Gender",font=("time new roman",11,"bold"),fg="black",bg="lightblue").place(x=50,y=50)
        txt_gender=ttk.Combobox(labelframeleft,font=("times new roman",11),textvariable=self.var_gender,state='readonly',justify=CENTER)
        txt_gender["value"]=("Male","Female","Other")
        txt_gender.place(x=50,y=75,width=250)
        
        self.var_maritial=StringVar()
        maritial=Label(labelframeleft,text="Maritial Status",font=("time new roman",11,"bold"),fg="black",bg="lightblue").place(x=370,y=50)
        txt_maritial=ttk.Combobox(labelframeleft,font=("times new roman",11),textvariable=self.var_maritial,state='readonly',justify=CENTER)
        txt_maritial["value"]=("Single","Cohabitation","Maried","Widow","Divorced","Living apart","Engaged")
        txt_maritial.place(x=370,y=75,width=250)
        
        # Row 3
        self.var_nationality=StringVar()
        question=Label(labelframeleft,text="Nationality",font=("time new roman",11,"bold"),fg="black",bg="lightblue").place(x=50,y=100)
        combo_nationality=AutocompleteCombobox(labelframeleft,font=("times new roman",11),textvariable=self.var_nationality,justify=CENTER)
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
        combo_nationality.place(x=50,y=125,width=250)

        self.var_id=StringVar()
        id=Label(labelframeleft,text="Security ID",font=("time new roman",11,"bold"),fg="black",bg="lightblue").place(x=370,y=100)
        self.txt_id=Entry(labelframeleft,font=("times new roman",11),textvariable=self.var_id,state="readonly").place(x=370,y=125,width=250)

        # Row 4
        self.var_email=StringVar()
        self.email=Label(labelframeleft,text="Email",font=("time new roman",11,"bold"),fg="black",bg="lightblue").place(x=50,y=150)
        self.txt_email=Entry(labelframeleft,font=("times new roman",11),textvariable=self.var_email).place(x=50,y=175,width=250)
        
        self.var_phone=StringVar()
        phone=Label(labelframeleft,text="Phone",font=("time new roman",11,"bold"),fg="black",bg="lightblue").place(x=370,y=150)
        txt_phone=Entry(labelframeleft,font=("times new roman",11),textvariable=self.var_phone).place(x=370,y=175,width=250)

        # Row 5
        self.var_city=StringVar()
        password=Label(labelframeleft,text="City",font=("time new roman",11,"bold"),fg="black",bg="lightblue").place(x=50,y=200)
        txt_city=Entry(labelframeleft,font=("times new roman",11),textvariable=self.var_city).place(x=50,y=225,width=250)
        
        self.var_postcode=StringVar()
        cpassword=Label(labelframeleft,text="Postcode",font=("time new roman",11,"bold"),fg="black",bg="lightblue").place(x=370,y=200)
        txt_postcode=Entry(labelframeleft,font=("times new roman",11),textvariable=self.var_postcode).place(x=370,y=225,width=250)        
        
        # Row 6
        self.var_address=StringVar()
        password=Label(labelframeleft,text="Address",font=("time new roman",11,"bold"),fg="black",bg="lightblue").place(x=50,y=250)
        txt_password=Entry(labelframeleft,font=("times new roman",11),textvariable=self.var_address).place(x=50,y=275,width=250)

        # Row 7
        self.var_password=StringVar()
        password=Label(labelframeleft,text="Password",font=("time new roman",11,"bold"),fg="black",bg="lightblue").place(x=50,y=300)
        txt_password=Entry(labelframeleft,show="*",font=("times new roman",11),textvariable=self.var_password).place(x=50,y=325,width=250)
        
        self.var_confirm=StringVar()
        confirm=Label(labelframeleft,text="Confirm password",font=("time new roman",11,"bold"),fg="black",bg="lightblue").place(x=370,y=300)
        txt_confirm=Entry(labelframeleft,show="*",font=("times new roman",11),textvariable=self.var_confirm).place(x=370,y=325,width=250)      
        
        # Button register
        btn_register=Button(labelframeleft,text="Modify",command=self.modify,font=("times new roman",12,"bold"),cursor="hand2",bg="yellow")
        btn_register.place(x=50,y=360)
        

    #---Clear data from entry boxes---#
    def clear(self):
        self.var_firstname.set("")
        self.var_lastname.set("")
        self.var_gender.set("")
        self.var_maritial.set("")
        self.var_nationality.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_city.set("")
        self.var_postcode.set("")
        self.var_address.set("")
        self.var_password.set("")
        self.var_confirm.set("")
        
    #----Modify data from entry boxes, update to SQL----#
    def modify(self):
        mess=""
        conn = sqlite3.connect("E:\Thesis\house\database\house.db")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM customer WHERE Security_ID=?",(self.var_id.get(),))
        result=my_cursor.fetchone()
        if(result[0]!=self.var_firstname.get()):
            text="Firstname has been modified by " + str(self.var_firstname.get()) + "\n\n"
            mess=mess+text
        if(result[1]!=self.var_lastname.get()):
            text="Lastname has been modified by " + str(self.var_lastname.get()) + "\n\n"
            mess=mess+text        
        if(result[2]!=self.var_gender.get()):
            text="Gender has been modified by " + str(self.var_gender.get()) + "\n\n"
            mess=mess+text
        if(result[3]!=self.var_maritial.get()):
            text="Maritial Status has been modified by " + str(self.var_maritial.get()) + "\n\n"
            mess=mess+text
        if(result[4]!=self.var_nationality.get()):
            text="Nationality has been modified by " + str(self.var_nationality.get()) + "\n\n"
            mess=mess+text  
        if(result[5]!=self.var_id.get()):        
            text="Security ID has been modified by " + str(self.var_id.get()) + "\n\n"
            mess=mess+text    
        if(result[6]!=self.var_email.get()):        
            text="Email has been modified by " + str(self.var_email.get()) + "\n\n"
            mess=mess+text               
        if(result[7]!=self.var_phone.get()):        
            text="Phone has been modified by " + str(self.var_phone.get()) + "\n\n"
            mess=mess+text   
        if(result[8]!=self.var_city.get()):        
            text="City has been modified by " + str(self.var_city.get()) + "\n\n"
            mess=mess+text           
        if(result[9]!=self.var_postcode.get()):        
            text="Postcode has been modified by " + str(self.var_postcode.get()) + "\n\n"
            mess=mess+text
        if(result[10]!=self.var_address.get()):        
            text="Address has been modified by " + str(self.var_address.get()) + "\n\n"
            mess=mess+text
        if(result[11]!=self.var_password.get()):        
            text="Password has been modified by " + str(self.var_password.get()) + "\n\n"
            mess=mess+text
        if(mess==""):
            messagebox.showwarning("Warning","You have not modified anything",parent=self.root)
        else:                                                                                                                                           
            try:
                my_cursor.execute("UPDATE customer SET Firstname=?,Lastname=?,Gender=?,Martial_Status=?,Nationality=?,Email=?,Phone=?,City=?,Postcode=?,Address=?,Password=? WHERE Security_ID=?",
                    (self.var_firstname.get(),
                    self.var_lastname.get(),
                    self.var_gender.get(),
                    self.var_maritial.get(),
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
                conn.close()
                messagebox.showinfo("Successfully Updated",str(mess),parent=self.root)                       
            except Exception as es:
                messagebox.showerror("Error",f"Something went wrong:{str(es)}",parent=self.root) 
    
        
if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
    