from django.shortcuts import render,redirect
# for registration DB coding
from django.shortcuts import render, get_object_or_404
from django.http import *
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.utils import timezone
from datetime import datetime as dt
import datetime
from .models import *
from django.views.decorators.csrf import csrf_exempt
from Paytm.checksum import *
from Paytm import checksum
MERCHANT_KEY = 'SHvO1nVoMFgZN%N4'


#change password
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



#from django.contrib import message
#from django.core.exeption import objectDoesNotExits

#def Create your views here.
def index(request):
	return render(request,'index.html')

def had(request):
	return render(request,'had.html')

def contact(request):
	return render(request,'contact.html')

def profile(request):
    return render(request,'profile.html')

def change(request):
    return render(request,'change.html')

def business(request):
	return render(request,'business.html')

def feedback(request):
    if request.POST:
        msg=request.POST['msg']

        obj=feedbacks(msg=msg)
        obj.username=request.user
        obj.save()
        return HttpResponse('feedback sent Successfully')
    return render(request,'feedback.html')



def order(request):
    if request.method =='POST':
        sbox= request.POST['sbox']
        mbox= request.POST['mbox']
        lbox= request.POST['lbox']
        month= request.POST['month']
        amount= request.POST['amount']
        name= request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        pickup_location = request.POST['pickup_location']
        zipcode = request.POST['zipcode']
        date = request.POST['date1']
        hour = request.POST['hour']
        minutes=request.POST['minutes']
        print(sbox,mbox,lbox,month,name,email,phone,pickup_location,zipcode,date,hour,minutes)
        obj1=orders(sbox=sbox,mbox=mbox,
                    lbox=lbox,month=month,amount=amount,name=name,
                    email=email,phone=phone,pickup_location=pickup_location,
                    zipcode=zipcode,date=date,hour=hour,minutes=minutes)
        # obj1.username=request.user
        obj1.save()
        print(str(obj1.orders_id))
        param_dict = {

            'MID':'UYCMZU96802626250305',
            'ORDER_ID':str(obj1.orders_id),
            'TXN_AMOUNT':str(amount),
            'CUST_ID':email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)

        return render(request, 'paytm.html', {'param_dict': param_dict}) 
    return render(request,'pricing.html')

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i =='CHECKSUMHASH':
            checksum = form[i]

    #verify = checksum.verify_checksum(response_dict,MERCHANT_KEY,checksum)
    verify= verify_checksum(response_dict,MERCHANT_KEY,checksum)

    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')

        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request,'paymentstatus.html',{'response':response_dict})

                	

def pricing(request):
    box1 = box.objects.all()
    return render(request,'pricing.html',{'box1': box1})
def busy_price(request):
    pass
def student(request):
	return render(request,'student.html')

# for registration DB coding

def register(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('mail')
        password = request.POST.get('password')
        # phone = request.POST['phone']
        # address = request.POST['address']
        # usertype = request.POST['usertype']
        # gender = request.POST['gender']
        users= User.objects.all()
        for u in users:
            if u.username == email:
                return render(request,'registration.html')
                messages.error(request,"Username Already Exist.")

        user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=email,password=password)
        user.save()
        messages.success(request,"Register Successfully..")
        return redirect('login')
    else:
        return render(request,'registration.html')

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return render(request, 'login.html',{
                'error_message': "Invali Email Or Password!"
                })

    else:
        return render(request,'login.html')        



def logout(request):
    auth.logout(request)
    return redirect('/')

def registration(request):
    return render(request,'registration.html')

        
def meet(request):
    if request.POST:
        fname= request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']


        us=contactus(fname=fname, lname=lname, email=email,phone=phone,message=message)
        us.save()
        messages.error(request,"Message Send Successfully....")
        return redirect('contact')

    return render(request,'contact.html') 

def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('change_password')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'accounts/change_password.html', {
            'form': form
        })       

    