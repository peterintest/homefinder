from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .search_options import bedroom_options, price_options

from .models import Listing

def index(request):
    listings = Listing.objects.all().filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.all()

    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(city__icontains=keywords) \
            | queryset_list.filter(postcode__icontains=keywords) \
            | queryset_list.filter(county__icontains=keywords) \
            | queryset_list.filter(title__icontains=keywords) \

    #Filter by number of bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__icontains=bedrooms)

    #Filter up to max price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'bedroom_options': bedroom_options,
        'price_options': price_options,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)
