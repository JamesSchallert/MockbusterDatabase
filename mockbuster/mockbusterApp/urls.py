from django.urls import path
from . import views

urlpatterns = [
	
	path('videogame_inventory/', views.VideoGameList.as_view(),name='videogame_inventory'),
	path('Rent/',views.Rent.as_view(),name='Rent'),
	path('Return/<int:pk>',views.Return.as_view(),name='Return'),
	path('NewRental/',views.NewRental.as_view(),name='NewRental'),
	path('Customer/',views.Customer.as_view(),name='Customer'),
	path('NewCustomer/',views.NewCustomer.as_view(),name='NewCustomer'),
	path('DeleteCustomer/<int:pk>',views.DeleteCustomer.as_view(),name='DeleteCustomer'),
	path('UpdateCustomer/<int:pk>',views.UpdateCustomer.as_view(),name='UpdateCustomer'),
    #path('view/<int:pk>', views.MockbusterView.as_view(), name='mockbuster_view'),
    #path('new', views.MockbusterCreate.as_view(), name='mockbuster_new'),
    #path('view/<int:pk>', views.MockbusterView.as_view(), name='mockbuster_view'),
    #path('edit/<int:pk>', views.MockbusterUpdate.as_view(), name='mockbuster_edit'),
    #path('delete/<int:pk>', views.MockbusterDelete.as_view(), name='mockbuster_delete'),
]
