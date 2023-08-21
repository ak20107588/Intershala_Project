from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import*
from django.contrib import messages
from django.http import JsonResponse



# Create your views here.

def dashboard(request):
    if request.session.has_key('is_logged'):
        return render(request,'dashboard.html')
    messages.warning(request,'Please Login!')
    return redirect('/')


def doctor(request):
    if request.session.has_key('is_logged'):
        return render(request,'doctor.html')
    messages.warning(request,'Please Login!')
    return redirect('/')

def messages1(request):
    return render(request,'messages.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def signup(request):
    data=User.objects.all()
    return render(request,'login.html')

def login(request):
    return render(request,'login.html')

def navbar(request):
    if request.session.has_key('is_logged'):
        data=User.objects.all()
        return render(request,'navbar.html',{'Result':data})
    messages.warning(request,'Please Login!')
    return redirect('/')


def blog(request):
    if request.session.has_key('is_logged'):
        return render(request,'blog.html')
    messages.warning(request,'Please Login!')
    return redirect('/')

def nodata(request):
    if request.session.has_key('is_logged'):
        return render(request,'nodata.html')
    messages.warning(request,'Please Login!')
    return redirect('/')

def blogdata(request):
    if request.session.has_key('is_logged'):
        data=Blog.objects.all()
        return render(request,'blog.html')
    messages.warning(request,'Please Login!')
    return redirect('/')
    

def blogdetail(request,id):
    if request.session.has_key('is_logged'):
        data=Blog.objects.filter(id=id)
        return render(request,'blogdetail.html',{'Data':data})
    messages.warning(request,'Please Login!')
    return redirect('/')
    

def allblogs(request):
    if request.session.has_key('is_logged'):

        data=Blog.objects.filter(IsDraft=False)

        return render(request,'allblogs.html',{'Data':data})
        # if Blog.objects.all(IsDraft='No'):
        #     return render(request,'allblogs.html',{'Data':data})
        # else:
        #     return render(request,'nodata.html')

        # if data is None :
        #     return render(request,'nodata.html')
            
        # else:
        #     return render(request,'allblogs.html',{'Data':data})
    messages.warning(request,'Please Login!')
    return redirect('/')



def draftblog(request):
    if request.session.has_key('is_logged'):
        
        data=Blog.objects.filter(IsDraft=True)
        return render(request,'draftblog.html',{'Data':data})
    
    messages.warning(request,'Please Login!')
    return redirect('/')


def patientdetail(request):
    if request.session.has_key('is_logged'):
        data=User.objects.filter(UserType='Patient')
        return render(request,'patientdetail.html',{'Result':data})
    messages.warning(request,'Please Login!')
    return redirect('/')   
    

def base(request):
    return render(request,'base.html')

def signup_detail(request):
    FirstName=(request.POST['firstname'])
    LastName=(request.POST['lastname'])
    ProfilePicture=(request.FILES['profilepicture'])
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

        if User.objects.filter(Email=lower_email).exists():

            messages.error(request,'Email Already Exist!')
            return redirect('/')
        
        if User.objects.filter(UserName=UserName).exists():
            messages.error(request,'Username Already Exist!')
            return redirect('/')
        
        
        else:
            
            a.save()
            request.session['is_logged']=True



            request.session['FirstName']=a.FirstName
            request.session['LastName']=a.LastName
            request.session['ProfilePicture']=a.ProfilePicture
            request.session['UserName']=a.UserName
            request.session['Email']=a.Email
            request.session['Address']=a.Address
            request.session['UserType']=a.UserType
            request.session['Password']=a.Password




            if a.UserType=='Doctor':
                user_type=a.UserType=='Doctor'
                request.session['user_type']=user_type
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

                user_type=context.UserType=='Doctor'
                print("user_type:",user_type)
                request.session['FirstName']=context.FirstName
                request.session['LastName']=context.LastName
                request.session['ProfilePicture']=context.ProfilePicture
                request.session['UserName']=context.UserName
                request.session['Email']=context.Email
                request.session['Address']=context.Address
                request.session['UserType']=context.UserType
                request.session['Password']=context.Password
                request.session['user_type']=user_type

                
                


                if context.UserType=='Doctor':
                    request.session['is_logged']=True
                    
                    return render(request,'doctor.html',{'Result':context})
                else:
                    print("new:",Password)                   
                    request.session['is_logged']=True
                    return render(request,'dashboard.html',{'Result':context})
                
            else:
                messages.error(request,'Invalid Password !')
                return redirect('/')
            
    except:

        messages.error(request,'Invalid Email !')
        return redirect('/')
    

def NewBlog(request):
    if request.session.has_key('is_logged'):
        Title=(request.POST['title'])
        BlogImages=(request.FILES['blogimg'])
        Category=(request.POST['category'])
        Summary=(request.POST['summary'])
        Content=(request.POST['content'])
        IsDraft=(request.POST['isdraft'])


        data={
            "Title":Title,
            "BlogImages":BlogImages,
            "Category":Category,
            "Summary":Summary,
            "Content":Content,
            "IsDraft":IsDraft
        }

        a=Blog(Title=Title,BlogImages=BlogImages,Category=Category,Summary=Summary,Content=Content,IsDraft=IsDraft)
        a.save()

        

        request.session['Title']=a.Title
        request.session['BlogImages']=a.BlogImages
        request.session['Category']=a.Category
        request.session['Summary']=a.Summary
        request.session['Content']=a.Content
        # request.session['is_draft']=a.IsDraft=='No'
        # request.session['is_draft1']=a.IsDraft=='Yes'

        # 


        return render(request,'doctor.html')
    messages.warning(request,"Please Login!")
    return redirect('/')




def post_list(request):
    categories = Blog.objects.all()
    selected_category_id = request.GET.get('category')
    

    if selected_category_id:
        posts = categories.filter(Category=selected_category_id)

    context = {
        'categories': categories,
        'selected_category_id': int(selected_category_id) if selected_category_id else None,
        'posts': posts,
    }

    return render(request, 'allblogs.html', context)


def blogcategory(request,category):
    data=Blog.objects.filter(Category=category)
    return render(request,'allblogs.html')


def get_items(request):
    if request.is_ajax() and request.method == "GET":
        category = request.GET.get['category']
        items = Blog.objects.filter(Category=category)
        return render(request,'allblogs.html')
    #     item_list_html = ""
        
    #     for item in items:
    #         item_list_html += f"<li>{item.name}</li>"
        
    #     return JsonResponse({'items': item_list_html})
    
    # return JsonResponse({'error': 'Invalid request'}, status=400)

def filter_items(request):
    category = request.GET.get('category')
    
    if category:
        items = Blog.objects.filter(Category=category).filter(IsDraft=False)
    else:
        items = Blog.objects.filter(IsDraft=False)
    
    return render(request, 'allblogs.html', {'Data': items})

        


