from django.shortcuts import render,redirect
import mysql.connector as sql
urn=''
pwd=''
mb=''
na=''
add=''
em=''
# Create your views here.
def signupaction(request):
    global urn,pwd,mb,na,add,em
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Suyog@123",database='webAPI')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Username":
                urn=value
            if key=="Password":
                pwd=value
            if key=="mobile":
                mb=value
            if key=="Name":
                na=value
            if key=="Address":
                add=value
            if key=="Email":
                em=value
                    
        
        c="insert into users Values('{}','{}','{}','{}','{}','{}')".format(urn,pwd,mb,na,add,em)
        cursor.execute(c)
        m.commit()
        
        

    return render(request,'signup_page.html')


