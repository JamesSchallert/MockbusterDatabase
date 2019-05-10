from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from mockbusterApp.models import Branch, VideoGame, Rental, Customer as CustomerModel

class Rent(ListView):
	model = Rental
	template_name = 'mockbusterApp/Rent.html'
	
class Return(DeleteView):
	model= Rental
	template_name = 'mockbusterApp/Return.html'
	success_url = reverse_lazy('Rent')

class NewRental(CreateView):
	model= Rental
	template_name = 'mockbusterApp/NewRental.html'
	fields = ['vg','cu','br','em']
	success_url = reverse_lazy('Rent')

class Customer(ListView):
	model = CustomerModel
	template_name = 'mockbusterApp/Customer.html'
	
class DeleteCustomer(DeleteView):
	model= CustomerModel
	template_name = 'mockbusterApp/DeleteCustomer.html'
	success_url = reverse_lazy('Customer')
	
class NewCustomer(CreateView):
	model= CustomerModel
	template_name = 'mockbusterApp/NewCustomer.html'
	fields = ['cu_first_name','cu_last_name','cu_phone_num','cu_address']
	success_url = reverse_lazy('Customer')

class UpdateCustomer(UpdateView):
	model = CustomerModel
	template_name = 'mockbusterApp/UpdateCustomer.html'
	fields = ['cu_first_name','cu_last_name','cu_phone_num','cu_address']
	success_url = reverse_lazy('Customer')

class Home(TemplateView):
	template_name = "mockbusterApp/home.html"

class VideoGameList(ListView):
    model = VideoGame

class MockbusterCreate(CreateView):
    model = VideoGame
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')

class MockbusterUpdate(UpdateView):
    model = VideoGame
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')

class MockbusterDelete(DeleteView):
    model = VideoGame
    success_url = reverse_lazy('book_list')