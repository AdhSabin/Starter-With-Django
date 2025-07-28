from django.shortcuts import render,redirect
from .models import Book,Publisher,Author
from .forms import PublisherForm,AuthorForm,BookForm
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json

# Replace with your Khalti secret key
KHALTI_SECRET_KEY = 'your_secret_key'
KHALTI_VERIFY_URL = 'https://khalti.com/api/v2/epayment/'

# Create your views here.
def booklist(request):
    books = Book.objects.all()
    return render(request,'relation/booklist.html', {'books': books})

def addpublisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booklist')
    else:
        form=PublisherForm()
    return render(request,'relation/addpublisher.html',{'form':form})

def addauthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booklist')
    else:
        form=AuthorForm()
    return render(request,'relation/addauthor.html',{'form':form})

def addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('booklist')
    else:
        form=BookForm()
    return render(request,'relation/addbook.html',{'form':form})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'relation/bookdetail.html', {'book':book})


@csrf_exempt
def verify_khalti_payment(request):
    if request.method == "POST":
        try:
            payload =json.loads(request.body)

            response = requests.post(
                KHALTI_VERIFY_URL,
                json={
                    'token': payload.get("token"),
                    'amount':payload.get("amount")

                },
                headers={
                    'Authorization':f'Bearer{KHALTI_SECRET_KEY}',
                    'Content-Type':'application/json'
                }
            )
            verification_data = response.json()

            if response.status_code == 200 and verification_data.get('status') == 'success':
                return JsonResponse({"success":True})
            else:
                return JsonResponse({"success":False},status=400)
            
        except Exception as e:
            return JsonResponse({"success":False,"error":str(e)},status=400)
    
    return JsonResponse({"success":False},status=400)