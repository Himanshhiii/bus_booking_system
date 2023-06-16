from datetime import date
from tkinter import*
import sqlite3
from tkinter.messagebox import *
con=sqlite3.Connection("My_database")
cur=con.cursor()
root = Tk()
root.title('Bus Booking')



width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d"%(width,height))

def confirmation():
    showinfo("Status","TICKET BOOKED SUCCCESSFULLY")

def new_run():
    f17=Frame()
    f17.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f17,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f17,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'Royal Blue1', fg = 'red').grid(row=1,column=0,columnspan=5)
    Label(f17,text = "Add New Running Details", font=("Arial",25), fg = 'light green').grid(row=2,column=0,columnspan=5,pady=20)

    f18=Frame(f17)
    f18.grid(row = 3, column = 0, columnspan = 15,pady = 20)
    Label(f18,text = "Bus Id ", font=("Arial",15),fg='light green').grid(row=0,column=0,padx = 20)
    e23 = Entry(f18).grid(row=0,column=1)
    Label(f18,text = "Running Date ", font=("Arial",15),fg='light green').grid(row=0,column=2,padx=20)
    e24 = Entry(f18).grid(row=0,column=3)
    Label(f18,text = "Seat Available", font=("Arial",15),fg='light green').grid(row=0,column=4,padx = 10+10)
    e25 = Entry(f18).grid(row=0,column=5)
    
    button20 = Button(f18,text = "Add Run",font=("Arial",15),bg='light green').grid(row=0,column=6,padx=20,pady=20)
    button21 = Button(f18,text = "Delete Run",font=("Arial",15),fg='red',bg='light green').grid(row=0,column=7,padx=20,pady=20)

    button22 = Button(f17,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)

def new_route():
    f15=Frame()
    f15.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f15,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f15,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'Royal Blue1', fg = 'red').grid(row=1,column=0,columnspan=5)
    Label(f15,text = "Add Bus Route Details", font=("Arial",25), fg = 'light green').grid(row=2,column=0,columnspan=5,pady=20)

    f16=Frame(f15)
    f16.grid(row = 3, column = 0, columnspan = 15,pady = 20)
    Label(f16,text = "Route Id ", font=("Arial",15),fg='light green').grid(row=0,column=0,padx = 20)
    e20 = Entry(f16).grid(row=0,column=1)
    Label(f16,text = "Station Name ", font=("Arial",15),fg='light green').grid(row=0,column=2,padx=20)
    e21 = Entry(f16).grid(row=0,column=3)
    Label(f16,text = "Station ID ", font=("Arial",15),fg='light green').grid(row=0,column=4,padx = 10+10)
    e22 = Entry(f16).grid(row=0,column=5)
    
    button20 = Button(f16,text = "Add Route",font=("Arial",15),bg='light green').grid(row=0,column=6,padx=20,pady=20)
    button21 = Button(f16,text = "Delete Route",font=("Arial",15),fg='red',bg='light green').grid(row=0,column=7,padx=20,pady=20)

    button22 = Button(f15,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)

def new_bus():
    f13=Frame()
    f13.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f13,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f13,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'Royal Blue1', fg = 'red').grid(row=1,column=0,columnspan=5)
    Label(f13,text = "Add Bus Details", font=("Arial",25), fg = 'light green').grid(row=2,column=0,columnspan=5,pady=20)

    f14=Frame(f13)
    f14.grid(row = 3, column = 0, columnspan = 15,pady = 20)
    Label(f14,text = "Bus Id ", font=("Arial",15),fg='light green').grid(row=0,column=0,padx = 20)
    e14 = Entry(f14).grid(row=0,column=1)
    Label(f14,text = "Bus Type ", font=("Arial",15),fg='light green').grid(row=0,column=2,padx=20)
    menu1= StringVar()
    menu1.set("CHOOSE")
    drop2 = OptionMenu(f14, menu1,"AC 2x2","AC 3x2","Non-AC 2x2","Non-AC 3x2","AC Sleeper 2x2","Non-AC Sleeper 2x2").grid(row=0,column=3)
    Label(f14,text = "Capacity ", font=("Arial",15),fg='light green').grid(row=0,column=4,padx= 20)
    e16 = Entry(f14).grid(row=0,column=5)
    Label(f14,text = "Fare Rs ", font=("Arial",15),fg='light green').grid(row=0,column=6,padx = 10+10)
    e17 = Entry(f14).grid(row=0,column=7)
    Label(f14,text = "Operator ID", font=("Arial",15),fg='light green').grid(row=0,column=8, padx = 19+1)
    e18 = Entry(f14).grid(row=0,column=9)
    Label(f14,text = "Route ID", font=("Arial",15),fg='light green').grid(row=0,column=10, padx = 19+1)
    e19 = Entry(f14).grid(row=0,column=11)
    button17 = Button(f14,text = "Add",font=("Arial",15),bg='light green',anchor=CENTER).grid(row=1,column=0,padx=20,pady=20,columnspan=25)
    button18 = Button(f14,text = "Edit",font=("Arial",15),bg='light green',anchor=CENTER).grid(row=1,column=2,padx=20,pady=20,columnspan=15)

    button19 = Button(f13,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)

def new_operator():
    f11=Frame()
    f11.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f11,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f11,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'Royal Blue1', fg = 'red').grid(row=1,column=0,columnspan=5)
    Label(f11,text = "Add Bus Operator Details", font=("Arial",25), fg = 'green').grid(row=2,column=0,columnspan=5)

    f12=Frame(f11)
    f12.grid(row = 3, column = 0, columnspan = 15,pady = 20)
    Label(f12,text = "Operator Id ", font=("Arial",15),fg='green').grid(row=0,column=0,padx = 20)
    e9 = Entry(f12)
    e9.grid(row=0,column=1)
    Label(f12,text = "Name ", font=("Arial",15),fg='green').grid(row=0,column=2,padx=20)
    e10 = Entry(f12)
    e10.grid(row=0,column=3)
    Label(f12,text = "Address ", font=("Arial",15),fg='green').grid(row=0,column=4,padx= 20)
    e11 = Entry(f12)
    e11.grid(row=0,column=5)
    Label(f12,text = "Phone ", font=("Arial",15),fg='green').grid(row=0,column=6,padx = 10+10)
    e12 = Entry(f12)
    e12.grid(row=0,column=7)
    Label(f12,text = "E-mail", font=("Arial",15),fg='green').grid(row=0,column=8, padx = 19+1)
    e13 = Entry(f12)
    e13.grid(row=0,column=9)

    def add_op():
        cur.execute('insert into operator (op_id ,name ,address ,phone , email) values (?,?,?,?,?)',(int(e9.get()),e10.get(),e11.get(),int(e12.get()),e13.get()))
        cur.commit()

    button15 = Button(f12,text = "Add",font=("Arial",15),bg='light green',command=add_op).grid(row=0,column=10,padx=20)
    button16 = Button(f12,text = "Edit",font=("Arial",15),bg='light green',command=new_operator).grid(row=0,column=11,padx=20)

    button14 = Button(f11,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)

# def proceed_to(f5):
#     f6=Frame(f5)
#     f6.grid(row = 6, column = 0, columnspan = 10,pady = 20)
#     Label(f6,text = "Fill Passenger Details To Book The Bus Ticket", font=("Arial",25), bg = 'Royal Blue1', fg = 'red').grid(row=0,column=0,columnspan=15)
#     Label(f6,text = "Name", font=("Arial",15)).grid(row=1,column=0,padx = 20, pady = 20)
#     e4 = Entry(f6).grid(row=1,column=1)
#     Label(f6,text = "Gender", font=("Arial",15)).grid(row=1,column=2,padx = 20, pady = 20)
#     menu= StringVar()
#     menu.set("CHOOSE")
#     drop1 = OptionMenu(f6, menu,"MALE","FEMALE","TRANS").grid(row =  1,column =3)
#     Label(f6,text = "No. of seats.", font=("Arial",15)).grid(row=1,column=4,padx = 20, pady = 20)
#     e5 = Entry(f6).grid(row=1,column=5)
#     Label(f6,text = "Mobile No", font=("Arial",15)).grid(row=1,column=6,padx = 20, pady = 20)
#     e6 = Entry(f6).grid(row=1,column=7)
#     Label(f6,text = "Age", font=("Arial",15)).grid(row=1,column=8,padx = 20, pady = 20)
#     e7 = Entry(f6).grid(row=1,column=9)
#     button8 = Button(f6,text="Book Seat", font=("Arial",15), activebackground = 'light green', bg = 'SpringGreen3',command = confirmation).grid(row=1,column=10,padx=20,pady=20)
    
    
# def show_bus(f5):


#     f6=Frame(f5)
#     f6.grid(row = 5, column = 0, columnspan = 10,pady = 20)
#     Label(f6,text = "Select BUS ", font=("Arial",15),fg='light green').grid(row=0,column=0,padx = 20)
#     Label(f6,text = "Operator ", font=("Arial",15),fg='light green').grid(row=0,column=1,padx=20)
#     Label(f6,text = "Bus Type ", font=("Arial",15),fg='light green').grid(row=0,column=2,padx= 20)
#     Label(f6,text = "Availability ", font=("Arial",15),fg='light green').grid(row=0,column=3,padx = 10+10)
#     Label(f6,text = "Fare ", font=("Arial",15),fg='light green').grid(row=0,column=4, padx = 19+1)
#     button7 = Button(f6,text="Proceed to Book", font=("Arial",15), activebackground = 'light green', bg = 'SpringGreen3',command = lambda : proceed_to(f5)).grid(row=1,column=5,padx=20,pady=20)
    
def seat_book():
    f4 = Frame()
    f4.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f4,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f4,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'Royal Blue1', fg = 'red').grid(row=1,column=0,columnspan=5)
    Label(f4,text = "Enter Journey Details", font=("Arial",20), bg='light green', fg='green4',bd=5).grid(row=3,column=0,columnspan = 5,pady=20)

    f5 = Frame(f4,pady = 20)
    f5.grid(row = 4, column = 0, columnspan = 5) 
    Label(f5,text = "TO ", font=("Arial",10)).grid(row=0,column=0,sticky=E)
    e1 = Entry(f5)
    e1.grid(row=0,column=1)
    Label(f5,text = "FROM ", font=("Arial",10)).grid(row=0,column=2)
    e2 = Entry(f5)
    e2.grid(row=0,column=3)
    Label(f5,text = "JOURNEY DATE ", font=("Arial",10)).grid(row=0,column=4)
    e3 = Entry(f5)
    e3.grid(row=0,column=5)

    def proceed_to(f5,busch):
        
    
        f6=Frame(f5)
        f6.grid(row = 6, column = 0, columnspan = 10,pady = 20)
        Label(f6,text = "Fill Passenger Details To Book The Bus Ticket", font=("Arial",25), bg = 'Royal Blue1', fg = 'red').grid(row=0,column=0,columnspan=15)
        Label(f6,text = "Name", font=("Arial",15)).grid(row=1,column=0,padx = 20, pady = 20)
        e4 = Entry(f6)
        e4.grid(row=1,column=1)
        Label(f6,text = "Gender", font=("Arial",15)).grid(row=1,column=2,padx = 20, pady = 20)
        menu= StringVar()
        menu.set("CHOOSE")
        drop1 = OptionMenu(f6, menu,"MALE","FEMALE","TRANS").grid(row =  1,column =3)
        Label(f6,text = "No. of seats.", font=("Arial",15)).grid(row=1,column=4,padx = 20, pady = 20)
        e5 = Entry(f6)
        e5.grid(row=1,column=5)
        Label(f6,text = "Mobile No", font=("Arial",15)).grid(row=1,column=6,padx = 20, pady = 20)
        e6 = Entry(f6)
        e6.grid(row=1,column=7)
        Label(f6,text = "Age", font=("Arial",15)).grid(row=1,column=8,padx = 20, pady = 20)
        e7 = Entry(f6)
        e7.grid(row=1,column=9)
        
        def booked():
            resp = askyesno("Book","Total fare =1000 ")
            cur.execute('insert into Booking(Mobile ,Name ,sex ,age ,Bus_id , journey_date ,Ticket ,ref_id ,FromSt ,Tost ) values (?,?,?,?,?,?,?,?,?,?)',(int(e6.get()),e4.get(),menu.get(),int(e7.get()),busch,e3.get(),e5.get(),852,e2.get(),e1.get()))
            cur.commit()
            #cur.execute('select ticket,seat from runs,booking where bus_id= ')
            tab2()
        



        button8 = Button(f6,text="Book Seat", font=("Arial",15), activebackground = 'light green', bg = 'SpringGreen3',command =booked ).grid(row=1,column=10,padx=20,pady=20)
        


    def show_bus(f5):
        data=cur.execute('select b.bus_id,o.name,b.type,t.seat,b.fare from route r,route s,runs t,bus b,operator o where o.op_id=b.op_id and r.route_id=s.route_id and t.bus_id=b.bus_id and b.route_id=r.route_id and t.journey_date= "'+str(e3.get())+'" and r.station="'+str(e1.get())+'" and s.station="'+str(e2.get())+'" and r.s_id>s.s_id')
        #print(data.fetchall())
        f6=Frame(f5)
        f6.grid(row = 5, column = 0, columnspan = 10,pady = 20)
        Label(f6,text = "Select BUS ", font=("Arial",15),fg='light green').grid(row=0,column=0,padx = 20)
        Label(f6,text = "Operator ", font=("Arial",15),fg='light green').grid(row=0,column=1,padx=20)
        Label(f6,text = "Bus Type ", font=("Arial",15),fg='light green').grid(row=0,column=2,padx= 20)
        Label(f6,text = "Availability ", font=("Arial",15),fg='light green').grid(row=0,column=3,padx = 10+10)
        Label(f6,text = "Fare ", font=("Arial",15),fg='light green').grid(row=0,column=4, padx = 19+1)
        i,busch=1,IntVar()
        for row in data:
            rb=Radiobutton(f6,text='Bus'+str(i),variable=busch,value=row[0])
            rb.grid(row=i,column=0)
            Label(f6,text = str(row[1]),fg = 'green').grid(row = i, column = 1)
            Label(f6,text = str(row[2]),fg = 'green').grid(row = i, column = 2)
            Label(f6,text = str(row[3]),fg = 'green').grid(row = i, column = 3)
            Label(f6,text = str(row[4]),fg = 'green').grid(row = i, column = 4)
            i+=1
        
        button7 = Button(f6,text="Proceed to Book", font=("Arial",15), activebackground = 'light green', bg = 'SpringGreen3',command = lambda : proceed_to(f5,busch)).grid(row=1,column=5,padx=20,pady=20)
            
    button5 = Button(f5,text="Show Bus", font=("Arial",15), activebackground = 'light green', bg = 'SpringGreen3',command = lambda : show_bus(f5)).grid(row=0,column= 6,padx=20)

    button6 = Button(f5,image=home_img,command = tab2).grid(row=0,column= 7,padx=20)
    
    
def check_booked_seat(f2):
    f7=Frame(f2)
    f7.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f7,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f7,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'Royal Blue1', fg = 'red',anchor=CENTER ).grid(row=1,column=0,columnspan=5)
    Label(f7,text = "Check Your Booking", font=("Arial",25), bg = 'light green', fg = 'forest green' ).grid(row=2,column=0,columnspan=10,pady=20)

    f8=Frame(f7)
    f8.grid(row=3,column=0,pady=20,columnspan=5)
    Label(f8,text = "Enter Your Mobile No.", font=("Arial",15)).grid(row=0,column=0)
    e8 = Entry(f8)
    e8.grid(row=0,column=1,padx=20)
    def checkHistory():
        if(len(e8.get())!=10):
            showerror("Value Missing","Enter correct Mobile Number!!")
        elif e8.get()=="":
            showerror("Error","Value missing!!!")
        else:
            data=cur.execute('select Name,Ticket,age,ref_id,journey_date,sex,Mobile,bus_id,fromst from booking where Mobile='+str(e8.get()))
            con.commit()
            details=data.fetchall()
            final = Frame(f8,relief='groove',bd=5)
            final.grid(row = 4, column =1,pady=30)
            passenger_text = Label(final, text = "Passenger: ")
            passenger_text.grid(row =1, column=0)
            passenger_text1 = Label(final, text = details[0][0])
            passenger_text1.grid(row =1, column=1)

            #passengerseat
            seats_text = Label(final, text = "No of seats: ")
            seats_text.grid(row =2, column=0)
            seats_text1 = Label(final, text = details[0][1])
            seats_text1.grid(row =2, column=1)

            #Age
            age_text = Label(final, text = "Age: ")
            age_text.grid(row =3, column=0)
            age_text1 = Label(final, text = details[0][2])
            age_text1.grid(row =3, column=1)

            #booking_Ref
            bookingref=Label(final, text = "Booking Ref: ")
            bookingref.grid(row =4, column=0)
            bookingref1=Label(final, text = details[0][3])
            bookingref1.grid(row =4, column=1)

            #Travel_date
            bookingref2=Label(final, text = "Travel Date: ")
            bookingref2.grid(row =5, column=0)
            bookingref3=Label(final, text = details[0][4])
            bookingref3.grid(row =5, column=1)

            #gender
            g_text = Label(final, text = "Gender: ")
            g_text.grid(row =6, column=0)
            g_text1 = Label(final, text = details[0][10])
            g_text1.grid(row =6, column=1)

            #Mobile Number
            phone_text = Label(final, text = "Phone: ")
            phone_text.grid(row =7, column=0)
            phone_text1 = Label(final, text = details[0][5])
            phone_text1.grid(row =7, column=1)

            # #Price
            # flare_text = Label(final, text = "Fare Rs: ")
            # flare_text.grid(row =8, column=2)
            # flare_text1 = Label(final, text =details[0][6])
            # flare_text1.grid(row =8, column=3)

            #Bus
            detail_text = Label(final, text = "Bus Detail: ")
            detail_text.grid(row =8, column=0)
            detail_text1 = Label(final, text = details[0][7])
            detail_text1.grid(row =8, column=1)

            # #Booked on
            # booked_text = Label(final, text = "Booked On: ")
            # booked_text.grid(row =10, column=2)
            # booked_text1 = Label(final, text = details[0][8])
            # booked_text1.grid(row =10, column=3)

            #Boarding
            point_text = Label(final, text = "Boarding Point: ")
            point_text.grid(row =9, column=0)
            point_text1 = Label(final, text = details[0][9])
            point_text1.grid(row =9, column=1)

            price=details[0][6]*details[0][1]
            last_text = Label(final, text = "Total amount Rs"+str(price)+" to be paid at the time of boarding the bus",font="Arial 8 italic")
            last_text.grid(row =10, column=1)


    button8 = Button(f8,text="Check Booking", font=("Arial",15),command = checkHistory).grid(row=0,column=2,padx=20)

    button9 = Button(f7,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)

def add_bus():
    f9=Frame()
    f9.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f9,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f9,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'Royal Blue1', fg = 'red',anchor=CENTER ).grid(row=1,column=0,columnspan=5)
    Label(f9,text = "Add New Details to Database", font=("Arial",25), bd=5, fg = 'light green',bg='green' ).grid(row=2,column=0,columnspan=10,pady=20)

    f10=Frame(f9)
    f10.grid(row=3,column=0,pady=20,columnspan=10)
    button10 = Button(f10,text="New Operator", font=("Arial",15),bg='light green',command = new_operator).grid(row=0,column=0,padx=20)
    button11 = Button(f10,text = "New Bus",font=("Arial",15),bg='orange',anchor=CENTER,command = new_bus).grid(row=0,column=1,padx=20)
    button12 = Button(f10,text = "New Route",font=("Arial",15),bg='SlateBlue1',anchor=CENTER,command = new_route).grid(row=0,column=2,padx=20)
    button13 = Button(f10,text = "New Run",font=("Arial",15),bg='sienna3',anchor=CENTER,command = new_run).grid(row=0,column=3,padx=20)

    button23 = Button(f9,text = "HOME",anchor=CENTER,command = tab2).grid(row=4,column=0,columnspan=5)
    
def tab2():
    f2 = Frame()
    f2.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f2,image = my_img,anchor=CENTER,width=width).grid(row=0,column=0,columnspan=5)
    Label(f2,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'Royal Blue1', fg = 'red',anchor=CENTER ).grid(row=1,column=0,columnspan=5)
    f3 =Frame(f2,pady=20)
    f3.grid(row = 2,column=0,columnspan=5)
    
    button2 = Button(f3,text="SEAT BOOKING",font=("Arial",15),bg='light green',padx=10,pady=10,command=seat_book).grid(row=1,column=0)
    Label(f3,text="    ").grid(row=0,column=1)
    button2 = Button(f3,text="CHECK BOOKED SEAT",font=("Arial",15),bg='light green',padx=10,pady=10,command=lambda:check_booked_seat(f2)).grid(row=1,column=2)
    Label(f3,text="    ").grid(row=0,column=3)
    button3 = Button(f3,text="ADD BUS DETAILS",font=("Arial",15),bg='light green',padx=10,pady=10,command=add_bus).grid(row=1,column=4)
    Label(f3,text="For Admins Only",fg='red').grid(row=2,column=4)
    button4 = Button(f2,text = "HOME",anchor=CENTER,command = tab2).grid(row=3,column=0,columnspan=5)
    


def tab1():
    f1 = Frame()
    f1.place(x=0,y=0,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
    my_label = Label(f1,image = my_img, anchor = CENTER).pack()
    Label(f1,text = "ONLINE BUS BOOKING SYSTEM", font=("Arial",25), bg = 'Royal Blue1', fg = 'red' ).pack()
    Label(f1,text = "Name:Himanshi Sharma", font=("Arial",15),fg='blue',anchor = S,pady=50).pack()
    Label(f1,text = "Enrollment No.:211B134", font=("Arial",14),fg='blue',anchor = S).pack()
    Label(f1,text = "Mobile: 6265469932", font=("Arial",14),fg='blue',anchor = S, pady=50).pack()
    Label(f1,text = "Submitted to :Dr. Mahesh Kumar", font=("Arial",20), bg = 'Royal Blue1', fg = 'red' , pady = 10).pack()
    Label(f1,text="Project Based learning",font="Arial 16 bold",fg='red').pack()

    button1 = Button(f1,text = "Start",command = tab2).pack()
#-------------------------------------------------------------------------------------------------------------

my_img = PhotoImage(file=".\\Bus_for_project.png")
home_img =PhotoImage(file=".\\home.png")
tab1()
root.mainloop()
