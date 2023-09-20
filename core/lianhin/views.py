from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from lianhin.basecontent import BaseContent
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages



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

def sign_out(request):
    auth.logout(request)
    return redirect('/')

def error_400_view(request, exception):
    return render(request, 'error_400.html', status=400)

def error_401_view(request, exception):
    return render(request, 'error_401.html', status=401)

def error_403_view(request, exception):
    return render(request, 'error_403.html', status=403)

def error_404_view(request, exception):
    return render(request, 'error_404.html', status=404)

def error_500_view(request):
    return render(request, 'error_500.html', status=500)

def error_503_view(request):
    return render(request, 'error_503.html', status=503)

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def surfacefinish(request):
    data=Surfacefinish.objects.all()
    context={'data':data}
    return render(request,'surfacefinish.html',context)
    
# def surfacefinishform(request):
#     if request.method == 'POST':
#         name_f = request.POST['surface_name']
#         icon_f = request.FILES['icon']
#         Surfacefinish.objects.create(surface_name=name_f, icon=icon_f)
#         return redirect('/surfacefinish')
#     else:
#         return render(request, 'surfacefinishform')

# def surfacefinishform(request):
#     if request.method == 'POST':
#         name_f = request.POST['surface_name']
#         icon_f = request.FILES['icon']
        
#         # Check if a record with the same name already exists
#         existing_record = Surfacefinish.objects.filter(surface_name=name_f).first()
        
#         if existing_record:
#             # Handle the case where the name already exists
#             # You can display an error message to the user
#             # or update the existing record if needed
#             # For example, you can update the icon of the existing record:
#             existing_record.icon = icon_f
#             existing_record.save()
#         else:
#             # Create a new record if the name is unique
#             Surfacefinish.objects.create(surface_name=name_f, icon=icon_f)
        
#         return redirect('/surfacefinish')
#     else:
#         return render(request, 'surfacefinishform.html')

def surfacefinishform(request):
    if request.method == 'POST':
        name_f = request.POST['surface_name']
        icon_f = request.FILES['icon']
        
        existing_record = Surfacefinish.objects.filter(surface_name=name_f).first()
        
        if existing_record:
            messages.error(request, f'Surfacefinish with name "{name_f}" already exists.')
        else:
            Surfacefinish.objects.create(surface_name=name_f, icon=icon_f)
            messages.success(request, f'Surfacefinish "{name_f}" added successfully.')
        
        return redirect('/surfacefinish')
    else:
        return render(request, 'surfacefinish.html')
    
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

@login_required
def brand(request):
    data=Brand.objects.filter(is_active=True)
    context={'data':data}
    return render(request,'brand.html',context)
    
# def brandform(request):
#     if request.method == 'POST':
#         name_f = request.POST['brand_name']
#         brand_image_f = request.FILES['brand_image']
#         Brand.objects.create(brand_name=name_f, brand_image=brand_image_f)
#         return redirect('/brand')
#     else:
#         return render(request, 'brandform.html')

def brandform(request):
    if request.method == 'POST':
        name_f = request.POST['brand_name']
        brand_image_f = request.FILES['brand_image']

        if Brand.objects.filter(brand_name=name_f).exists():
            messages.error(request, 'A Brand with this name already exists.')
        else:
            Brand.objects.create(brand_name=name_f, brand_image=brand_image_f)
            messages.success(request, 'Brand created successfully.')

        return redirect('/brand')
    else:
        return render(request, 'brand.html')
    

    
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

@login_required
def collection(request):
    collections = Collection.objects.all()
    brands = Brand.objects.all()
    context = {'collections': collections, 'brands': brands}
    return render(request, 'collection.html', context)

# def collectionform(request):
#     brands = Brand.objects.all()

#     if request.method == 'POST':
#         collection_name_f = request.POST['collection_name']
#         brand_id = request.POST['brand_name']

#         try:
#             brand_obj = Brand.objects.get(id=brand_id)
#             Collection.objects.create(collection_name=collection_name_f, brand=brand_obj)
#             return redirect('/collection')
#         except Brand.DoesNotExist:
#             return render(request, 'collectionform.html', {'brands': brands})

#     return render(request, 'collectionform.html', {'brands': brands})


def collectionform(request):
    brands = Brand.objects.all()

    if request.method == 'POST':
        collection_name_f = request.POST['collection_name']
        brand_id = request.POST['brand_name']

        try:
            brand_obj = Brand.objects.get(id=brand_id)
            if Collection.objects.filter(collection_name=collection_name_f, brand=brand_obj).exists():
                messages.error(request, 'A Collection with this name already exists for the selected brand.')
            else:
                Collection.objects.create(collection_name=collection_name_f, brand=brand_obj)
                messages.success(request, 'Collection created successfully.')
                return redirect('/collection')
        except Brand.DoesNotExist:
            messages.error(request, 'Invalid Brand selected.')
    
    return render(request, 'collection.html', {'brands': brands})


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

# def updatecollection(request,id):
#     data=Collection.objects.get(id=id)
#     brand=Brand.objects.all()
#     if request.method=='POST':
#         collection_name_f=request.POST['collection_name']

#         data.collection_name=collection_name_f
#         data.save()
#         return redirect('/collection')
#     context={'data':data,'brand':brand}
#     return render(request,'updatecollection.html',context)

def updatecollection(request, id):
    data = Collection.objects.get(id=id)
    brands = Brand.objects.all()

    if request.method == 'POST':
        collection_name_f = request.POST['collection_name']
        brand_id = request.POST['brand_name']

        try:
            brand_obj = Brand.objects.get(id=brand_id)
            data.collection_name = collection_name_f
            data.brand = brand_obj
            data.save()
            return redirect('/collection')
        except Brand.DoesNotExist:
            return render(request, 'updatecollection.html', {'data': data, 'brands': brands})

    context = {'data': data, 'brands': brands}
    return render(request, 'updatecollection.html', context)

@login_required 
def series(request):
    series = Series.objects.all()
    collections = Collection.objects.all()
    context = {'series': series, 'collections': collections}
    return render(request, 'series.html', context)

# def seriesform(request):
#     collections = Collection.objects.all()

#     if request.method == 'POST':
#         series_name_f = request.POST['series_name']
#         collection_id = request.POST['collection_name']

#         try:
#             collection_obj = Collection.objects.get(id=collection_id)
#             Series.objects.create(series_name=series_name_f, collection=collection_obj)
#             return redirect('/series')
#         except Collection.DoesNotExist:
#             return render(request, 'seriesform.html', {'collections': collections})

#     return render(request, 'seriesform.html', {'collections': collections})

      
def seriesform(request):
    collections = Collection.objects.all()
    print(collections)
    if request.method == 'POST':
        series_name_f = request.POST['series_name']
        collection_id = request.POST['collection_name']

        try:
            collection_obj = Collection.objects.get(id=collection_id)

            if Series.objects.filter(series_name=series_name_f, collection=collection_obj).exists():
                messages.error(request, 'A Series with this name already exists for the selected Collection.')
            else:
                Series.objects.create(series_name=series_name_f, collection=collection_obj)
                messages.success(request, 'Series created successfully.')
                return redirect('/series')
        except Collection.DoesNotExist:
            messages.error(request, 'Invalid Collection selected.')

    return render(request, 'series.html', {'collections': collections})

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

# def updateseries(request,id):
#     data=Series.objects.get(id=id)
#     collection=Collection.objects.all()
#     if request.method=='POST':
#         series_name_f = request.POST['series_name']


#         data.series_name=series_name_f
#         data.save()
#         return redirect('/series')
#     context={'data':data,'collection':collection}
#     return render(request,'updateseries.html',context)

def updateseries(request, id):
    series = Series.objects.get(id=id)
    collections = Collection.objects.all()

    if request.method == 'POST':
        series_name_f = request.POST['series_name']
        collection_id = request.POST['collection']

        try:
            collection_obj = Collection.objects.get(id=collection_id)

            series.series_name = series_name_f
            series.collection = collection_obj 
            series.save()

            return redirect('/series')
        except Collection.DoesNotExist:
            messages.error(request, 'Invalid Collection selected.')

    context = {'data': series, 'collection': collections}
    return render(request, 'updateseries.html', context)