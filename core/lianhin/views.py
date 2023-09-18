from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from lianhin.basecontent import BaseContent

# Create your views here.


def sign_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/index')
        else:
            return redirect('/')
    
    return render(request,'sign_in.html')

def index(request):
    return render(request,'index.html')


def surfacefinish(request):
    data=Surfacefinish.objects.filter(is_active=True)
    context={'data':data}
    return render(request,'surfacefinish.html',context)
    
def surfacefinishform(request):
    if request.method == 'POST':
        name_f = request.POST['surface_name']
        icon_f = request.FILES['icon']
        Surfacefinish.objects.create(surface_name=name_f, icon=icon_f)
        return redirect('/surfacefinish')
    else:
        return render(request, 'surfacefinishform.html')
    
def Active_surfacefinish(request,id):
    data=Surfacefinish.objects.get(id=id)
    data.is_active=False
    data.save()
    return redirect('/surfacefinish')

def Deactive_surfacefinish(request,id):
    data=Surfacefinish.objects.get(id=id)
    data.is_active=True
    data.save()
    return redirect('/surfacefinish')  

def deletesurfacefinish(request,id):
    data=Surfacefinish.objects.get(id=id)
    data.delete()
    return redirect('/surfacefinish')

def updatesurfacefinish(request,id):
    data=Surfacefinish.objects.get(id=id)
    if request.method=='POST':
        name_f=request.POST['surface_name']
        icon_f=request.FILES.get('icon')

        if icon_f:
            data.icon=icon_f
        else:
            pass
        data.surface_name=name_f

        data.save()
        return redirect('/surfacefinish')
    context={'data':data}
    return render(request,'updatesurfacefinish.html',context)

def brand(request):
    data=Brand.objects.filter(is_active=True)
    context={'data':data}
    return render(request,'brand.html',context)
    
def brandform(request):
    if request.method == 'POST':
        name_f = request.POST['brand_name']
        brand_image_f = request.FILES['brand_image']
        Brand.objects.create(brand_name=name_f, brand_image=brand_image_f)
        return redirect('/brand')
    else:
        return render(request, 'brandform.html')
    
def Active_brand(request,id):
    data=Brand.objects.get(id=id)
    data.is_active=False
    data.save()
    return redirect('/brand')

def Deactive_brand(request,id):
    data=Brand.objects.get(id=id)
    data.is_active=True
    data.save()
    return redirect('/brand')  

def deletebrand(request,id):
    data=Brand.objects.get(id=id)
    data.delete()
    return redirect('/brand')

def updatebrand(request,id):
    data=Brand.objects.get(id=id)
    if request.method=='POST':
        name_f=request.POST['brand_name']
        brand_image_f=request.FILES.get('brand_image')

        if brand_image_f:
            data.brand_image=brand_image_f
        else:
            pass

        data.brand_name=name_f

        data.save()
        return redirect('/brand')
    context={'data':data}
    return render(request,'updatebrand.html',context)

def collection(request):
    collections = Collection.objects.filter(is_active=True)
    brands = Brand.objects.all()
    context = {'collections': collections, 'brands': brands}
    return render(request, 'collection.html', context)

def collectionform(request):
    brands = Brand.objects.all()

    if request.method == 'POST':
        collection_name_f = request.POST['collection_name']
        brand_id = request.POST['brand_name']

        try:
            brand_obj = Brand.objects.get(id=brand_id)
            Collection.objects.create(collection_name=collection_name_f, brand=brand_obj)
            return redirect('/collection')
        except Brand.DoesNotExist:
            return render(request, 'collectionform.html', {'brands': brands})

    return render(request, 'collectionform.html', {'brands': brands})


def Active_collection(request,id):
    data=Collection.objects.get(id=id)
    data.is_active=False
    data.save()
    return redirect("/collection")

def Deactive_collection(request,id):
    data=Collection.objects.get(id=id)
    data.is_active=True
    data.save()
    return redirect("/collection")

def deletecollection(request,id):
    data=Collection.objects.get(id=id)
    data.delete()
    return redirect('/collection')

def updatecollection(request,id):
    data=Collection.objects.get(id=id)
    brand=Brand.objects.all()
    if request.method=='POST':
        collection_name_f=request.POST['collection_name']

        data.collection_name=collection_name_f
        data.save()
        return redirect('/collection')
    context={'data':data,'brand':brand}
    return render(request,'updatecollection.html',context)

def series(request):
    series = Series.objects.filter(is_active=True)
    collection = Collection.objects.all()
    context = {'series': series, 'collection': collection}
    return render(request, 'series.html', context)

def seriesform(request):
    collections = Collection.objects.all()

    if request.method == 'POST':
        series_name_f = request.POST['series_name']
        collection_id = request.POST['collection_name']

        try:
            collection_obj = Collection.objects.get(id=collection_id)
            Series.objects.create(series_name=series_name_f, collection=collection_obj)
            return redirect('/series')
        except Collection.DoesNotExist:
            return render(request, 'seriesform.html', {'collections': collections})

    return render(request, 'seriesform.html', {'collections': collections})


def Active_series(request,id):
    data=Series.objects.get(id=id)
    data.is_active=False
    data.save()
    return redirect("/series")

def Deactive_series(request,id):
    data=Series.objects.get(id=id)
    data.is_active=True
    data.save()
    return redirect("/series")

def deleteseries(request,id):
    data=Series.objects.get(id=id)
    data.delete()
    return redirect('/series')

def updateseries(request,id):
    data=Series.objects.get(id=id)
    collection=Collection.objects.all()
    if request.method=='POST':
        series_name_f = request.POST['series_name']


        data.series_name=series_name_f
        data.save()
        return redirect('/series')
    context={'data':data,'collection':collection}
    return render(request,'updateseries.html',context)