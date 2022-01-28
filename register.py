# Import the required libraries
from tkinter import *
from tkinter import ttk, messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import ImageTk,Image
import pymysql

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
        txt_email=ttk.Combobox(frame1,font=("times new roman",12),textvariable=self.var_gender,state='readonly',justify=CENTER)
        txt_email["value"]=("Male","Female","Other")
        txt_email.place(x=50,y=140,width=250)
        
        self.var_martial=StringVar()
        martial=Label(frame1,text="Martial Status",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=370,y=110)
        txt_martial=ttk.Combobox(frame1,font=("times new roman",12),textvariable=self.var_martial,state='readonly',justify=CENTER)
        txt_martial["value"]=("Single","Cohabitation","Maried","Widow","Divorced","Living apart","Engaged")
        txt_martial.place(x=370,y=140,width=250)
        
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

        self.var_security=StringVar()
        answer=Label(frame1,text="Security ID",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=370,y=170)
        txt_answer=Entry(frame1,font=("times new roman",15),textvariable=self.var_security).place(x=370,y=200,width=250)

        # Row 4
        self.var_email=StringVar()
        password=Label(frame1,text="Email",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=50,y=230)
        txt_password=Entry(frame1,font=("times new roman",12),textvariable=self.var_email).place(x=50,y=260,width=250)
        
        self.var_phone=StringVar()
        cpassword=Label(frame1,text="Phone",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=370,y=230)
        txt_cpassword=Entry(frame1,font=("times new roman",12),textvariable=self.var_phone).place(x=370,y=260,width=250)

        # Row 5
        self.var_city=StringVar()
        password=Label(frame1,text="City",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=50,y=290)
        txt_password=Entry(frame1,font=("times new roman",12),textvariable=self.var_city).place(x=50,y=320,width=250)
        
        self.var_postcode=StringVar()
        cpassword=Label(frame1,text="Postcode",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=370,y=290)
        txt_cpassword=Entry(frame1,font=("times new roman",12),textvariable=self.var_postcode).place(x=370,y=320,width=250)        
        
        # Row 6
        self.var_address=StringVar()
        password=Label(frame1,text="Address",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=50,y=350)
        txt_password=Entry(frame1,font=("times new roman",12),textvariable=self.var_address).place(x=50,y=380,width=250)

        # Row 7
        self.var_password=StringVar()
        password=Label(frame1,text="Password",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=50,y=410)
        txt_password=Entry(frame1,font=("times new roman",12),textvariable=self.var_password).place(x=50,y=440,width=250)
        
        self.var_confirm=StringVar()
        confirm=Label(frame1,text="Confirm Password",font=("time new roman",12,"bold"),fg="white",bg="black").place(x=370,y=410)
        txt_confirm=Entry(frame1,font=("times new roman",12),textvariable=self.var_confirm).place(x=370,y=440,width=250)      
        
        
        # Terms & conditions
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Hereby Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="black",font=("times time roman",10,"italic","bold"),fg="red").place(x=45,y=480)
        
        # Button register
        btn_register=Button(frame1,text="Register Now",font=("times new roman",18,"bold"),cursor="hand2",bg="yellow")
        btn_register.place(x=50,y=520)
        
        # Button login
        btn_login=Button(self.root,text="Sign In",command=self.login_window,font=("times new roman",15,"bold"),cursor="hand2",bg="lightblue")
        btn_login.place(x=155,y=295,width=110)
    
    
    # Switch to login mainpage
    def login_window(self):
        root.destroy()
        import login
        
                 
root=Tk()
obj=User_Register(root) 
root.mainloop()