from django.shortcuts import render,redirect
from .models import *
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

#login_required

# Create your views here.
class ProductDetail(DetailView):
    model = Products
    template_name = 'product.html'
    context_object_name = 'product'


@login_required(login_url = '/main/auth-login/')
def Index(request):
    context = {
        'category':Category.objects.all(),
        'product':Products.objects.all().filter(category__id = 2)
    }
    return render(request, 'index.html', context)



def Blank(request):
    context = {
        'category':Category.objects.all(),
        'product':Products.objects.all()
    }
    return render(request, 'blank.html', context)


def Store(request):
    context = {
        'category':Category.objects.all(),
        'product':Products.objects.all().filter(category__id = 1),
        'product_1':Products.objects.all().filter(category__id = 2),
        'product_2':Products.objects.all().filter(category__id = 3),
        'product_3':Products.objects.all().filter(category__id = 4),
    }
    return render(request, 'store.html', context)



def AddProduct(request):

    if request.method == 'POST':
        discount = request.POST['discount']
        # is_new = request.POST['is_new']
        image = request.POST['image']
        category = request.POST['category']
        name = request.POST['name']
        price = request.POST['price']
        new_price = request.POST['new_price']
        text = request.POST['text']
        Products.objects.create(discount=discount,image=image,category_id=category , name=name,price=price,new_price=new_price,text=text)

        return redirect('/main/addproduct/')

    context={
        'category':Category.objects.all()
    }



    return render(request,'addproduct.html',context)



def Sms(request):
    if request.method == 'POST':
        r = request.POST
        first_name=r['first_name']
        last_name = r['last_name']
        job = r['job']
        text = r['text']

        Contact.objects.create(first_name=first_name,last_name=last_name,job=job,text=text)
        return redirect('/main/contact/')

    return render(request,'contact.html')


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout


def Register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/main/index/')
    else:
        form = UserCreationForm()
    context={
        'form':form
    }
    return render(request,'registration/register.html',context)


def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        form = authenticate(request,username=username,password=password)
        if form is not None:
            login(request,form)
            return redirect('main/index/')
    return render(request,'registration/login.html')


def Logout(request):
    logout(request)
    return redirect('/main/index/')


def Req(request):
    return redirect('/main/index/')


def Requirem(request):
    return redirect('/main/index/')