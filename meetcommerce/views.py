from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import usersForm

def homePage(request):
    data = {
        'title': 'Home Page',
        'bdata': "Wellcome to Meet Commerce",
        'clist':['PHP','Java','Django'],
        'number': [2,5,10,20,30,60,80],
        'student_details':[
            {'name':'Hassan','phone': 9230444444},
            {'name':'test','phone': 9230444444}
        ]
    }
    return render(request, "index.html",data)

def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"services.html")
def projects(request):
    return render(request,"projects.html")
def greet(request, name):
    return HttpResponse(f"Hello!, {name})!")
def contacts(request):
    return render(request,"contacts.html")
from django.shortcuts import render



# def userForm(request):
#     # This is the implementation of get and Post Method
#     num1 = None
#     num2 = None
#     output = None

#     if request.method == "POST":
#         try:
#             num1 = int(request.POST.get('num1'))
#             num2 = int(request.POST.get('num2'))
#             output = num1 + num2
#         except (ValueError, TypeError):
#             output = "Invalid input"
#     else:
#         num1 = request.GET.get('num1', '')
#         num2 = request.GET.get('num2', '')


#     context = {
#         'num1': num1,
#         'num2': num2,
#         'output': output
#     }

#     return render(request, "userform.html", context)

def userForm(request):
    finaldata: int =0
    fn=usersForm()

    data={'form':fn}
    try:
        if request.method=="POST":
            n1: int =int(request.POST.get("num1"))
            n2 : int = int(request.POST.get("num2"))
            finaldata: int =n1+n2
            
            data = {
                'form': fn,
                'Output': finaldata
            }
            url="/about-us/?output={}".format(finaldata)

            return redirect(url)
    except:
        pass
    return render(request,"userform.html",data)

def submitForm(request):
    finalans: int = 0
    data1={}
    try:
        if request.method=="POST":
            num1: int = int(request.POST.get("num1"))
            num2: int = int(request.POST.get("num2"))
            finalans: int = num1 + num2
            data1={
                'n1': num1,
                'n2': num2,
                'Output': finalans
            }
        return HttpResponse(finalans)   
    except:
        pass

def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1  = eval(request.POST.get("num1"))
            n2  = eval(request.POST.get("num2"))
            opr  = request.POST.get("opr")
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
    
    except:
        c="Invalid Operation"
    
    print(c)
    return render(request, "calculator.html",{'output':c})    

def evenOdd(request):
    o=''
    n=None
    try:
        if request.method=="POST":
            n: int = int(request.POST.get('num1'))
            opr = request.POST.get('opr')
            if n%2==0:
                o = "Even Number"
            else:
                o = "Odd Number"
    except:
        o = print("Invalid Input")
    return render(request, "evenodd.html",{'output': o,'n1': n})

def markSheet(request):
    data = {}  # Initialize an empty context dictionary
    if request.method == "POST":
        try:
            m1 = int(request.POST.get("num1"))
            m2 = int(request.POST.get("num2"))
            m3 = int(request.POST.get("num3"))
            m4 = int(request.POST.get("num4"))
            t = m1 + m2 + m3 + m4
            per = t * 100 / 400
            if per >= 80:
                d = "First Division"
            elif per >= 65:
                d = "Second Division"
            elif per >= 45:
                d = "Third Division"
            elif per >= 33:
                d = "Fourth Division"
            else:
                d = "Fail"
            
            data = {
                'total': t,
                'percentage': per,
                'division': d,
                'm1': m1,
                'm2': m2,
                'm3': m3,
                'm4': m4
            }
        except:
            data = {
                'error': "Invalid input. Please enter valid marks."
            }
    return render(request, "marksheet.html", data)

def courseDetail(request,courseid):
    return HttpResponse(courseid)

# ********  Sessions ********
# def index(request):
    
#     if "tasks" not in request.session:
#         request.session["tasks"]=[]

#     return render(request, "task.html",{
#         "tasks": request.session["tasks"]
#     }) 