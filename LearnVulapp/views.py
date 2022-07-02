from django.forms.models import fields_for_model
from django.http.response import HttpResponseRedirect
from .forms import CommentForm, Commentf
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import DetailView,CreateView
from .models import Book, Comment
from django.urls import reverse_lazy
from json import dumps
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def book_by_id(request,book_id):
    book = Book.objects.get(pk=book_id)
    #return HttpResponse(f'Book: {book.title}, published on{book.pub_date}')
    return render(request,'book_details.html',{'book':book})

def homeView(request):
    return render(request, 'home.html')

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        #answ = Book.objects.all()
        answ = Book.objects.all().filter(title=search)
        return render(request,'searchbar.html',{'answ':answ,'search':search})
'''
def detailbook(request):
    if  request.method == 'GET':
        istenilen = request.GET.get('')
'''

def feed(request):
    if request.method == 'GET':
        #answ = Book.objects.all()
        answ = Book.objects.all()
        return render(request,'feed.html',{'answ':answ})

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_details.html'

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    #success_url = redirect('feed')
    def form_valid(self,form):
        form.instance.book_id = self.kwargs['pk']
        return super().form_valid(form)


def comment(self,request):
    
    if request.method == 'POST':
        form = Commentf(request.POST)
        if form.is_valid():
            
            #buraya devam
            answ = Book.objects.all()
            #return render(request,'LearnVulsite.LearnVulapp.views.feed',{'answ':answ})
            #return HttpResponseRedirect()
             #return render(request,self,{'form':form})
    else:
        form = Commentf()

    return render(request,'add_comment.html',{'form':form})
    
def contact(request):
  if request.method == 'GET':
    return render(request,'contact.html')


def contact_result(request):
    
    
    uname = request.GET['uname']
    topic = request.GET['topic']
    
    return render(request,'contactresult.html',{'name':uname})