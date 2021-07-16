from django.shortcuts import redirect, render
from .models import Contacttuber
from django.contrib import messages
# Create your views here.
def contact_tuber(request):
    
    if request.method=='POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']
        
        contacttuber = Contacttuber(name=name, phone=phone, email=email, company_name=company_name, subject=subject, message=message)
        contacttuber.save()
        messages.success(request, 'Thanks for Reaching out...............')
        
    
        return redirect('youtubers')

    pass