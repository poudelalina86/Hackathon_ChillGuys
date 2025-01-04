from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
from  .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# def index(request):
#     return render(request,'index.html')

#     def login_page(request):
#     return render(request,'log.html')

def signin(request):
    return render(request,'signup.html')

def signin_auth(request):
     if request.method == 'POST':
         username=request.POST.get('username')
         email=request.POST.get('email')
         password1=request.POST.get('password')
         password2=request.POST.get('confirm-password')
          
         if User.objects.filter(username=username):
             messages.error(request,"Username already exist!")
             return redirect('signin')
         
         if User.objects.filter(email=email):
             messages.error(request,"Email already register!")
             return redirect('signin')
         
         if len(username)>15:
            messages.error(request,"Username must be under 10 character!")
            return redirect('signin')
  
         if password1!=password2:
           messages.error(request,"Password donnot match!")
           return redirect('signin')
         
         if not username.isalnum():
           messages.error(request,"Username must be Alpha-Numeric!")
           return redirect('signin')    
         
         else:   
          my_user=User.objects.create_user(username,email,password1)
          my_user.username = username
          my_user.save()

          messages.success(request,"Your Account has been created successfully.")
          
          #Welcome Email

        #   subject = "Welcome to Harsha"
        #   message


          return redirect('loginpage')
     return redirect('signin')
     
def login_page(request):
     if request.method =='POST':
         username = request.POST.get('username')
         password1= request.POST.get('password')
         #check if user has correct credentials
         user = authenticate(request, username=username, password=password1)
         if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect('homepage')
         else:
             # No backend authenticated the credentials

             messages.error(request,"Your credentials are incorrect.Signin if you have not.")

             return render( request,'login.html')
     return render(request,'login.html')


@login_required(login_url='/loginpage')
def profile(request):
     if request.method == 'POST':
      u_form = UserUpdateForm(request.POST, instance=request.user)
      p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
      
      if u_form.is_valid() and p_form.is_valid():
         u_form.save()
         p_form.save()

         messages.success(request,f'Your account has been updated!')
         return redirect('profile')
     else:
       u_form = UserUpdateForm(instance=request.user)
       p_form = ProfileUpdateForm(instance=request.user.profile)
     
     context = {
         'u_form': u_form,
         'p_form': p_form
      }
     return render(request,'profile.html', context )

@login_required(login_url='/loginpage')
def detailpage(request):
    return render(request,'detail.html')



