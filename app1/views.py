from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import*
from django.contrib import messages


# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')

def doctor(request):
    return render(request,'doctor.html')

def messages1(request):
    return render(request,'messages.html')

def logout(request):
    return redirect('/')

def signup(request):
    data=User.objects.all()
    return render(request,'login.html')

def login(request):
    return render(request,'login.html')

def signup_detail(request):
    FirstName=(request.POST['firstname'])
    LastName=(request.POST['lastname'])
    ProfilePicture=(request.POST['profilepicture'])
    UserName=(request.POST['username'])
    Email=(request.POST['email'])
    Address=(request.POST['address'])+","+(request.POST['city'])+","+(request.POST['state'])+","+(request.POST['pincode'])
    UserType=(request.POST['usertype'])
    Password=(request.POST['password'])
    ConfirmPassword=(request.POST['confirmpassword'])

    lower_email=Email.lower()

    print("Email value: ",Email)


    if Password==ConfirmPassword:

        data={
            "FirstName":FirstName,
            "LastName":LastName,
            "ProfilePicture":ProfilePicture,
            "UserName":UserName,
            "Email":lower_email,
            "Address":Address,
            "UserType":UserType,
            "Password":Password,
            "ConfirmPassword":ConfirmPassword,
        }

        a=User(FirstName=FirstName,LastName=LastName,ProfilePicture=ProfilePicture,UserName=UserName,Email=lower_email,Address=Address,UserType=UserType,Password=Password,ConfirmPassword=ConfirmPassword)

        if User.objects.filter(Email=lower_email,UserName=UserName).exists():

            messages.error(request,'Email Already Exist!')
            return render(request,'login.html')
        
        if User.objects.filter(UserName=UserName).exists():
            messages.error(request,'Username Already Exist!')
            return render(request,'login.html')
        
        
        else:
            a.save()

            if a.UserType=='Doctor':
                messages.success(request,'Signup Success.')
                return render(request,'doctor.html',{'Result':a})
            else:
                return render(request,'dashboard.html',{'Result':a})
    else:
        messages.error(request,'Password & Confirm Password Not Match!')
        return redirect('/')
    
   

def login_detail(request):
    Email=(request.POST['email'])
    Password=(request.POST['password'])
    lower_email=Email.lower()
    print("Email Login & Password:",Email,Password)
    print(Email)

    try:
        context=User.objects.get(Email=lower_email)

        if User.objects.get(Email=lower_email):
            print("New Email:",Email)
            if (Password==context.Password):
                print("password new:",Password)
                print("usertype:",context.UserType)
                if context.UserType=='Doctor':
                    return render(request,'doctor.html',{'Result':context})
                else:
                    print("new:",Password)                   
                    return render(request,'dashboard.html',{'Result':context})
                
            else:
                messages.error(request,'Invalid Password !')
                return render(request,'login.html')
            
    except:

        messages.error(request,'Invalid Email !')
        return render(request,'login.html')
