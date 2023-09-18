from django.urls import path
from .import views


urlpatterns = [
    path('sign_in',views.sign_in,name='sign_in'),
    # path('sign_up',views.sign_up,name='sign_up'),
    path('',views.index,name='index'),

    path('surfacefinish',views.surfacefinish,name='surfacefinish'),
    path('surfacefinishform',views.surfacefinishform,name='surfacefinishform'),
    path('Active_surfacefinish/<int:id>',views.Active_surfacefinish,name='Active_surfacefinish'),
    path('Deactive_surfacefinish/<int:id>',views.Deactive_surfacefinish,name='Deactive_surfacefinish'),
    path('updatesurfacefisnish/<int:id>',views.updatesurfacefinish,name='updatesurfacefinish'),
    path('deletesurfacefinish/<int:id>',views.deletesurfacefinish,name='deletesurfacefinish'),

    path('brand',views.brand,name='brand'),
    path('brandform',views.brandform,name='brandform'),
    path('Active_brand/<int:id>',views.Active_brand,name='Active_brand'),
    path('Deactive_brand/<int:id>',views.Deactive_brand,name='Deactive_brand'),
    path('updatebrand/<int:id>',views.updatebrand,name='updatebrand'),
    path('deletebrand/<int:id>',views.deletebrand,name='deletebrand'),

    path('collection',views.collection,name='collection'),
    path('collectionform',views.collectionform,name='collectionform'),
    path('Active_collection/<int:id>',views.Active_collection,name='Active_collection'),
    path('Deactive_collection/<int:id>',views.Deactive_collection,name='Deactive_collection'),
    path('updatecollection/<int:id>',views.updatecollection,name='updatecollection'),
    path('deletecollection/<int:id>',views.deletecollection,name='deletecollection'),
]