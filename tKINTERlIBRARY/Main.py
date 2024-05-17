from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import time
import datetime
from time import strftime
import mysql.connector

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

# Creating a class for the Login Window
class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1550x800+0+0")
        
        # Loading images
        img1 = Image.open("Source/Librarybg.jpg")
        img1 = img1.resize((1530, 800), Image.Resampling.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        bg_lbl = Label(self.root, image=self.photoImg1)
        bg_lbl.place(x=0, y=0, width=1530, height=800)
        
        # Adding title
        title = Label(bg_lbl, text="Library Management System", font=("times new roman", 42, "bold"), bg="orange", fg="red")
        title.place(x=0, y=0, width=1550, height=70)
        
        # Creating a frame for login
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=200, width=340, height=430)
        
        # Adding login icon
        img1 = Image.open("Source/usericon.png")
        img1 = img1.resize((90, 90), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=200, width=90, height=90)
        
        # Adding "Admin Login" text
        get_str = Label(frame, text="Admin Login", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=85)
        
        # Adding username field
        self.txtuser = StringVar()
        username = Label(frame, text="Username", font=("times new roman", 12, "bold"), fg="white", bg="black")
        username.place(x=70, y=125)
        txtuser = ttk.Entry(frame, textvariable=self.txtuser, font=("times new roman", 15, "bold"))
        txtuser.place(x=40, y=150, width=270)
        
        # Adding password field
        self.txtpass = StringVar()
        password = Label(frame, text="Password", font=("times new roman", 12, "bold"), fg="white", bg="black")
        password.place(x=70, y=195)
        txtpass = ttk.Entry(frame, textvariable=self.txtpass, font=("times new roman", 15, "bold"), show="*")
        txtpass.place(x=40, y=220, width=270)
        
        # Adding login button
        btn_login = Button(frame, text="Login", borderwidth=3, relief=RAISED, command=self.login, cursor="hand2", font=("times new roman", 16, "bold"), fg="white", bg="red", activebackground="#B00857")
        btn_login.place(x=110, y=270, width=120, height=35)
        
        # Adding "New User Register" button
        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=320, width=160)
        
        # Adding "Forget Password" button
        forgetbtn = Button(frame, text="Forget Password", command=self.forgot_password_window, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgetbtn.place(x=10, y=340, width=160)

    # Method to open the registration window
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)
        
    # Method to handle login
    def login(self):
        if self.txtuser.get() == "Pratik" and self.txtpass.get() == "Ketan":
            messagebox.showinfo("Success", "Welcome to Library Management System...")
            self.new_window = Toplevel(self.root)
            self.app = LibraryManagementSystem(self.new_window)
        elif self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="242424", database="USER")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (self.txtuser.get(), self.txtpass.get()))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Enter Library Management System")
                if open_main > 0:
                    pass
                    self.new_window = Toplevel(self.root)
                    self.app = LibraryManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
                conn.commit()
                self.clear()
                conn.close()
                
    # Method to clear the login fields
    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")
    
    # Method to open the "Forget Password" window
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please Enter the Email address to reset password")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="242424", database="USER")
                my_cursor = conn.cursor()
                query = ("SELECT * FROM register WHERE email=%s")
                value = (self.txtuser.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please enter a valid username")
                else:
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("340x450+610+200")
                    self.root2.configure(bg="white")
                    
                    l = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                    l.place(x=0, y=10, relwidth=1)

                    security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
                    security_Q.place(x=50, y=80)

                    self.combo_securiy_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                    self.combo_securiy_Q["values"] = ("Select", "Your Birth Place", "Your Nickname", "Your Blood Group")
                    self.combo_securiy_Q.place(x=50, y=110, width=250)
                    self.combo_securiy_Q.current(0)

                    security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
                    security_A.place(x=50, y=150)
                    self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                    self.txt_security.place(x=50, y=180, width=250)

                    new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
                    new_password.place(x=50, y=220)
                    self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"), show='*')
                    self.txt_newpass.place(x=50, y=250, width=250)

                    btn = Button(self.root2, text="Reset", command=self.reset_pass, font=("times new roman", 15, "bold"), fg="White", bg="green")
                    btn.place(x=120, y=290, width=100)
                    
                    self.reset_email = self.txtuser.get()

                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}")

    def reset_pass(self):
        if self.combo_securiy_Q.get() == "Select" or self.txt_security.get() == "" or self.txt_newpass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="242424", database="USER")
                cur = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s AND security_question=%s AND security_answer=%s"
                value = (self.reset_email, self.combo_securiy_Q.get(), self.txt_security.get())
                cur.execute(query, value)
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please select the correct Security Question / Enter Answer", parent=self.root2)
                else:
                    query = "UPDATE register SET password=%s WHERE email=%s"
                    value = (self.txt_newpass.get(), self.reset_email)
                    cur.execute(query, value)
                    conn.commit()
                    messagebox.showinfo("Info", "Your password has been reset, please login with new password", parent=self.root2)
                    self.root2.destroy()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root2)

# Class for Registeration window
class Register:
    def __init__(self, root):
            self.root = root
            self.root.title("Register")
            self.root.geometry("1600x900+0+0")
            self.var_fname = StringVar()
            self.var_lname = StringVar()
            self.var_contact = StringVar()
            self.var_email = StringVar()
            self.var_securityQ = StringVar()
            self.var_SecurityA = StringVar()
            self.var_pass = StringVar()
            self.var_confpass = StringVar()
            
            # Adding background images
            self.bg = ImageTk.PhotoImage(file="Source/registerbg.jpg")
            bg_lbl = Label(self.root, image=self.bg)
            bg_lbl.place(x=0, y=0,relheight=1,relwidth=1)
            
            self.bg1 = ImageTk.PhotoImage(file="Source/Registerone.jpg")
            left_lbl = Label(self.root, image=self.bg1)
            left_lbl.place(x=50, y=100, width=470, height=550)
            
            frame = Frame(self.root, bg="white")
            frame.place(x=520, y=100, width=800, height=550)
            
            register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
            register_lbl.place(x=50, y=50)
            
            fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
            fname.place(x=50, y=100)
            self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
            self.fname_entry.place(x=50, y=130, width=250)
            
            l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
            l_name.place(x=370, y=100)
            self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
            self.txt_lname.place(x=370, y=130, width=250)
            
            contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
            contact.place(x=50, y=170)
            self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
            self.txt_contact.place(x=50, y=200, width=250)
            
            email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
            email.place(x=370, y=170)
            self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
            self.txt_email.place(x=370, y=200, width=250)
            
            security_Q = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white", fg="black")
            security_Q.place(x=50, y=240)
            self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
            self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Nick name", "Your Blood Group")
            self.combo_security_Q.place(x=50, y=270, width=250)
            self.combo_security_Q.current(0)
            
            security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
            security_A.place(x=370, y=240)
            self.txt_security = ttk.Entry(frame, textvariable=self.var_SecurityA, font=("times new roman", 15, "bold"))
            self.txt_security.place(x=370, y=270, width=250)
            
            pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
            pswd.place(x=50, y=310)
            self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15, "bold"))
            self.txt_pswd.place(x=50, y=340, width=250)
            
            confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
            confirm_pswd.place(x=370, y=310)
            self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
            self.txt_confirm_pswd.place(x=370, y=340, width=250)
            
            self.var_check = IntVar()
            self.checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", bg='white', font=("times new roman", 12, "bold"), onvalue=1, offvalue=0)
            self.checkbtn.place(x=50, y=380)
            
            img = Image.open("Source/btnregister.png")
            img = img.resize((200, 65), Image.Resampling.LANCZOS)
            self.photoimage = ImageTk.PhotoImage(img)
            b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), fg="white",bg='white')
            b1.place(x=10, y=420, width=200)
            
            img1 = Image.open("Source/image.png")
            img1 = img1.resize((200, 75), Image.Resampling.LANCZOS)
            self.photoimage1 = ImageTk.PhotoImage(img1)
            b1 = Button(frame, image=self.photoimage1, command=self.return_login, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), fg="white",bg='white')
            b1.place(x=330, y=420, width=200)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be the same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="242424", database="USER")
                my_cursor = conn.cursor()

                query = "SELECT * FROM register WHERE email=%s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email", parent=self.root)
                else:
                    insert_query = "INSERT INTO register (first_name, last_name, contact_no, email, security_question, security_answer, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    insert_data = (self.var_fname.get(), self.var_lname.get(), self.var_contact.get(), self.var_email.get(), self.var_securityQ.get(), self.var_SecurityA.get(), self.var_pass.get())
                    my_cursor.execute(insert_query, insert_data)

                    conn.commit()
                    messagebox.showinfo("Success", "Registered Successfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Error during registration: {e}", parent=self.root)
            finally:
                if 'conn' in locals() and conn.is_connected():
                    conn.close()
                    my_cursor.close()


    def return_login(self):
        self.root.destroy()

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # =====================Variables==========================
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.auther_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook = StringVar()
        self.lateratefine_var = StringVar()
        self.dateoverdue = StringVar()
        self.finallprice = StringVar()

        # =======================TitleLabel=========================
        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="white", fg="crimson", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        def time():
            string = strftime('%I:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
        
        lbl = Label(lbltitle, font=('times new roman', 15, 'bold'), background='purple', foreground='white')
        lbl.place(x=0, y=0, width=150)
        time()

        # ====================Dataframe=======================
        DataFrame = Frame(self.root, bd=20, padx=12, relief=RIDGE)
        DataFrame.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft = LabelFrame(DataFrame, bd=12, padx=10, relief=RIDGE, fg="darkgreen", font=("arial", 12, "bold"), text="Library Membership Information")
        DataFrameLeft.place(x=0, y=5, width=800, height=350)

        lblMember = Label(DataFrameLeft, text="Member Type", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)
        cmbMember = ttk.Combobox(DataFrameLeft, font=("times new roman", 15, "bold"), width=27, textvariable=self.member_var, state='readonly')
        cmbMember["values"] = ("Admin Staff", "Student", "Lecturer")
        cmbMember.grid(row=0, column=1)

        lblPRN_NO = Label(DataFrameLeft, text="PRN_No:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblPRN_NO.grid(row=1, column=0, sticky=W)
        txtPRN_NO = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.prn_var)
        txtPRN_NO.grid(row=1, column=1)

        lblTitle = Label(DataFrameLeft, text="ID NO:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.id_var)
        txtTitle.grid(row=2, column=1)

        lblFirstname = Label(DataFrameLeft, text="First Name:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblFirstname.grid(row=3, column=0, sticky=W)
        txtFirstname = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.firstname_var)
        txtFirstname.grid(row=3, column=1)

        lblLastname = Label(DataFrameLeft, text="Last Name:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblLastname.grid(row=4, column=0, sticky=W)
        txtLastname = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.lastname_var)
        txtLastname.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, text="Address1:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.address1_var)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, text="Address2:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.address2_var)
        txtAddress2.grid(row=6, column=1)

        lblPostcode = Label(DataFrameLeft, text="Postcode:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblPostcode.grid(row=7, column=0, sticky=W)
        txtPostcode = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.postcode_var)
        txtPostcode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, text="Mobile:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.mobile_var)
        txtMobile.grid(row=8, column=1)

        lblBookID = Label(DataFrameLeft, text="Book ID:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblBookID.grid(row=1, column=2, sticky=W)
        txtBookID = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.bookid_var)
        txtBookID.grid(row=1, column=3)

        lblBookTitle = Label(DataFrameLeft, text="Book Title:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblBookTitle.grid(row=2, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.booktitle_var)
        txtBookTitle.grid(row=2, column=3)

        lblAuthor = Label(DataFrameLeft, text="Author:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblAuthor.grid(row=3, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.auther_var)
        txtAuthor.grid(row=3, column=3)

        lblDateBorrowed = Label(DataFrameLeft, text="Date Borrowed:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblDateBorrowed.grid(row=4, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.dateborrowed_var)
        txtDateBorrowed.grid(row=4, column=3)

        lblDateDue = Label(DataFrameLeft, text="Date Due:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblDateDue.grid(row=5, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.datedue_var)
        txtDateDue.grid(row=5, column=3)

        lblDaysOnBook = Label(DataFrameLeft, text="Days On Book:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblDaysOnBook.grid(row=6, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.daysonbook)
        txtDaysOnBook.grid(row=6, column=3)

        lblLateReturnFine = Label(DataFrameLeft, text="Late Return Fine:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblLateReturnFine.grid(row=7, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.lateratefine_var)
        txtLateReturnFine.grid(row=7, column=3)

        lblDateOverDue = Label(DataFrameLeft, text="Date Over Due:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblDateOverDue.grid(row=8, column=2, sticky=W)
        txtDateOverDue = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.dateoverdue)
        txtDateOverDue.grid(row=8, column=3)

        lblFinalPrice = Label(DataFrameLeft, text="Final Price:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblFinalPrice.grid(row=9, column=2, sticky=W)
        txtFinalPrice = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=20, textvariable=self.finallprice)
        txtFinalPrice.grid(row=9, column=3)

        # ==================Data Frame Right==================
        DataFrameRight = LabelFrame(DataFrame, bd=12, padx=20, relief=RIDGE, fg="darkgreen", font=("arial", 12, "bold"), text="Book Details")
        DataFrameRight.place(x=810, y=5, width=660, height=350)

        self.txtBox = Text(DataFrameRight, font=("arial", 12, "bold"), width=35, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky='ns')

        listBooks = ['Cinderella', 'Game Design', 'Ancient Rome', 'Made in Africa', 'Sleeping Beauty', 'London Street', 'Nigeria', 'Python Programming', 'Machine Learning', 'Data Science']
        
        def SelectBook(event):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if x == "Cinderella":
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Cinderella")
                self.auther_var.set("Unknown")
            elif x == "Game Design":
                self.bookid_var.set("BKID5455")
                self.booktitle_var.set("Game Design")
                self.auther_var.set("Unknown")
            elif x == "Ancient Rome":
                self.bookid_var.set("BKID5456")
                self.booktitle_var.set("Ancient Rome")
                self.auther_var.set("Unknown")
            elif x == "Made in Africa":
                self.bookid_var.set("BKID5457")
                self.booktitle_var.set("Made in Africa")
                self.auther_var.set("Unknown")
            elif x == "Sleeping Beauty":
                self.bookid_var.set("BKID5458")
                self.booktitle_var.set("Sleeping Beauty")
                self.auther_var.set("Unknown")
            elif x == "London Street":
                self.bookid_var.set("BKID5459")
                self.booktitle_var.set("London Street")
                self.auther_var.set("Unknown")
            elif x == "Nigeria":
                self.bookid_var.set("BKID5460")
                self.booktitle_var.set("Nigeria")
                self.auther_var.set("Unknown")
            elif x == "Python Programming":
                self.bookid_var.set("BKID5461")
                self.booktitle_var.set("Python Programming")
                self.auther_var.set("Unknown")
            elif x == "Machine Learning":
                self.bookid_var.set("BKID5462")
                self.booktitle_var.set("Machine Learning")
                self.auther_var.set("Unknown")
            elif x == "Data Science":
                self.bookid_var.set("BKID5463")
                self.booktitle_var.set("Data Science")
                self.auther_var.set("Unknown")
        
        listBox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=8)
        listScrollbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END, item)

        # =================Button Frame=======================
        FrameButton = Frame(self.root, bd=20, relief=RIDGE)
        FrameButton.place(x=0, y=530, width=1530, height=70)

        btnAddData = Button(FrameButton, command=self.add_data, text="Add Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=0)

        btnShowData = Button(FrameButton, command=self.show_data, text="Show Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnShowData.grid(row=0, column=1)

        btnUpdate = Button(FrameButton, command=self.update, text="Update", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(FrameButton, command=self.delete, text="Delete", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnDelete.grid(row=0, column=3)

        btnReset = Button(FrameButton, command=self.reset, text="Reset", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnReset.grid(row=0, column=4)

        btnExit = Button(FrameButton, command=self.iExit, text="Exit", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnExit.grid(row=0, column=5)

        # =================Information Frame===================
        FrameDetails = Frame(self.root, bd=20, relief=RIDGE)
        FrameDetails.place(x=0, y=600, width=1530, height=195)

        table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg='orange')
        table_frame.place(x=0, y=2, width=1500, height=180)

        xscroll = Scrollbar(table_frame, orient=HORIZONTAL)
        yscroll = Scrollbar(table_frame, orient=VERTICAL)
        self.library_table = ttk.Treeview(table_frame, column=("membertype", "prnno", "title", "firstname", "lastname", "address1", "address2", "postid", "mobile", "bookid", "booktitle", "author", "dateborrowed", "datedue", "days", "latereturnfine", "dateoverdue", "finalprice"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No.")
        self.library_table.heading("title", text="ID No.")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address1")
        self.library_table.heading("address2", text="Address2")
        self.library_table.heading("postid", text="Post Code")
        self.library_table.heading("mobile", text="Mobile")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days On Book")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table['show'] = 'headings'
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fatch_data()

    def add_data(self):
        if self.prn_var.get() == "" or self.id_var.get() == "" or self.firstname_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="242424", database="user")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into members values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.member_var.get(),
                    self.prn_var.get(),
                    self.id_var.get(),
                    self.firstname_var.get(),
                    self.lastname_var.get(),
                    self.address1_var.get(),
                    self.address2_var.get(),
                    self.postcode_var.get(),
                    self.mobile_var.get(),
                    self.bookid_var.get(),
                    self.booktitle_var.get(),
                    self.auther_var.get(),
                    self.dateborrowed_var.get(),
                    self.datedue_var.get(),
                    self.daysonbook.get(),
                    self.lateratefine_var.get(),
                    self.dateoverdue.get(),
                    self.finallprice.get()
                ))
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Success", "Member has been inserted successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}")

    def update(self):
        if self.prn_var.get() == "" or self.id_var.get() == "" or self.firstname_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="242424", database="user")
                my_cursor = conn.cursor()
                query = """
                    UPDATE members
                    SET 
                        Member = %s,
                        PRN_NO = %s,
                        firstname = %s,
                        lastname = %s,
                        address1 = %s,
                        address2 = %s,
                        postcode = %s,
                        mobile = %s,
                        bookid = %s,
                        booktittle = %s,
                        Auther = %s,
                        dateborrowed = %s,
                        datedue = %s,
                        DaysOnBook = %s,
                        latereturnfine = %s,
                        dateoverdue = %s,
                        finalprice = %s
                    WHERE ID = %s
                """
                values = (
                    self.member_var.get(),
                    self.prn_var.get(),
                    self.firstname_var.get(),
                    self.lastname_var.get(),
                    self.address1_var.get(),
                    self.address2_var.get(),
                    self.postcode_var.get(),
                    self.mobile_var.get(),
                    self.bookid_var.get(),
                    self.booktitle_var.get(),
                    self.auther_var.get(),
                    self.dateborrowed_var.get(),
                    self.datedue_var.get(),
                    self.daysonbook.get(),
                    self.lateratefine_var.get(),
                    self.dateoverdue.get(),
                    self.finallprice.get(),
                    self.id_var.get()
                )
                my_cursor.execute(query, values)
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Success", "Member has been updated successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}")



    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="242424", database="user")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from members")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for row in rows:
                self.library_table.insert('', END, values=row)
            conn.commit()
        conn.close()

    def show_data(self):
        self.txtBox.insert(END, "Member Type:\t\t" + self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN No:\t\t" + self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID No:\t\t" + self.id_var.get() + "\n")
        self.txtBox.insert(END, "First Name:\t\t" + self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "Last Name:\t\t" + self.lastname_var.get() + "\n")
        self.txtBox.insert(END, "Address1:\t\t" + self.address1_var.get() + "\n")
        self.txtBox.insert(END, "Address2:\t\t" + self.address2_var.get() + "\n")
        self.txtBox.insert(END, "Post Code:\t\t" + self.postcode_var.get() + "\n")
        self.txtBox.insert(END, "Mobile:\t\t" + self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID:\t\t" + self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title:\t\t" + self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Author:\t\t" + self.auther_var.get() + "\n")
        self.txtBox.insert(END, "Date Borrowed:\t\t" + self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "Date Due:\t\t" + self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "Days on Book:\t\t" + self.daysonbook.get() + "\n")
        self.txtBox.insert(END, "Late Return Fine:\t\t" + self.lateratefine_var.get() + "\n")
        self.txtBox.insert(END, "Date Over Due:\t\t" + self.dateoverdue.get() + "\n")
        self.txtBox.insert(END, "Final Price:\t\t" + self.finallprice.get() + "\n")

    def reset(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.auther_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook.set("")
        self.lateratefine_var.set("")
        self.dateoverdue.set("")
        self.finallprice.set("")
        self.txtBox.delete("1.0", END)

    def iExit(self):
        iExit = messagebox.askyesno("Library Management System", "Do you want to exit?")
        if iExit > 0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_var.get() == "" or self.id_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="242424", database="user")
                my_cursor = conn.cursor()
                query = "delete from members where PRN_NO=%s"
                value = (self.prn_var.get(),)
                my_cursor.execute(query, value)
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Success", "Member has been deleted successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}")

    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        contents = self.library_table.item(cursor_row)
        row = contents['values']
        
        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.auther_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook.set(row[14])
        self.lateratefine_var.set(row[15])
        self.dateoverdue.set(row[16])
        self.finallprice.set(row[17]) 
if __name__ == "__main__":
    main()

    
