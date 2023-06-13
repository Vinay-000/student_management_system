from tkinter import *
from tkinter import ttk, messagebox
import pymysql

class student():
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1370x700+0+0")          # screen size
        title=Label(self.root,text="Student Management System",relief= GROOVE,font=("times new roman",50,"bold"), bg="#00f0f0",fg="red" )  ## setting up the titile
        title.pack(side=TOP,fill=X)

        ######--- all variables (Data base connection----- #############


        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt= StringVar()


        ######--- manage frame----- #############
        Manage_Frame= Frame(self.root,bd=4,relief=RIDGE,bg="#3399ff")
        Manage_Frame.place(x=28,y=100,width=450,height=585)

        m_title= Label(Manage_Frame,text="Manage student",bg="#3399ff",fg="black",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan =2, pady=20)

        ## Roll no####
        lbl_roll= Label(Manage_Frame,text="Roll No",bg="#3399ff",fg="white",font=("times new roman",20,"bold"))    ## label visualization
        lbl_roll.grid(row=1, column=0, pady=10,padx=20,sticky = "w")
        txt_roll= Entry(Manage_Frame,textvariable= self.Roll_No_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE) # Roll_no entry tab formatting
        txt_roll.grid(row=1, column=1, pady=10,padx=20,sticky = "w")
        #name####
        lbl_name = Label(Manage_Frame, text="Name", bg="#3399ff", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame, textvariable= self.name_var,  font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        ### Email###
        lbl_email = Label(Manage_Frame, text="Email", bg="#3399ff", fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_email = Entry(Manage_Frame,textvariable= self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        #### Gender ######

        lbl_gender = Label(Manage_Frame, text="Gender", bg="#3399ff", fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame, textvariable= self.gender_var, font=("times new roman", 13, "bold"),state="readonly") ## setting drop down list for gender
        combo_gender["values"] = ('Male','Female',"other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        ###contact
        lbl_contact = Label(Manage_Frame, text="contact", bg="#3399ff", fg="white", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_contact = Entry(Manage_Frame,textvariable= self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")


        #### Date of birth
        lbl_dob = Label(Manage_Frame, text="Date of birth", bg="#3399ff", fg="white", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_dob = Entry(Manage_Frame,textvariable= self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        ## Address

        lbl_add = Label(Manage_Frame, text="Address", bg="#3399ff", fg="white", font=("times new roman", 20, "bold"))
        lbl_add.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_add = Text(Manage_Frame,width=30,height=3, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE) # text field for address
        self.txt_add.grid(row=7, column=1, pady=10, padx=20, sticky="w")


        #####################3 Button Frame#######################################
        btn_frame= Frame(Manage_Frame,bd=3,relief=RIDGE,bg="#996633")
        btn_frame.place(x=15,y=525,width=420)

        add_btn=Button(btn_frame,text="Add",width=10,bg="#00ff00",command =self.add_student).grid(row=0,column=0,padx=10,pady=10)
        delete_btn = Button(btn_frame, text="Delete", bg="#ff0000",width=10,command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        update_btn = Button(btn_frame, text="Update", bg="yellow",width=10,command =self.update_data).grid(row=0, column=1, padx=10, pady=10)
        clr_btn = Button(btn_frame, text="Clear",bg="#808080", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)



        ######--- Details frame----- #############  Data visualization tab
        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="blue")
        Details_Frame.place(x=500, y=100, width=880, height=585)

        lbl_search = Label(Details_Frame, text="Search by", bg="Blue", fg="white",
                        font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20,sticky="w")

        combo_search = ttk.Combobox(Details_Frame, textvariable= self.search_by, font=("times new roman", 13, "bold"), width=10,state="readonly")
        combo_search["values"] = ("Roll_no", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Details_Frame,textvariable= self.search_txt, font=("times new roman", 10, "bold"), width=20,bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        search_btn = Button(Details_Frame, text="Search", width=10,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        show_all_btn = Button(Details_Frame, text="Show all", width=10,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        ######--- Table  frame----- #############
        Table_Frame = Frame(Details_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x =Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table= ttk.Treeview(Table_Frame,column=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_y,yscrollcommand=scroll_x)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)


        self.Student_table.heading("roll",text="Roll No")           ## Headings for Data
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="gender")
        self.Student_table.heading("contact", text="contact")
        self.Student_table.heading("dob", text="Date of birth")
        self.Student_table.heading("address", text="Address")


        self.Student_table["show"]= "headings"                      ## Table formating
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=100)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_student(self):  # creating functionality for Add button.

        if self.Roll_No_var.get()=="" or self.name_var.get()== "":      ## check if its blank if yes pop up error
            messagebox.showerror(" Error:", ' Name and Roll no required')
        else:
            con=pymysql.connect(host="localhost",user="root",password="Winervinay",database="sms")
            cur=con.cursor()
            print("Connect")
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),   ## sql query for adding entry in data base
                                                                         self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.txt_add.get('1.0',END)))
            con.commit()                                                                                ## commit changes in data base
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "  Saved  ")

    def fetch_data(self):                               ### functionn for getting all data from data base and show in table
        con = pymysql.connect(host="localhost", user="root", password="Winervinay", database="sms")
        cur = con.cursor()
        cur.execute("select * from student")
        rows=cur.fetchall()
        if len(rows)!=0:                    ## errase existing data if any in table
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):                ## clear data field in left side( name, roll_no, contact, email, add, gender)
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_add.delete("1.0",END)

    def get_cursor(self,ev):    # get the functionallity to select line item in a table
        curosor_row=self.Student_table.focus()
        contents=self.Student_table.item(curosor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_add.delete("1.0",END)
        self.txt_add.insert(END, row[6])


    def update_data(self):          ## update the existin data in database
        con = pymysql.connect(host="localhost", user="root", password="Winervinay", database="sms")
        cur = con.cursor()
        print("Connect")
        cur.execute("update student set name =%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(  #### sql quesry for updating data
                                                                         self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.txt_add.get('1.0', END),
                                                                         self.Roll_No_var.get()))
        con.commit()
        self.fetch_data()
        con.close()
        self.clear()

        messagebox.showinfo("Success", "  Saved  ")

    def delete_data(self):                      ## delete selected data in shown table
        con = pymysql.connect(host="localhost", user="root", password="Winervinay", database="sms")
        cur = con.cursor()
        cur.execute("delete from student where roll_no =%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):                  ## search data result based on given inputs
        con = pymysql.connect(host="localhost", user="root", password="Winervinay", database="sms")
        cur = con.cursor()
        cur.execute("select * from student where " + str(self.search_by.get())+ " like '%"+ str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()





class student(): ## mail function to show the results 
    pass
    root= Tk()
    obj= student(root)
    root.mainloop()
