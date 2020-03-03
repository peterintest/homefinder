from django.shortcuts import render
from listings.search_options import bedroom_options, price_options

from listings.models import Listing

def index(request):
    listings = Listing.objects.order_by('-creation_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'bedroom_options': bedroom_options,
        'price_options': price_options
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
