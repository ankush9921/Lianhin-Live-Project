from django.urls import path
from .import views

handler404 = views.error_404_view


urlpatterns = [
    path('',views.sign_in,name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
    # path('sign_up',views.sign_up,name='sign_up'),
    path('index',views.index,name='index'),
    path('accounts/sign_in/', views.sign_in, name='sign_in'),

    path('surfacefinish',views.surfacefinish,name='surfacefinish'),
    path('surfacefinishform',views.surfacefinishform,name='surfacefinishform'),
    path('Active_surfacefinish/<int:id>',views.Active_surfacefinish,name='Active_surfacefinish'),
    path('Deactive_surfacefinish/<int:id>',views.Deactive_surfacefinish,name='Deactive_surfacefinish'),
    path('updatesurfacefinish/<int:id>',views.updatesurfacefinish,name='updatesurfacefinish'),
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

    path('series',views.series,name='series'),
    path('seriesform',views.seriesform,name='seriesform'),
    path('Active_series/<int:id>',views.Active_series,name='Active_series'),
    path('Deactive_series/<int:id>',views.Deactive_series,name='Deactive_series'),
    path('updateseries/<int:id>',views.updateseries,name='updateseries'),
    path('deleteseries/<int:id>',views.deleteseries,name='deleteseries'),

    path('model',views.model,name='model'),
    path('modelform',views.modelform,name='modelform'),
    path('Active_model/<int:id>',views.Active_model,name='Active_model'),
    path('Deactive_model/<int:id>',views.Deactive_model,name='Deactive_model'),
    path('updatemodel/<int:id>',views.updatemodel,name='updatemodel'),
    path('deletemodel/<int:id>',views.deletemodel,name='deletemodel'),
]