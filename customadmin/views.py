from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages
from django.http import HttpResponseRedirect , HttpResponse

def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists ():
                messages.info(request,'Account not found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            user_obj = authenticate(username=username,password=password)
            if user_obj and user_obj.is_superuser:
                login(request,user_obj)
                return redirect('/dashboard/')
            messages.info(request,'Invalid Password')
            return redirect('/')
        return render(request,'login.html')
    except Exception as e :
        print(e)

def dashboard(request):
    return render(request,'index.html')