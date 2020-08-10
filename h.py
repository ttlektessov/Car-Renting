from tkinter import *
import ctypes
from tkinter.messagebox import *
import tkinter.messagebox
import sqlite3
def save(event):
        num=ent4.get()
        length=len(num)
        q1=ent1.get()
        q2=ent2.get()
        q3=ent3.get()
        q4=ent4.get()
        Cost=0 ## Total rent cost
        pum=0 ## Pick up month
        dom=0 ##Drop of month
        pud=0 ## Pick up day
        dod=0 ## Drop off day
        cm=0 ## Cost for month
        cd=0 ## Cost for day
        if (q1!="" and q2!="" and q3!="" and q4!=""):
            if (length>=10):
                City=ent1.get()
                Address=ent2.get()
                Name=ent3.get()
                PhoneNumber=ent4.get()
                PickupDate= var1.get() +' '+ var2.get()
                PickupTime= var5.get() + ':'+ var6.get()
                DropoffDate= var3.get() + ' ' + var4.get()
                DropoffTime= var7.get() + ':' + var8.get()
                Car=var9.get()
                Purpose=rad0.get()
                pud=int(var1.get())
                dod=int(var3.get()) ##Drop of day
                z=var2.get() ##Pick Up Month
                if(z=="January"):
                        pum=int(1)
                elif(z=="February"):
                        pum=int(2)
                elif(z=="March"):
                        pum=int(3)
                elif(z=="April"):
                        pum=int(4)
                elif(z=="May"):
                        pum=int(5)
                elif(z=="June"):
                        pum=int(6)
                elif(z=="July"):
                        pum=int(7)
                elif(z=="August"):
                        pum=int(8)
                elif(z=="September"):
                        pum=int(9)
                elif(z=="October"):
                        pum=int(10)
                elif(z=="November"):
                        pum=int(11)
                elif(z=="December"):
                        pum=int(12)
                x=var4.get()
                if(x=="January"):
                        dom=int(1)
                elif(x=="February"):
                        dom=int(2)
                elif(x=="March"):
                        dom=int(3)
                elif(x=="April"):
                        dom=int(4)
                elif(x=="May"):
                        dom=int(5)
                elif(x=="June"):
                        dom=int(6)
                elif(x=="July"):
                        dom=int(7)
                elif(x=="August"):
                        dom=int(8)
                elif(x=="September"):
                        dom=int(9)
                elif(x=="October"):
                        dom=int(10)
                elif(x=="November"):
                        dom=int(11)
                elif(x=="December"):
                        dom=int(12)
                if(dom>pum):
                        if(dod>pud):
                                cd=42
                                Cost=(30-((dod-pud)-(dom-pum)))*cd
                        elif(dod<pud):
                                cd=42
                                Cost=(30-((pud-dod)-(dom-pum)))*cd
                        elif(dod==pud):
                                cd=45
                                Cost=cd+((dom-pum)*cm)
                elif(dom==pum):
                        if(dod>pud):
                                cd=42
                                Cost=(dod-pud)*cd
                        elif(dod==pud):
                                cd=45
                                Cost=cd
                conn=sqlite3.connect('rentcar.db')
                with conn:
                        cursor=conn.cursor()
                cursor.execute('INSERT INTO rentcar (City,Address,Name,PhoneNumber,PickupDate,PickupTime,DropoffDate,DropoffTime,Purpose,Cost,Car) VALUES(?,?,?,?,?,?,?,?,?,?,?)',(City,Address,Name,PhoneNumber,PickupDate,PickupTime,DropoffDate,DropoffTime,Purpose,Cost,Car,))
                conn.commit()
                message="Success! You have been registered! Rent cost is: $"+str(Cost)
                title="result".title()
                tkinter.messagebox.showinfo(title, message)
            else:
                message="Wrong phone number"
                title="result".title()
                tkinter.messagebox.showinfo(title, message)
        else:
            message="Do not leave any empty fields"
            title="result".title()
            tkinter.messagebox.showinfo(title, message)
def readdb(event):
        global inf1
        global inf2
        global inf3
        global inf4
        global inf5
        global inf6
        global inf7
        global inf8
        global inf9
        global inf10
        q=ent.get()
        connn=sqlite3.connect('rentcar.db')
        with connn:
                cursor1=connn.cursor()
        cursor1.execute('SELECT * FROM rentcar')
        
        for row in cursor1.fetchall():
                        if (row[3]==q):
                                inf1=row[0]
                                inf2=row[1]
                                inf3=row[2]
                                inf4=row[3]
                                inf5=row[4]
                                inf6=row[5]
                                inf7=row[6]
                                inf8=row[7]
                                inf9=row[8]
                                inf10=row[9]
                                message="Name: "+str(inf3) +"\nCity: "+str(inf1) +"\nAdress: "+ str(inf2)+"\nPhone Number: "+ str(inf4) +"\nPickup Date: "+ str(inf5)+"\nPickup Time: "+ str(inf7)+"\nDropoff Date: "+ str(inf6)+"\nDropoff Time: "+ str(inf8)+"\nPurpose: "+ str(inf9)+"\nCost: "+ str(inf10)
                                title="result".title()
                                tkinter.messagebox.showinfo(title, message)
def find(event):
        global ent
        root2=Tk()
        root2.title("Find")
        root2.geometry('400x200')
        lab=Label(root2,text="Enter client's number:",font="Arial 15")
        lab.place(x=10,y=10)
        ent=Entry(root2,width=25,bd=3)
        ent.place(x=210,y=15)
        close=Button(root2, text=" Close ",font="Arial 20",bg="firebrick2", command=root2.destroy)
        close.place(x=270,y=130)
        fin=Button(root2,text="Find",font="Arial 20",bg="dodgerblue")
        fin.place(x=170,y=130)
        fin.bind('<Button-1>',readdb)
        
        
root = Tk()
global ent1
global ent2
global ent3
global var1
global newbutton1
global rad0
root.title("Car Hire – Search, Compare & Save")
root.geometry('1100x600')

img=PhotoImage(file="header-img.png")
ima=Label(root,image=img) 
ima.place(x=0,y=0, relwidth=1, relheight=1) 
ima.image=img

Startlabel= Label(root, text="Welcome to the Car Renting system!", font="Fixedsys 17 italic")
Startlabel.place(x = 580, y = 0)

lab = Label(root, text="City", font="Arial 15")
lab.place(x=10, y=0)
ent1=Entry(root,width=30,bd=3)
ent1.place(x=150, y=5)
lab = Label(root, text="Address", font="Arial 15")
lab.place(x=10, y=40)
ent2=Entry(root,width=30,bd=3)
ent2.place(x=150, y=45)
lab = Label(root, text="Full name", font="Arial 15")
lab.place(x=10, y=80)
ent3=Entry(root,width=30,bd=3)
ent3.place(x=150, y=85)
lab = Label(root, text="Phone number", font="Arial 15")
lab.place(x=10, y=120)
ent4=Entry(root,width=30,bd=3)
ent4.place(x=150, y=125)


lab = Label(root,text="<<More details>>", font="Helvetica 15")
lab.place(x=170, y=160)
lab = Label(root, text="Pick-up Date:", font="Arial 15")
lab.place(x=10, y=190)

mainframe = Frame(root)
mainframe.place(x=10,y=220)
var1=StringVar(root)
var1.set('Day')
choices=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
option1=OptionMenu(mainframe,var1,*choices)
option1.grid(row=1, column=1)

mainframe = Frame(root)
mainframe.place(x=75,y=220)
var2=StringVar(root)
var2.set('Month')
choices=['January','February','March','April','May','June','July','August','September','October','November','December']
option2=OptionMenu(mainframe,var2,*choices)
option2.grid(row=1, column=1)

lab = Label(root, text="Drop-off Date:", font="Arial 15")
lab.place(x=310, y=190)
mainframe = Frame(root)
mainframe.place(x=310,y=220)
var3=StringVar(root)
var3.set('Day')
choices=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
option3=OptionMenu(mainframe,var3,*choices)
option3.grid(row=1, column=1)

mainframe = Frame(root)
mainframe.place(x=375,y=220)
var4=StringVar(root)
var4.set('Month')
choices=['January','February','March','April','May','June','July','August','September','October','November','December']
option4=OptionMenu(mainframe,var4,*choices)
option4.grid(row=1, column=1)

lab = Label(root, text="Time:", font="Arial 14")
lab.place(x=10, y=260)
mainframe = Frame(root)
mainframe.place(x=10,y=290)
var5=StringVar(root)
var5.set('Hour')
choices=['07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
option5=OptionMenu(mainframe,var5,*choices)
option5.grid(row=1, column=1)
mainframe = Frame(root)
mainframe.place(x=80,y=290)
var6=StringVar(root)
var6.set('Minute')
choices=['00','15','30','45']
option6=OptionMenu(mainframe,var6,*choices)
option6.grid(row=1, column=1)

lab = Label(root, text="Time:", font="Arial 14")
lab.place(x=310, y=260)
mainframe = Frame(root)
mainframe.place(x=310,y=290)
var7=StringVar(root)
var7.set('Hour')
choices=['07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
option7=OptionMenu(mainframe,var7,*choices)
option7.grid(row=1, column=1)
mainframe = Frame(root)
mainframe.place(x=380,y=290)
var8=StringVar(root)
var8.set('Minute')
choices=['00','15','30','45']
option8=OptionMenu(mainframe,var8,*choices)
option8.grid(row=1, column=1)

mainframe = Frame(root)
mainframe.place(x=380,y=350)
var9=StringVar(root)
var9.set('Car')
choices=['Kia Sedona (Mini Van)','Ford F150 (Pickup)','Chevy Silverado (Pickup)','Toyota RAV4 (SUV)','Ford Focus','Hyundai Accent','Hyundai Santa Fe (SUV)','Nissan Versa','Toyota Yaris','Mitsubishi Mirage','Volkswagen Jetta','Chevrolet Cruze','Hyundai Elantra']
option4=OptionMenu(mainframe,var9,*choices)
option4.grid(row=1, column=1)

lab = Label(root, text="Purpose of rental", font="Arial 14")
lab.place(x=10, y=350)
rad0=StringVar()
rad0.set(1)
Radiobutton(root,text="Business", font="Arial 9", variable=rad0,value="Business").place(x=210, y=354)
Radiobutton(root,text="Leisure", font="Arial 9", variable=rad0,value="Leisure").place(x=290, y=354)

lab = Label(root, text="No credit card fees", font="Arial 10 italic")
lab.place(x=10, y=405)
lab = Label(root, text="No amendment fees", font="Arial 10 italic")
lab.place(x=10, y=425)
lab = Label(root, text="24/7 phone support", font="Arial 10 italic")
lab.place(x=10, y=445)
lab = Label(root, text="Longer you take, less you pay", font="Arial 10 italic")
lab.place(x=10, y=465)

close=Button(root, text=" Close ",font="Arial 20",bg="firebrick2", command=root.destroy)
close.place(x=630,y=440)
newbutton1=Button(root,text="Register", font="Arial 20",bg="white")
newbutton1.place(x=421,y=440)
newbutton1.bind('<Button-1>',save)
fin=Button(root,text="Find",font="Arial 20",bg="dodgerblue")
fin.place(x=550,y=440)
fin.bind('<Button-1>',find)

root.mainloop()
