from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(listing=listing,
                          listing_id=listing_id,
                          name=name,
                          email=email,
                          phone=phone,
                          message=message)

        contact.save()

        messages.success(request, 'Your message has been sent')
        return redirect(f'/listings/{listing_id}')
