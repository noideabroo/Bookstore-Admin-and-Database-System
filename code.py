import tkinter as tk
from functools import partial
import mysql.connector
from tkinter import PhotoImage

def show_frame(frame):
    frame.tkraise()
    
def validateLogin(my_login, my_password):
    mycursor.execute ("insert into details values('"+my_login.get()+"','"+my_password.get()+"')")
    mydb.commit()
    return

window = tk.Tk()
window.state("zoomed")
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)
window.title("Batata Book Store")
icon=PhotoImage(file="book.png")
window.iconphoto(True,icon)

#mysql

mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists practice")
mycursor.execute("use practice")

mycursor.execute("create table if not exists details(username varchar(100) not null,password varchar(100) not null)")
mycursor.execute("create table if not exists stuff(product varchar(100) not null,price int not null)")

mydb.commit()


#frame1

frame1=tk.Frame(window,bg="#7070db")
frame2=tk.Frame(window,bg="light blue")
frame3=tk.Frame(window,bg="light blue")
frame4=tk.Frame(window,bg="light blue")
frame5=tk.Frame(window,bg="light blue")

for frame in (frame1,frame2,frame3,frame4,frame5):
    frame.grid(row=0,column=0,sticky="NSEW")
    
#frame1 code

global price
price=[]

frame1_title=tk.Label(frame1,text="WELCOME TO THE BATATA",bg="#7070db",fg="white",font="Stencil 45 bold")
frame1_title.pack(fill="x")

login_label=tk.Label(frame1,text="\n\n\n\n\nEnter your username",bg="#7070db",fg="white",font="Corbel 14")
login_label.pack()

my_login=tk.StringVar()

login_entry_box=tk.Entry(frame1,textvariable=my_login,font="Corbel 12",width=22)
login_entry_box.pack()

password_label=tk.Label(frame1,text="\nEnter your password",bg="#7070db",fg="white",font="Corbel 14")
password_label.pack(fill="x")

my_password=tk.StringVar()

password_entry_box=tk.Entry(frame1,textvariable=my_password,font="Corbel 12",width=22)
password_entry_box.pack()

validateLogin = partial(validateLogin, my_login, my_password)

btn=tk.Button(frame1,text="Save",height=1,width=10,relief="raised",command=validateLogin)
btn.pack(pady=10)

frame1_btn=tk.Button(frame1,text="Enter",height=2,width=20,command=lambda:show_frame(frame2))
frame1_btn.pack(pady=30)


#frame2

frame2_title1=tk.Label(frame2,text="KIDS",bg="light blue",fg="white",font="Stencil 30 bold")
frame2_title1.pack(padx=20, pady=195,side=tk.RIGHT,anchor=tk.N)

def addbook1():
    book1_title=tk.Label(frame5,text="beauty and beast\t\t70 Dhs",font="none 14")
    book1_title.pack(pady=10)
    mycursor.execute("""insert into stuff values ("beauty and the beast",70)""")
    mydb.commit()

def addbook2():
    book2_title=tk.Label(frame5,text="judy moody\t\t30 Dhs",font="none 14")
    book2_title.pack(pady=10)
    mycursor.execute("""insert into stuff values ("judy moody",30)""")
    mydb.commit()

def addbook3():
    book3_title=tk.Label(frame5,text="the cat in the hat\t\t49.5 Dhs",font="none 14")
    book3_title.pack(pady=10)
    mycursor.execute("""insert into stuff values ("the cat in the hat",49.5)""")
    mydb.commit()

def addbook4():
    book4_title=tk.Label(frame5,text="matilda\t\t37 Dhs",font="none 14")
    book4_title.pack(pady=10)
    price.append(price4)
    mycursor.execute("""insert into stuff values ("matilda",37)""")
    mydb.commit()

def addbook5():
        book5_title=tk.Label(frame5,text="alice in wonderland\t\t52 Dhs",font="none 14")
        book5_title.pack(pady=10)
        mycursor.execute("""insert into stuff values ("alice in wonderland",52)""")
        mydb.commit()

frame2_title=tk.Label(frame2,text="BOOKS",bg="light blue",fg="white",font="Stencil 45 bold")
frame2_title.pack()

image1=PhotoImage(file= "beauty and beast.PNG")                                          
picture_label=tk.Label (frame2,image=image1)
picture_label.pack(padx=20, pady=15,side=tk.LEFT,anchor=tk.N)                                             #book1 
btn1=tk.Button(frame2,text="BUY  70 Dhs",bg="green",fg="white",command=addbook1)
btn1.place(x=70,y=370)
    
image2=PhotoImage(file="judy moody.PNG")
picture_label=tk.Label (frame2,image=image2)
picture_label.pack(padx=20, pady=20,side=tk.LEFT,anchor=tk.N)                                        #book2
btn2=tk.Button(frame2,text="BUY  30 Dhs",bg="green",fg="white",command=addbook2)
btn2.place(x=300,y=375)
    

image3=PhotoImage(file="the cat in the hat.PNG")
picture_label=tk.Label (frame2,image=image3)
picture_label.pack(padx=20, pady=20,side=tk.LEFT,anchor=tk.N)                                        #book3
btn3=tk.Button(frame2,text="BUY  49.5 Dhs",bg="green",fg="white",command=addbook3)
btn3.place(x=520,y=375)

image4=PhotoImage(file="matilda.PNG")
picture_label=tk.Label (frame2,image=image4)
picture_label.pack(padx=20, pady=20,side=tk.LEFT,anchor=tk.N)                                         #book4
btn4=tk.Button(frame2,text="BUY  37 Dhs",bg="green",fg="white",command=addbook4)
btn4.place(x=750,y=375)

image5=PhotoImage(file="alice in wonderland.PNG")
picture_label=tk.Label (frame2,image=image5)
picture_label.pack(padx=20, pady=20,side=tk.LEFT,anchor=tk.N)                                                       #book5
btn5=tk.Button(frame2,text="BUY 52  Dhs",bg="green",fg="white",command=addbook5)
btn5.place(x=975,y=375)

frame2_btn=tk.Button(frame2,text="NEXT",command=lambda:show_frame(frame3))
frame2_btn.place(x=570,y=600)


#frame3

frame3_title=tk.Label(frame3,text="young adult",bg="light blue",fg="white",font="Stencil 45 bold")
frame3_title.pack()

frame3_btn=tk.Button(frame3,text="NEXT",command=lambda:show_frame(frame4))
frame3_btn.place(x=570,y=600)

def addbook6():
    book6_title=tk.Label(frame5,text="famous 5\t\t45 Dhs",font="none 14")
    book6_title.pack(pady=10)
    mycursor.execute("""insert into stuff values ("famous 5 ",45)""")
    mydb.commit()
    
def addbook7():
    book7_title=tk.Label(frame5,text="harry potter\t\t50 Dhs",font="none 14")
    book7_title.pack(pady=10)
    mycursor.execute("""insert into stuff values ("harry potter",50)""")
    mydb.commit()
    
def addbook8():
    book8_title=tk.Label(frame5,text="paper towns\t\t35 Dhs",font="none 14")
    book8_title.pack(pady=10)
    mycursor.execute("""insert into stuff values ("harry potter",35)""")
    mydb.commit()
    
def addbook9():
    book9_title=tk.Label(frame5,text="six of crows\t\t49 Dhs",font="none 14")
    book9_title.pack(pady=10)
    mycursor.execute("""insert into stuff values ("six of crows",49)""")
    mydb.commit()
    
def addbook10():
    book10_title=tk.Label(frame5,text="the hunger games\t\t37 Dhs",font="none 14")
    book10_title.pack(pady=10)
    mycursor.execute("""insert into stuff values ("the hunger games",37)""")
    mydb.commit()
    
image6=PhotoImage(file= "famous 5.PNG")
picture_label=tk.Label (frame3,image=image6)
picture_label.pack(padx=20, pady=15,side=tk.LEFT,anchor=tk.N)                                                                           #book6
btn1=tk.Button(frame3,text="BUY 45 Dhs",bg="green",fg="white",command=addbook6)
btn1.place(x=70,y=370)

image7=PhotoImage(file="harry potter.PNG")
picture_label=tk.Label (frame3,image=image7)
picture_label.pack(padx=20, pady=20,side=tk.LEFT,anchor=tk.N)                                                                            #book7
btn2=tk.Button(frame3,text="BUY 50 Dhs",bg="green",fg="white",command=addbook7)
btn2.place(x=300,y=375)

image8=PhotoImage(file="paper towns.PNG")
picture_label=tk.Label (frame3,image=image8)
picture_label.pack(padx=20, pady=20,side=tk.LEFT,anchor=tk.N)                                                                        #book8
btn3=tk.Button(frame3,text="BUY 35 Dhs",bg="green",fg="white",command=addbook8)
btn3.place(x=520,y=375)

image9=PhotoImage(file="six of crows.PNG")
picture_label=tk.Label (frame3,image=image9)
picture_label.pack(padx=20, pady=20,side=tk.LEFT,anchor=tk.N)                                                                         #book9
btn4=tk.Button(frame3,text="BUY 49 Dhs",bg="green",fg="white",command=addbook9)
btn4.place(x=750,y=375)

image10=PhotoImage(file="the hunger games.PNG")
picture_label=tk.Label (frame3,image=image10)
picture_label.pack(padx=20, pady=20,side=tk.LEFT,anchor=tk.N)                                                                     #book10
btn5=tk.Button(frame3,text="BUY 37 Dhs",bg="green",fg="white",command=addbook10)
btn5.place(x=975,y=375)


# frame 4
frame4_title=tk.Label(frame4,text="adult",bg="light blue",fg="white",font="Stencil 45 bold")
frame4_title.pack()

frame4_btn=tk.Button(frame4,text="CHECKOUT",command=lambda:show_frame(frame5))
frame4_btn.place(x=570,y=600)

def addbook11():
    book11_title=tk.Label(frame5,text="cinder\t\t38 Dhs",font="none 14")
    book11_title.pack(pady=10)
    mycursor.execute("""insert into stuff values ("cinder",38)""")
    mydb.commit()
    
def addbook12():
    book12_title=tk.Label(frame5,text="the 7 husbands\t\t45 Dhs",font="none 14")
    book12_title.pack(pady=10)
    mycursor.execute("""insert into stuff values ("the 7 husbands",45)""")
    mydb.commit()
    
def addbook13():
    book13_title=tk.Label(frame5,text="the girl on the train\t\t57 Dhs",font="none 14")
    book13_title.pack(pady=10)
    mycursor.execute("""insert into stuff values ("the girl on the train",57)""")
    mydb.commit()
    
def addbook14():
    book14_title=tk.Label(frame5,text="to kill a mockingbird\t\t23 Dhs",font="none 14")
    book14_title.pack(pady=10)
    mycursor.execute("""insert into stuff values ("to kill a mockingbird",23)""")
    mydb.commit()
    
def addbook15():
    book15_title=tk.Label(frame5,text="we were liars\t\t42 Dhs",font="none 14")
    book15_title.pack(pady=10)
    mycursor.execute("""insert into stuff values ("we were liars",42)""")
    mydb.commit()


image11=PhotoImage(file= "cinder.PNG")
picture_label=tk.Label (frame4,image=image11)
picture_label.pack(padx=20, pady=15,side=tk.LEFT,anchor=tk.N)                                                #book11
btn1=tk.Button(frame4,text="BUY 38 Dhs",bg="green",fg="white",command=addbook11)
btn1.place(x=70,y=370)

image12=PhotoImage(file="the 7 husbands.PNG")
picture_label=tk.Label (frame4,image=image12)
picture_label.pack(padx=20, pady=20,side=tk.LEFT,anchor=tk.N)                                                    #book12
btn2=tk.Button(frame4,text="BUY 45 Dhs",bg="green",fg="white",command=addbook12)
btn2.place(x=300,y=375)

image13=PhotoImage(file="the girl on the train.PNG")
picture_label=tk.Label (frame4,image=image13)
picture_label.pack(padx=20, pady=20,side=tk.LEFT,anchor=tk.N)                                                        #book13
btn3=tk.Button(frame4,text="BUY 57 Dhs",bg="green",fg="white",command=addbook13)
btn3.place(x=520,y=375)

image14=PhotoImage(file="to kill a mocking bird.PNG")
picture_label=tk.Label (frame4,image=image14)
picture_label.pack(padx=20, pady=20,side=tk.LEFT,anchor=tk.N)                                                          #book14
btn4=tk.Button(frame4,text="BUY 23 Dhs",bg="green",fg="white",command=addbook14)
btn4.place(x=750,y=375)

image15=PhotoImage(file="we were liars.PNG")
picture_label=tk.Label (frame4,image=image15)
picture_label.pack(padx=20, pady=20,side=tk.LEFT,anchor=tk.N)                                                     #book15
btn5=tk.Button(frame4,text="BUY 42 Dhs",bg="green",fg="white",command=addbook15)
btn5.place(x=975,y=375)



#frame5

frame5_title=tk.Label(frame5,text="BILL",bg="light blue",fg="white",font="Stencil 45 bold")
frame5_title.pack(fill="x")

frame5_title2=tk.Label(frame5,text="PRODUCT\t\tPRICE",bg="light blue",fg="black",font="none 18")
frame5_title2.pack(pady=30)

frame5_btn=tk.Button(frame5,text="Enter",command=lambda:show_frame(frame1))
frame4_btn.pack()


show_frame(frame1)
    
window.mainloop()
