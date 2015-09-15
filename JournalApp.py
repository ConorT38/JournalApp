#Any and all of the code that has been commented out, are predecessor of the database connection. Keep for legacy sake.
#Author: Conor Thompson, NCI NetSoc VP

from tkinter import *
import datetime
import sys
import re
import hashlib
import os
import MySQLdb as mdb
from tkinter.filedialog import askopenfilename


def main():

    def Chat():
        man.destroy()
        Chat_main()

    def Entry():
        man.destroy()
        Entry_main()

    man = Tk()
    man.configure(bg="#867970")
    man.title("NetSoc App")

    man.minsize(width=300, height=200)
    man.maxsize(width=300, height=200)

    La = Label(man, anchor=CENTER, text="Choose a mode: ", bg="#867970", font=("Helvetica", 12))
    La.place(x=85, y=5)


    Ba = Button(man, text="Chat", command=Chat, bg="#3D352A", width=10)
    Ba.place(y=100, x=40)

    Bb = Button(man, text="Entries", command=Entry, bg="#3D352A", width=10)
    Bb.place(y=100, x=150)

def Chat_main():

    con = mdb.connect('localhost', 'conor', 'blizzardofozz1', 'database1')
        
    
    def check_user(event):
        #path = "C:\Python34\\Journal\\"
        #path = str(path)
        username1 = str(E1.get())

        passw = E2.get()
        passw2 = str(passw)

        with con:
            
            cur = con.cursor()

            cur.execute("SELECT * FROM users WHERE username='"+username1+"' AND password='"+passw2+"'")
            
            #r = open(path+username1+"\\Password\\Password.txt",'r')
            #pas = r.read()
            #pas = str(pas)

            cur.fetchall()
            
            if(cur.rowcount ==1):
                for row in cur.fetchall():
                    username = row['username']
                    fname = row['fname']
                    lname = row['lname']
                    
                messagebox.showinfo("Access Granted", "Login successful!")
                top.destroy()
                Chat_loggedin(username1)
               

            else: 
                messagebox.showinfo("Access Denied", "That is the wrong Username/Password.")
                print("that is the wrong thing")
                print(passw2)
                E1.delete(0, END)
                E2.delete(0, END)

    def signup1():
        top.destroy()
        signup()
        
    top = Tk()
    top.configure(bg="#867970")
    top.title("Login")

    top.minsize(width=300, height=200)
    top.maxsize(width=300, height=200)

    #username 
    L1 = Label(top, anchor=CENTER, text="User Name: ", bg="#867970")
    L1.place( x=20, y=20)
    E1 = Entry(bd=2)
    E1.place(x=100, y=20)

    #password
    L2 = Label(top, anchor=CENTER, text="Password: ", bg="#867970")
    L2.place( x=20, y=60)
    E2= Entry(bd=2, show="*")
    E2.place(x=100, y=60)

    #submit
    submit = Button(top, text="Enter", width=10, command=check_user, bg="#3D352A")
    submit.place(x=100, y=100)

    signupbtn = Button(top, text="Signup", width=10,command=signup1, bg="#3D352A")
    signupbtn.place(x=215, y=167)
    top.bind("<Return>", check_user)
    submit.bind("<Button-1>", check_user)

    #top.mainloop()

    
def Entry_main():

    con = mdb.connect('localhost', 'conor', 'blizzardofozz1', 'database1')
        
    
    def check_user(event):
        #path = "C:\Python34\\Journal\\"
        #path = str(path)
        username1 = str(E1.get())

        passw = E2.get()
        passw2 = str(passw)

        with con:
            
            cur = con.cursor()

            cur.execute("SELECT * FROM users WHERE username='"+username1+"' AND password='"+passw2+"'")
            
            #r = open(path+username1+"\\Password\\Password.txt",'r')
            #pas = r.read()
            #pas = str(pas)

            cur.fetchall()
            
            if(cur.rowcount ==1):
                for row in cur.fetchall():
                    username = row['username']
                    fname = row['fname']
                    lname = row['lname']
                    
                messagebox.showinfo("Access Granted", "Login successful!")
                top.destroy()
                Entry_loggedin(username1)
               

            else: 
                messagebox.showinfo("Access Denied", "That is the wrong Username/Password.")
                print("that is the wrong thing")
                print(passw2)
                E1.delete(0, END)
                E2.delete(0, END)

    def signup1():
        top.destroy()
        signup()
        
    top = Tk()
    top.configure(bg="#867970")
    top.title("Login")

    top.minsize(width=300, height=200)
    top.maxsize(width=300, height=200)

    #username 
    L1 = Label(top, anchor=CENTER, text="User Name: ", bg="#867970")
    L1.place( x=20, y=20)
    E1 = Entry(bd=2)
    E1.place(x=100, y=20)

    #password
    L2 = Label(top, anchor=CENTER, text="Password: ", bg="#867970")
    L2.place( x=20, y=60)
    E2= Entry(bd=2, show="*")
    E2.place(x=100, y=60)

    #submit
    submit = Button(top, text="Enter", width=10, command=check_user, bg="#3D352A")
    submit.place(x=100, y=100)

    signupbtn = Button(top, text="Signup", width=10,command=signup1, bg="#3D352A")
    signupbtn.place(x=215, y=167)
    top.bind("<Return>", check_user)
    submit.bind("<Button-1>", check_user)

    #top.mainloop()

def Chat_loggedin(username):

    import socket, threading, time, msvcrt
    
    con = mdb.connect('localhost', 'conor', 'blizzardofozz1', 'database1')
    cur = con.cursor()

    curr_time = datetime.datetime.now().time()
    now = curr_time.isoformat()
    now = str(now)

    username = str(username)
    
    
    logn = Tk()
    logn.configure(bg="#8B8B8B")
    logn.title(username+"'s Journal")
    
    logn.minsize(width=500, height=400)
    logn.maxsize(width=500, height=400)

    Ldate = Label(logn, text="Date: "+now, bg="#8B8B8B")
    Ldate.place(x=380, y=20)

    Ltitle = Label(logn, text="Title: ", bg="#8B8B8B")
    Ldesc = Label(logn, text="Description: ", bg="#8B8B8B")
    Lcontent = Label(logn, text="Entry: ", bg="#8B8B8B")

    Ltitle.place(x=20, y=45)
    Ldesc.place(x=20, y=85)
    Lcontent.place(x=20, y=125)

    title = Entry(bd=2, width=40)
    title.place(x=100, y=45)
    description = Entry(bd=2, width=40)
    description.place(x=100, y=85)
    content = Text(bd=2, width=40, height=12)
    content.place(x=100, )    
    

    #save button
    def save():
        
        filetitle = str(title.get())
        filecontent = str(content.get('1.0', END))
        filedesc = str(description.get())
        

        with con:
            cur.execute("INSERT INTO entries(title, description, content, date) VALUES('"+filetitle+"','"+filedesc+"','"+filecontent+"',NOW())")
            
        #path = str("C:\Python34\Journal\\"+username+"\\Entries\\")

        #f = open(path+filetitle+".txt", 'w')
        #f.write("Title: "+filetitle+"\n\n\nDescription: "+filedesc+"\n\n\nTime: "+now+"\n\n\nEntry: "+filecontent)
        #f.close()
        messagebox.showinfo("Saved!", "Entry name: '"+filetitle+"' successfully saved!")

        title.delete(0, END)
        description.delete(0, END)
        #content.delete(0, 'end -1c')
        
        
    savebtn = Button(logn, text="Save", width=10, command=save, bg="#5A8B8B")
    savebtn.place(x=320, y=365)

    #close button
    def close():
        logn.destroy()
        sys.exit(0)

    def logout():
        logn.destroy()
        Entry_main()
        
        
    sendbtn = Button(logn, text="Send", width=10, command=close, bg="#5A8B8B")
    sendbtn.place(x=415, y=365)

    logoutbtn = Button(logn, text="Logout", width=10, command=logout, bg="#5A8B8B")
    logoutbtn.place(x=20, y=365)


def Entry_loggedin(username):
    
    con = mdb.connect('localhost', 'conor', 'blizzardofozz1', 'database1')
    cur = con.cursor()

    curr_time = datetime.datetime.now().time()
    now = curr_time.isoformat()
    now = str(now)

    username = str(username)
    
    
    logn = Tk()
    logn.configure(bg="#8B8B8B")
    logn.title(username+"'s Journal")
    
    logn.minsize(width=500, height=400)
    logn.maxsize(width=500, height=400)
    
    Ldate = Label(logn, text="Date: "+now, bg="#8B8B8B")
    Ldate.place(x=380, y=20)

    Ltitle = Label(logn, text="Title: ", bg="#8B8B8B")
    Ldesc = Label(logn, text="Description: ", bg="#8B8B8B")
    Lcontent = Label(logn, text="Entry: ", bg="#8B8B8B")

    Ltitle.place(x=20, y=45)
    Ldesc.place(x=20, y=85)
    Lcontent.place(x=20, y=125)

    title = Entry(bd=2, width=40)
    title.place(x=100, y=45)
    description = Entry(bd=2, width=40)
    description.place(x=100, y=85)
    content = Text(bd=2, width=40, height=8)
    content.place(x=100, y=125)    
    

    #save button
    def save():
        
        filetitle = str(title.get())
        filecontent = str(content.get('1.0', END))
        filedesc = str(description.get())
        

        with con:
            cur.execute("INSERT INTO entries(title, description, content, date) VALUES('"+filetitle+"','"+filedesc+"','"+filecontent+"',NOW())")
            
        #path = str("C:\Python34\Journal\\"+username+"\\Entries\\")

        #f = open(path+filetitle+".txt", 'w')
        #f.write("Title: "+filetitle+"\n\n\nDescription: "+filedesc+"\n\n\nTime: "+now+"\n\n\nEntry: "+filecontent)
        #f.close()
        messagebox.showinfo("Saved!", "Entry name: '"+filetitle+"' successfully saved!")

        title.delete(0, END)
        description.delete(0, END)
        #content.delete(0, 'end -1c')
        
        
    savebtn = Button(logn, text="Save", width=10, command=save, bg="#5A8B8B")
    savebtn.place(x=320, y=365)

    #close button
    def close():
        logn.destroy()
        sys.exit(0)

    def logout():
        logn.destroy()
        Entry_main()

    def browse():
        filename = askopenfilename()
        f = open(filename, 'r')
        r = f.read()
        messagebox.showinfo("Selected File:", "You have selected: "+filename+" \n\n"+r)

    Lb1 = Listbox(logn, selectmode=SINGLE)
    Lb1.place(x=415,y=300)
    browsebtn = Button(logn, text="Browse", width=10, command=browse, bg="#5A8B8B")
    browsebtn.place(x=110, y=365)
    
    closebtn = Button(logn, text="Close", width=10, command=close, bg="#5A8B8B")
    closebtn.place(x=415, y=365)

    logoutbtn = Button(logn, text="Logout", width=10, command=logout, bg="#5A8B8B")
    logoutbtn.place(x=20, y=365)

    
def signup():
    
    con = mdb.connect('localhost', 'conor', 'blizzardofozz1', 'database1')
    cur = con.cursor()

    def Csignup(event):

        errors = list()

        fnamec = str(Efname.get())
        lnamec = str(Elname.get())
        unamec = str(Euname.get())
        pasc = str(Epas1.get())
        pasc2 = str(Epas2.get())

        if(pasc != pasc2):
            errors.insert(0, "Passwords do not match")
            

        fnamematch = re.match('^[a-zA-Z0-9]',fnamec)
        lnamematch = re.match('^[a-zA-Z0-9]',lnamec)
        unamematch = re.match('^[a-zA-Z0-9]',unamec)
        pasc1 = re.match('^[a-zA-Z0-9]',pasc)

        if(not fnamematch):
            errors.insert(1, "Not a valid first name")
            
        if(not lnamematch):
            errors.insert(2, "Not a valid last name")
            
        if(not unamematch):
            errors.insert(3, "Not a valid username")

        if(len(pasc) < 5):
            errors.insert(4, "Password too short, must be at least 5 characters long")
            

        if (pasc1 and fnamematch and lnamematch and unamematch and not errors):
            #pasc = hash(pasc)
            pasc2 = str(pasc)
            
            with con:
                
                cur.execute("INSERT INTO users(fname, lname, username, password) VALUES('"+fnamec+"','"+lnamec+"','"+unamec+"','"+pasc2+"')")
                cur.close()

            #os.mkdir("C:\\Python34\\Journal\\"+unamec)
            #os.mkdir("C:\\Python34\\Journal\\"+unamec+"\\Password")
            #os.mkdir("C:\\Python34\\Journal\\"+unamec+"\\Entries")
            #p = open("C:\\Python34\\Journal\\"+unamec+"\\Password\\Password.txt",'w')
            
           #p.write(pasc2)
            #p.close()
            messagebox.showinfo("Success!", "You have made an account!")
            si.destroy()
            Entry_main()

        elif(errors):
            for i in range(len(errors)):
                messagebox.showinfo("Failed", errors[i]+"\n")
            
        
    si = Tk()
    si.configure(bg="#85CDCD")
    si.title("Signup")

    si.minsize(width=300, height=300)
    si.maxsize(width=300, height=300)

    #First name 
    fname = Label(si, anchor=CENTER, text="First Name: ", bg="#85CDCD")
    fname.place( x=20, y=20)
    Efname = Entry(bd=2)
    Efname.place(x=100, y=20)

     #Last name 
    lname = Label(si, anchor=CENTER, text="Last Name: ", bg="#85CDCD")
    lname.place( x=20, y=60)
    Elname = Entry(bd=2)
    Elname.place(x=100, y=60)

     #Username 
    uname = Label(si, anchor=CENTER, text="User Name: ", bg="#85CDCD")
    uname.place( x=20, y=100)
    Euname = Entry(bd=2)
    Euname.place(x=100, y=100)

    #password
    pas1 = Label(si, anchor=CENTER, text="Password: ", bg="#85CDCD")
    pas1.place( x=20, y=140)
    Epas1= Entry(bd=2, show="*")
    Epas1.place(x=100, y=140)

    #confirm password
    pas2 = Label(si, anchor=CENTER, text="Confirm: ", bg="#85CDCD")
    pas2.place( x=20, y=180)
    Epas2= Entry(bd=2, show="*")
    Epas2.place(x=100, y=180)

    #submit
    submit = Button(si, text="Enter", width=10, command=Csignup, bg="#5A8B8B")
    submit.place(x=100, y=220)
    
    si.bind("<Return>", Csignup)
    submit.bind("<Button-1>", Csignup)

    def back():
        si.destroy()
        Entry_main()

    Backbtn = Button(si, text="Back", width=5,command=back, bg="#5A8B8B")
    Backbtn.place(x=5, y=265)
    



main()     
    
