from django.shortcuts import render
import mysql.connector as sql
urn=''
pwd=''
# Create your views here.
def loginaction(request):
    global unr,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Suyog@123",database='webAPI')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Username":
                urn=value
            if key=="password":
                pwd=value
        
        c="select * from users where Username='{}' and password='{}'".format(urn,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")

    return render(request,'login_page.html')



