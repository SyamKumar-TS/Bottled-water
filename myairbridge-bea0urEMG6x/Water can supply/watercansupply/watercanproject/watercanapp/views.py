from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from watercanapp.models import Orders, Contact, Usr_can_odr, Delivered_his, com_can_odr, stock
from .decorator import Admin_only
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
razorpay_client = razorpay.Client(
  auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        con = Contact(name=name, contact_number=contact_number, email=email)
        con.save()
        return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm_password')

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already Taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Id is already Exists...")
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('login_view')
        else:
            messages.info(request, "Both password is not matching")
            return redirect('register')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('first')
        else:
            messages.info(request, "Username or Password Is Wrong...")
            return redirect('login_view')
    return render(request, 'login_view.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

@Admin_only 
def first(request):
    inf = Orders.objects.filter(odr = request.user)
    can_odr = Usr_can_odr.objects.filter(usr_can = request.user)
    com_can = com_can_odr.objects.filter(no =request.user)
    com_del = Delivered_his.objects.filter(no =request.user)
    return render(request, 'first.html', {'inf':inf, 'can_odr':can_odr, 'com_can':com_can, 'com_del':com_del})

def cancel_odr(request, id):
    can_odr = Orders.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        adress = request.POST.get('adress')
        quantity = request.POST.get('quantity')
        amount = request.POST.get('amount')
        reason = request.POST.get('reason')
        can_his = Usr_can_odr(name=name, phone_no=phone_no, adress=adress,quantity=quantity,amount=amount, reason=reason, usr_can=request.user)
        can_his.save()
        can = Orders.objects.get(id=id)
        can.delete()
        return redirect('first')
    return render(request, 'cancel.html', {'can_odr':can_odr})

def update_odr(request, id):
    up_odr = Orders.objects.get(id=id)
    if request.method == 'POST':
        up_odr = Orders.objects.get(id=id)
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        quantity = request.POST.get('quantity')
        amount = request.POST.get('amount')

        
        up_odr.name = name
        up_odr.phone_number = phone_number
        up_odr.address = address
        up_odr.quantity = quantity
        up_odr.amount =amount
        up_odr.save()
        return redirect('first')

    return render(request, 'update.html', {'up_odr':up_odr})

def buy(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_no')
        address = request.POST.get('adress')
        quantity = request.POST.get('quantity')
        date = request.POST.get('date')
        amount = request.POST.get('amount')
        odr = Orders(name=name, phone_number=phone_number, address=address, quantity=quantity,date=date, amount=amount, odr = request.user)
        odr.save()
        return redirect('last')
    return render(request, 'buy.html')

def last(request):
    return render(request, 'last.html')

@csrf_exempt
def paymentsuccess(request):
    return render(request, 'paymentsuccess.html')

def payment(request,id):
    odr = Orders.objects.get(id=id)
    currency = 'INR'
    amt = odr.amount
    odr.payment_status = True
    odr.save()
    amount = amt * 100
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                        currency=currency,
                        payment_capture='0'))
    razorpay_order_id = razorpay_order["id"]
    callback_url = 'http://127.0.0.1:8000/paymentsuccess'
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url 
    context['slotid'] = "1"
    return render(request, "payment.html",context)

def company(request):
    det = Orders.objects.all()
    can_odr = Usr_can_odr.objects.all()
    delv_his = Delivered_his.objects.all()
    com_can = com_can_odr.objects.all()
    stk = stock.objects.get(id=1)
    stks = stk.total_stock
    return render(request, 'company.html', {'det':det, 'can_odr':can_odr, 'delv_his':delv_his, 'com_can':com_can,"stks":stks})

def delivered(request, id):
    deliv = Orders.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        quantity = request.POST.get('quantity')
        amount = request.POST.get('amount')
        no = request.POST.get('no')
        deliv_his = Delivered_his(name=name, phone_number=phone_number, address=address, quantity=quantity,amount=amount, no=no)
        deliv_his.save()
        deliv.delete()
        stk = stock.objects.get(id=1)
        stk.total_stock =  stk.total_stock-int(quantity)
        stk.save()
        return redirect('company')
    return render(request, 'delv.html', {'deliv':deliv})

def com_odr_can(request, id):
    odr_can = Orders.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        quantity = request.POST.get('quantity')
        amount = request.POST.get('amount')
        reason = request.POST.get('reason')
        no = request.POST.get('no')
        com_can_his = com_can_odr(name=name, phone_number=phone_number, address=address, quantity=quantity,amount=amount, reason=reason, no=no)
        com_can_his.save()
        odr_can.delete()
        return redirect('company')
    return render(request, 'com_odr_can.html', {'odr_can':odr_can})

def updatestock(request):
    stk = request.POST.get("stock")
    stockupdate = stock.objects.get(id=1)
    stockupdate.total_stock =  stockupdate.total_stock+int(stk)
    stockupdate.save()
    messages.info(request, "Stock updated successfuly...")
    return redirect("company")
    