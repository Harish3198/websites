from django.shortcuts import render
import mysql.connector as sql
fname=''
lname=''
email=''
pwd=''
# Create your views here.
def home(request):
    return render(request, "index.html")


def signupaction(request):
    global fname,lname,email,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root", passwd="Harish@123", database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fname=value
            if key=="last_name":
                lname=value
            if key=="email":
                email=value
            if key=="password":
                pwd=value

        c="insert into users Values('{}','{}','{}','{}')".format(fname,lname,email,pwd)
        cursor.execute(c)
        m.commit()
        return render(request,'welcome.html')
    return render(request,'signup_page.html')