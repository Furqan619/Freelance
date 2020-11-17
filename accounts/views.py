from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages



# Create your views here.
# But before creating views here you have to include this app "urls.py" to project's "urls.py"

def login(request):
      if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate( username= username, password= password)

            if user is not None:
                  auth.login(request, user)
                  return redirect('/')
            else:
                  messages.info(request, 'invalid credentials')
                  return redirect('login')

      else:
            return render(request, 'login.html')
                  


def register(request):
      if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            # ("password = password1") 'password' is the name of the column in db & 'password1' is variable
            password2 = request.POST['password2']
            date_joined = request.POST['date_joined']

            if password1 == password2:
                  if User.objects.filter(username=username).exists():
                        # Here we are checking(filtering) that username already exists or not 
                        messages.info(request,'Username taken') 
                        return redirect('register')           

                  elif User.objects.filter(email = email).exists():
                        messages.info(request, 'Email id taken')
                        return redirect('register')
                         
                  else:
                        user = User.objects.create_user(first_name= first_name, last_name=last_name, username=username, email=email, password=password1,  date_joined=date_joined )
                        user.save()
                        messages.info(request, 'User created')
                        return redirect('login')
            else:
                  messages.info(request, 'Password Not Matching')      


            return redirect('register')

      
      else:
            return render (request, 'register.html',)


def logout(request):
      auth.logout(request)
      return redirect('/')

def takemeout(request):
      return render(request, 'index.html')
