from django.shortcuts import render

from .models import Profile,Skill,Document



def Login(request):
    return render(request, 'Book/Login.html')

def Auth(request):
    Auth = Profile.objects.all()
    flag = 0
    for user in Auth:
        if(user.Email==request.POST.get("Email") and user.Password == request.POST.get("Password")):
            flag+=1


    if(flag>0):
        email = {'email':request.POST.get("Email")}
        return  render(request, 'Book/Home.html', email )
    else:
        return  render(request, 'Book/errorPage.html')





def SignUpPage(request):
        return render(request, 'Book/SignUp.html')





def SignUp(request):
    Auth = Profile.objects.all()
    flag = 0
    for user in Auth:
        if(user.Email==request.POST.get("Email")):
            flag += 1
            
    if(flag>0):
        return  render(request, 'Book/errorPage.html')        
    else:
            if(request.POST.get("Password")!= request.POST.get("ConfirmPassword")):
                return  render(request, 'Book/errorPage.html')
            else:
                profile = Profile(First_Name=request.POST.get("FirstName")
                ,Last_Name=request.POST.get("LastName")
                ,Email=request.POST.get("Email")
                ,Password=request.POST.get("Password")
                ,Date_Of_Birth=request.POST.get("DOB")
                ,PhoneNumber=request.POST.get("PhoneNumber"))
                profile.save()
                return  render(request, 'Book/Login.html')





       
       
    
