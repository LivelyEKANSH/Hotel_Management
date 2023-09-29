#A HOTEL MANAGEMENT PROJECT

def showallrecords():
    import pymysql
    d1=pymysql.connect(host="localhost",user="root",passwd="tiger",database="PROJECT")
    c1=d1.cursor()
    quer="select * from guest;"
    c1.execute(quer)
    record=c1.fetchall()
    for i in record:
        print(i)


        
    
def addrecords():
    import pymysql
    
    d1=pymysql.connect(host="localhost",user="root",passwd="tiger",database="PROJECT")
    c1=d1.cursor()
    ans1="yes"
    while ans1=="yes":
        for i in range(1,201):
            x=i
            quer3="select * from guest where guestid=%d"%x
            rowcount=c1.execute(quer3)
            if rowcount==0:
                ans1="no"
                break
    y=input("Enter the guest name:")
    v=input("enter the type of room:(single/double/triple) ")
    r=int(input("enter the no. of days:"))
    ci=input("enter the check in date:(YY-MM-DD)")
    co=input("entr the check out date:")            
    ans3="yes"
    while ans3=="yes":
        a=input("Enter the source of booking:(online/offline)")
        if a=="offline":
            ans3="no"
        elif a=="online":
            ans3="no"
        else:
            print("invaild input")
    ans2="ye"
    
    if v=="single":
        while ans2=="ye":
            for i in range(1,51):  
                c=i
                quer2="select * from guest where room_no=%d" %c
                c1.execute(quer2)
                if c1.rowcount==0:
                    ans2="no"
                    break
    elif v=="double":
        while ans2=="ye":
            for i in range(51,101):  
                c=i
                quer2="select * from guest where room_no=%d" %c
                c1.execute(quer2)
                if c1.rowcount==0:
                    ans2="no"
                    break
    elif v=="triple":
        while ans2=="ye":
            for i in range(101,151):  
                c=i
                quer2="select * from guest where room_no=%d" %c
                c1.execute(quer2)
                if c1.rowcount==0:
                    ans2="no"
                    break
    if v=="single":
        b=(2000+2000*r)*9/50
        
    elif v=="double":
        b=(4000+4000*r)*9/50
        
    elif v=="triple":
        b=(6000+6000*r)*9/50
    quer="Insert into guest values(%d,'%s','%s',%d,'%s','%s','%d','%s',%d);" %(x,y,v,r,ci,co,c,a,b)
    c1.execute(quer)
    d1.commit()
    print("Record Added")
    ch=input('wanna see rec?(y/n)')
    if ch=="y":
        quer2="SELECT* FROM guest where guestid=%d"%x
        c1.execute(quer2)
        rec=c1.fetchone()
        x,y,v,r,ci,co,c,a,b=rec
        print("guest id=%d"%x,"guest name= %s"%y,"type(room)= %s"%v,"number of days= %d"%r,"Check in Date= %s"%ci,"check Out Date=%s"%co,"Room number=%d"%c,"source of booking=%s"%a,"net pay=%d"%b,sep="\n")
    else:
        exit
        
    print("Thank You")


    
        
def search():
    import pymysql
   
    d1=pymysql.connect(user="root",host="localhost",passwd="tiger",database="PROJECT")
    c1=d1.cursor() 
    print("1. Id \n2. Name \n3. Source of booking \n4. Room no. \n5. date \n6. Type of room")
    cho=int(input("enter the no."))
    
    if cho==1:

        x=int(input("enter the id:"))
        quer="select * from guest where guestid='%d';" %x
        
        
    elif cho==2:
   
        x=input("enter the name:")
        quer="select * from guest where nameofguest='%s';" %x
        
        
    elif cho==3:

        x=input("enter the source of booking:")
        quer="select * from guest where sourceof_booking='%s';" %x
        
        
    elif cho==4:

        x=int(input("enter the room no:"))
        quer="select * from guest where room_no='%d';" %x
        
        
    elif cho==5:

        x=input("enter the date:")
        quer="select * from guest where cidate='%s';" %x
        
        
    elif cho==6:

        x=input("enter the type of room:")
        quer="select * from guest where typeofroom='%s'" %x
    c1.execute(quer)
    rec=c1.fetchone()
    print(rec)


    
    
def delete():
    import pymysql
    d1=pymysql.connect(host="localhost",user="root",passwd="tiger",database="PROJECT")
    c1=d1.cursor()
    x=int(input("enter the id:"))
    quer="delete from guest where guestid=%d;" %x
    rowcount=c1.execute(quer)
    if rowcount>0:
        d1.commit()
        print("Record Deleted")
    else:
        print("NO RECORD FOUND")

        
        
def changerecord():
    import pymysql
    d1=pymysql.connect(user="root",host="localhost",passwd="tiger",database="project")
    c1=d1.cursor()
    x=int(input("enter the id:"))
    query="select * from guest where guestid=%d" %x
    c1.execute(query)
    if c1.rowcount>0:
        row=list(c1.fetchone())
        for i in row:
            if i==x:
                guid=i
                print(row)
        print("\n1. name of guest \n2. source of booking \n3. date \n4. type of room")
        x=int(input("enter the no:"))
        if x==1:
            y=input("enter the new name of guest:")
            quer="update guest set nameofguest='%s' where guestid=%d" %(y,guid)
            c1.execute(quer)
            d1.commit()
            print("RECORD CHANGED")    
        elif x==2:
            y=input("enter the new source guest:")
            quer="update guest set sourceof_booking='%s' where guestid=%d" %(y,guid)
            c1.execute(quer)
            d1.commit()
            print("RECORD CHANGED")     
        elif x==3:
            y=input("enter the new date:")
            quer="update guest set cidate='%s' where guestid=%d" %(y,guid)
            c1.execute(quer)
            d1.commit()
            print("RECORD CHANGED")
        elif x==4:
            y=input("enter the new type of room:")
            quer="update guest set typeof_room='%s' where guestid=%d" %(y,guid)
            c1.execute(quer)
            d1.commit()
            quer4="select nofdays from guest where guestid=%d" %(guid)
            c1.execute(quer4)
            r=list(c1.fetchone())
            ans2="ye"
            if y=="single":
                while ans2=="ye":
                    for i in range(1,51):  
                        c=i
                        quer2="select * from guest where room_no=%d" %c
                        c1.execute(quer2)
                        if c1.rowcount==0:
                            ans2="no"
                            break
            elif y=="double":
                while ans2=="ye":
                    for i in range(51,101):  
                        c=i
                        quer2="select * from guest where room_no=%d" %c
                        c1.execute(quer2)
                        if c1.rowcount==0:
                            ans2="no"
                            break
            elif y=="triple":
                while ans2=="ye":
                    for i in range(101,151):  
                        c=i
                        quer2="select * from guest where room_no=%d" %c
                        c1.execute(quer2)
                        if c1.rowcount==0:
                            ans2="no"
                            break
            elif y=="quad":
                while ans2=="ye":
                    for i in range(151,201):  
                        c=i
                        quer2="select * from guest where room_no=%d" %c
                        c1.execute(quer2)
                        if c1.rowcount==0:
                            ans2="no"
                            break
            quer1="update guest set room_no='%d' where guestid=%d" %(c,guid)
            c1.execute(quer1)
            d1.commit()
            if y=="single":
                b=2000*r[0]*9/50
            elif y=="double":
                b=4000*r[0]*9/50
            elif y=="triple":
                b=6000*r[0]*9/50
            elif y=="quad":
                b=8000*r[0]*9/50
            quer2="update guest set netpay=%d where guestid=%d" %(b,guid)
            c1.execute(quer2)
            d1.commit()
            print("RECORD CHANGED")
        elif cr!=[1,2,3,4,5,6,7]:
            print("INVAILD INPUT")
    elif c1.rowcount==0:
        print("NO RECORD FOUND TO CHANGE")



        
def staff():
    
    print("\n1. all the records of staff \n2. add records of staff\n3. search records of staff \n4. delete records of staff \n5. update the records")  
    x=int(input("Enter the choice of no."))
    if x==1:
        allrecords()
    elif x==2:
        addrecordss()
    elif x==3:
        searchrec()
    elif x==4:
        deleterec()
    elif x==5:
        changerec()
    elif x not in [1,2,3,4,5]:
        print("\t\tINVAILD INPUT")

        
        
def addrecordss():
    import pymysql
    d1=pymysql.connect(host="localhost",user="root",passwd="tiger",database="PROJECT")
    c1=d1.cursor()
    print("\n1. Support staff \n2. food and beverages \n3. administration")
    print("")
    ans1="yes"
    while ans1=="yes":
        for i in range(1,201):
            x=i
            quer2="select * from staff where staffid=%d"%x
            rowcount=c1.execute(quer2)
            if rowcount==0:
                ans1="no"
                break
    y=input("Enter the name:")
    a=input("Enter the department:")
    if a=="Support staff":
        j=10000
    elif a=="food and beverages":
        j=30000
    elif a=="administration":
        j=50000
    z=input("Enter the hiredate:")
    quer="Insert into staff values(%d,'%s','%s',%d,'%s');" %(x,y,a,j,z)
    c1.execute(quer)
    d1.commit()
    print("Record Added")
    f=input("Want to see the added record:")
    if f=="y":
        quer="select * from staff where staffid=%d;"%x
        c1.execute(quer)
        rec=c1.fetchone()
        sid,sname,dept,sal,Hdate=rec
        print("staff id= %d"%sid,"staff name= %s"%sname,"depatment= %s"%dept,"salary= %d"%sal,"hireDate= %s"%Hdate,sep="\n")
    else:
        print("THANK YOU")



        
def deleterec():
    import pymysql
    d1=pymysql.connect(host="localhost",user="root",passwd="tiger",database="PROJECT")
    c1=d1.cursor()
    x=int(input("enter the id:"))
    quer="delete from staff where id=%d;" %x
    rowcount=c1.execute(quer)
    if rowcount>0:
        d1.commit()
        print("Record Deleted")
    else:
        print("NO RECORD FOUND")



        
def searchrec():
    import pymysql
  
    d1=pymysql.connect(host="localhost",user="root",passwd="tiger",database="PROJECT")
    c1=d1.cursor()
    print("\n1. id \n2. name \n3. dept \n4. hiredate")
    x=int(input("enter the no."))
    if x==1:
        
        l=int(input("enter the id:"))
        quer="select * from staff where id='%d';" %l

    elif x==2:
        
        l=input("enter the name:")
        quer="select * from staff where name='%s';" %l
        
    elif x==3:
        
        l=input("enter the dept:")
        quer="select * from staff where dept='%s';" %l
        
    elif x==4:
        
        l=input("enter the hire date:")
        quer="select * from staff where hiredate='%s';" %l
        
        
    elif x not in [1,2,3,4]:
        print("invaild input")
    c1.execute(quer)
    record=c1.fetchone()
    print(record)
            

            
def changerec():
    import pymysql
  
    d1=pymysql.connect(user="root",host="localhost",passwd="tiger",database="PROJECT")
    c1=d1.cursor()
    x=int(input("enter the id:"))
    quer="select * from staff where staffid=%d" %x
    c1.execute(quer)
    if c1.rowcount>0:
        print("1. id \n2. name \n3. department \n4. hire date")
        cr=int(input("enter the no:"))
        if cr==1:
            ans1="yes"
            while ans1=="yes":
                y=int(input("enter the id:"))
                quer1="select * from staff where staffid=%d" %y
                c1.execute(quer1)
                if c1.rowcount>0:
                    print("DUPLICATE INPUT")
                elif c1.rowcount==0:
                    ans1="no"
            quer="update staff set staffid=%d where staffid=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            print("RECORD UPDATED")
        elif cr==2:
            y=input("enter the name:")
            quer="update staff set name='%s' where staffid=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            print("RECORD UPDATED")    
        elif cr==3:
            y=input("enter the deparment:")
            quer="update staff set dept='%s' where staffid=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            if y=="support staff":
                j=2000
            elif y=="food and beverages":
                j=4000
            elif y=="administration":
                j=6000
            quer1="update staff set salary='%d' where staffid=%d" %(j,x)
            c1.execute(quer1)
            d1.commit()
            print("RECORD UPDATED")     
        elif cr==4:
            y=input("enter the hiredate:")
            quer="update staff set hiredate='%s' where staffid=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            print("RECORD UPDATED")
    elif c1.rowcount==0:
        print("invalid input")



        
def allrecords():
    import pymysql
  
    d1=pymysql.connect(host="localhost",user="root",password="tiger",database="PROJECT")
    c=d1.cursor()
    quer="SELECT * FROM staff;"
    c.execute(quer)
    record=c.fetchall()
    for k in record:
        print(k)
ans="y"

def guest():
    print("\n1. all records of guest \n2. add records of guest \n3. search records \n4. delete records of guest \n5. update the records")  
    x=int(input("Enter Your Choice : "))
    if x==1:
        showallrecords()
    elif x==2:
        addrecords()
    elif x==3:
        search()
    elif x==4:
        delete()
    elif x==5:
        changerecord()
    elif x not in [0,1,2,3,4,5]:
        print("\t\tINVAILD INPUT")
        
while ans=="y":
    print("*     *  * * *  *        *        * * * *  ")
    print("*     *  *      *        *        *     *  ")
    print("* * * *  * * *  *        *        *     *  ")
    print("*     *  *      *        *        *     *  ")
    print("*     *  * * *  * * * *  * * * *  * * * *  ")
    print("1.Guest records \n2.Staff records \n3.Exit")
    x=int(input("enter the no:"))
    if x==1:
        guest()
    elif x==2:
        staff()
    elif x==3:
        quit()
    elif x!=[1,2,3]:
        print("\t\tINVAILD INPUT")
    ans=input("want to continue:")


