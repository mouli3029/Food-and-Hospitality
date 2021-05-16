from django.shortcuts import render,redirect
from .forms import UserRegisterForm

from django.template import Context
from django.template.loader import get_template

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from django.core.mail import send_mail,EmailMultiAlternatives
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,'user/home.html',{'title':'index'})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # details for sending the mail
            html_email = get_template('user/email.html')
            ctx = {'username':username}
            subject = 'Welcome'
            from_email = 'moulichowdary82@gmail.com'
            to = email

            html_content = html_email.render(ctx)
            # Renders the context to the html_email Template
            # more deatails -- https://docs.djangoproject.com/en/3.2/ref/templates/api/#rendering-a-context

            msg = EmailMultiAlternatives(subject,html_content,from_email,[to])
            msg.attach_alternative(html_content,'text/html')
            msg.send()

            messages.success(request,f'Your account with %s has been created successFully'.format({ username }))
            return redirect('login')
    
    # If it is a get request
    else :
        # send the empty form so that user can register
        form = UserRegisterForm()
    return render(request,'user/register.html',{'form':form})

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        # If there is a user
        if user is not None:
            form = login(request,user)
            messages.success(request,f'Welcome {username} !!')
            return redirect('index')
        else : 
            messages.info(request,"No account is found ! Please register to access")
    form = AuthenticationForm()
    return render(request,'user/login.html',{'form':form})



        


