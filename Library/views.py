from django.shortcuts import render,redirect,HttpResponse
from . models import Book
from .forms import BookCreate
from django.core.mail import send_mail

# Create your views here.
def library(request):
    user = request.user
    shelf = Book.objects.all()
    return render(request,'library.html',{'shelf':shelf,'user':user})

def uploadform(request):
    upload = BookCreate()
    if request.method == "POST":
        upload = BookCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('library')
        else:
            return HttpResponse("Something went wrong.Please reload ")
    else:
        return render(request,'uploadform.html',{'upload_form':upload}) 
		
def update_book(request,book_id):
	book_id = int(book_id)
	try:
		book_shelf = Book.objects.get(id=book_id)
	except Book.DoesNotExist:
		return redirect('library')
	
	book_form = BookCreate(request.POST or None, instance=book_shelf)
	if book_form.is_valid():
		book_form.save()
		return redirect('library')
		
	return render(request,'uploadform.html',{'upload_form':book_form})

def delete_book(request,book_id):
      book_id = int(book_id)

      try:
        book_shelf = Book.objects.get(id=book_id)
      except:
        return redirect('library')
      book_shelf.delete()
      return redirect('library') 

def send_template_email(request):
    subject = 'This is the demo for sending mail'
    #html_message = render_to_string('new.html', {'context_variable': 'value'})
    plain_message = "Hey, just completed email integration on django"
    from_email = 'sabinadhikari494@gmail.com'
    to_email = ['itsmeas69@gmail.com']
    send_mail(subject, plain_message, from_email, to_email)
    return render(request,'new.html') 

def send_template_email(request):
    if request.method == "POST":
        # Get values from modal form
        from_email = 'sabinadhikari494@gmail.com'
        to_email = request.POST['to_email']
        subject = request.POST['subject']
        body = request.POST['body']

        # Send the email
        try:
            send_mail(subject, body, from_email, [to_email])
            return render(request, 'new.html', {'message': 'Email sent successfully!'})
        except Exception as e:
            return render(request, 'new.html', {'message': f'Failed to send email: {e}'})
    else:
        return redirect('library') 



















# def send_template_email(request):
#     if request.method == 'POST':
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             from_email = form.cleaned_data['from_email']
#             to_email = [form.cleaned_data['to_email']]  # list
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             send_mail(subject, message, from_email, to_email)
#             return render(request,'new.html') 
#     else:
#         form = EmailForm()
#     return render(request, 'new.html', {'form': form})
            
















