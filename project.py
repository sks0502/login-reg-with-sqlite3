from tkinter import *
from tkinter import Text,Tk
import os
import sqlite3
from tkinter import ttk, messagebox

#---------------------------------------------------------------Login Function --------------------------------------
def clear():
	userentry.delete(0,END)
	passentry.delete(0,END)

def close():
	win.destroy()	


def login():

        user1=user_name.get()
        pass1=password.get()

        conn = sqlite3.connect('reg.db')
        with conn:
                cursor=conn.cursor()
                
        cursor.execute('CREATE TABLE IF NOT EXISTS Register (first_name TEXT NOT NULL ,last_name TEXT NOT NULL ,age INTEGER NOT NULL ,var TEXT,city TEXT,address TEXT,user TEXT PRIMARY KEY NOT NULL ,passwd TEXT NOT NULL,very_pass TEXT NOT NULL)')  
        cursor.execute('select * from Register Where user=? AND passwd=?',(user1,pass1))

        if cursor.fetchone() is not None:
                messagebox.showinfo("Success" , "Successfully Login" , parent = win)
                close()
                main_window()
                
        else:
                
                messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)

        conn.commit()
	
	
#__________________main_window_______________________

    
def main_window():
    
    global main_window_screen
    main_window_screen = Toplevel(win)
    main_window_screen.title("hospital management")
    main_window_screen.geometry("400x250")
    
    Label(main_window_screen, text="Welcome to Hospital Management",bg="light blue", width="300", height="2", font=("Calibri", 16,"bold")).pack()
    
    


#---------------------register function----------------------- 


def signup():
        def database():
                name1=first_name.get()
                sname1=last_name.get()
                age1=age.get()
                var1=var.get()
                city1=city.get()
                add1=add.get()
                user1=user_name.get()
                pass1=password.get()
                pass2=very_pass.get()
                if first_name.get()=="" or last_name.get()=="" or age.get()=="" or city.get()=="" or add.get()=="" or user_name.get()=="" or password.get()=="" or very_pass.get()=="" :
                        messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
                elif password.get() != very_pass.get():
                        messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)

                else:
                        try:
                                conn=sqlite3.connect('reg.db')
                                cursor=conn.cursor()
                                cursor.execute("select * from Register where user=?",user1)
                                row = cursor.fetchone()
                                if row!=None:
                                        messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
                                else:
                                        cursor.execute('CREATE TABLE IF NOT EXISTS Register (first_name TEXT NOT NULL ,last_name TEXT NOT NULL ,age INTEGER NOT NULL ,var TEXT,city TEXT,address TEXT,user TEXT PRIMARY KEY NOT NULL ,passwd TEXT NOT NULL,very_pass TEXT NOT NULL)')
                                        cursor.execute('INSERT INTO Register(first_name,last_name,age,var,city,address,user,passwd,very_pass) VALUES(?,?,?,?,?,?,?,?,?)',(name1,sname1,age1,var1,city1,add1,user1,pass1,pass2))
                                        conn.commit()
                                        messagebox.showinfo("Success" , "Ragistration Successfull" , parent = winsignup)
                                        clear()
                                        switch()
                        except Exception as es:
                                messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = winsignup)
        
	

        
# close signup function			
        def switch():
                winsignup.destroy()

# clear data function
        def clear():
            first_name.delete(0,END)
            last_name.delete(0,END)
            age.delete(0,END)
            var.set("Male")
            city.delete(0,END)
            add.delete(0,END)
            user_name.delete(0,END)
            password.delete(0,END)
            very_pass.delete(0,END)
	
						
                                                                

                                                                             # start Signup Window	
        winsignup = Tk() 
        winsignup.title("sign up ")
        winsignup.maxsize(width=500 ,  height=600)
        winsignup.minsize(width=500 ,  height=600)


#heading label
        heading = Label(winsignup , text = "Signup" , font = 'Verdana 20 bold')
        heading.place(x=80 , y=60)

# form data label
        first_name = Label(winsignup, text= "First Name :" , font='Verdana 10 bold')
        first_name.place(x=80,y=130)

        last_name = Label(winsignup, text= "Last Name :" , font='Verdana 10 bold')
        last_name.place(x=80,y=160)

        age = Label(winsignup, text= "Age :" , font='Verdana 10 bold')
        age.place(x=80,y=190)

        Gender = Label(winsignup, text= "Gender :" , font='Verdana 10 bold')
        Gender.place(x=80,y=220)

        city = Label(winsignup, text= "City :" , font='Verdana 10 bold')
        city.place(x=80,y=260)

        add = Label(winsignup, text= "Address :" , font='Verdana 10 bold')
        add.place(x=80,y=290)

        user_name = Label(winsignup, text= "User Name :" , font='Verdana 10 bold')
        user_name.place(x=80,y=320)

        password = Label(winsignup, text= "Password :" , font='Verdana 10 bold')
        password.place(x=80,y=350)

        very_pass = Label(winsignup, text= "Verify Password:" , font='Verdana 10 bold')
        very_pass.place(x=80,y=380)

# Entry Box ------------------------------------------------------------------

        first_name = StringVar()
        last_name = StringVar()
        age = IntVar(winsignup, value='0')
        var= StringVar()
        city= StringVar()
        add = StringVar()
        user_name = StringVar()
        password = StringVar()
        very_pass = StringVar()

	
        first_name = Entry(winsignup, width=40 , textvariable = first_name)
        first_name.place(x=200 , y=133)


	
        last_name = Entry(winsignup, width=40 , textvariable = last_name)
        last_name.place(x=200 , y=163)

        age = Entry(winsignup, width=40, textvariable=age)
        age.place(x=200 , y=193)

	
        Radiobutton(winsignup,text='Male', value="Male", variable = var).place(x= 200 , y= 220)
        Radiobutton(winsignup,text='Female', value="Female", variable = var).place(x= 200 , y= 238)


        city = Entry(winsignup, width=40,textvariable = city)
        city.place(x=200 , y=263)


        add = Entry(winsignup, width=40 , textvariable = add)
        add.place(x=200 , y=293)

	
        user_name = Entry(winsignup, width=40,textvariable = user_name)
        user_name.place(x=200 , y=323)

	
        password = Entry(winsignup, width=40, textvariable = password)
        password.place(x=200 , y=353)

	
        very_pass= Entry(winsignup, width=40 ,show="*" , textvariable = very_pass)
        very_pass.place(x=200 , y=383)


# button login and clear

        btn_signup = Button(winsignup, text = "Signup" ,font='Verdana 10 bold', command = database)
        btn_signup.place(x=200, y=413)


        btn_login = Button(winsignup, text = "Clear" ,font='Verdana 10 bold' , command = clear)
        btn_login.place(x=280, y=413)


        sign_up_btn = Button(winsignup , text="Switch To Login" , command = switch )
        sign_up_btn.place(x=350 , y =20)


        winsignup.mainloop()

#--------------------------------------------------------------

    
win = Tk()

#app title
win.title("hostpital mangement system")

#size of main window
win.maxsize(width=500 ,  height=500)
win.minsize(width=500 ,  height=500)

#heading label to main window 
Label(text="HOSPITAL MANGEMENT", bg="light blue", width="300", height="4", font=("Calibri", 16,"bold")).pack()
Label(win , text="").pack()

heading = Label(win , text = "Login" , font = 'Verdana 25 bold')
heading.place(x=80 , y=150)

#.............................


username = Label(win, text= "User Name :" , font='Verdana 10 bold')
username.place(x=80,y=220)

userpass = Label(win, text= "Password :" , font='Verdana 10 bold')
userpass.place(x=80,y=260)

# entry box

user_name = StringVar()
password = StringVar()
	
userentry = Entry(win, width=40 , textvariable = user_name)
userentry.focus()
userentry.place(x=200 , y=223)

passentry = Entry(win, width=40, show="*" ,textvariable = password)
passentry.place(x=200 , y=260)

# button  (login and clear)

btn_login = Button(win, text = "Login" ,font='Verdana 10 bold',command = login)
btn_login.place(x=200, y=293)


btn_login = Button(win, text = "Clear" ,font='Verdana 10 bold', command = clear)
btn_login.place(x=260, y=293)

# signup button

sign_up_btn = Button(win , text="Register" , command = signup )
sign_up_btn.place(x=420 , y =70)


win.mainloop()


