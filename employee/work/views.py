from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import EmpForm
from work.models import Emp
from work.forms import BookForm
from work.models import Book
from work.forms import BooksForm
from work.models import Books

class Booklist(View):
  def get(self ,request,*args,**kwargs):
    qs=Book.objects.all()
    return render(request,"booklist.html",{"qs":qs})
  


class Book_detailView(View):
  def get(self,request,**kwargs):  
    print(kwargs)
    id=kwargs.get("pk")
    qs=Books.objects.get(id=id)
    return render(request,"bookd.html",{"data":qs})


class Book_delete(View):
  def get(self,request,*args,**kwargs):
    id=kwargs.get("pk")
    Book.objects.get(id=id).delete()
    return redirect("book-al")




class BookView(View):
   def get(self,request):
     form=BookForm()
     return render(request,"book.html",{"form":form})
   
   def post(self,request):
    form=BookForm(request.POST)
    if form.is_valid():
     print(form.cleaned_data)  
     Book.objects.create(**form.cleaned_data)

     return render(request,"book.html",{"form":form})
    else:
     return render(request,"book.html",{"form":form})
    

class BOOKView(View):
   def get(self,request):
     form=BooksForm
     return render(request,"books.html",{"form":form})    
   
   def post(self,request):
    form=BooksForm(request.POST)
    if form.is_valid():
      form.save()
      print("created")
      return render(request,"books.html",{"form":form})
    else:
     return render(request,"books.html",{"form":form})
    
    

      
   
  

class Employee(View):
 def get(self,request):
    form=EmpForm()
    return render(request,"add.html",{"form":form})
 
 def post(self,request):
   form=EmpForm(request.POST)
   if form.is_valid():
     print(form.cleaned_data)
     Emp.objects.create(**form.cleaned_data)

     return render(request,"add.html",{"form":form})
   else:
     return render(request,"add.html",{"form":form})
   
       
# Create your views here.
