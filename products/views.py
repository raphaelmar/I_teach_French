from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Level

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    levels = None
    
    if request.GET:
        if 'level' in request.GET:
            levels = request.GET['level'].split(',')
            products = products.filter(level__name__in=levels)
            levels = Level.objects.filter(name__in=levels)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,"You did not enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_levels': levels,
    }

    return render(request, 'products/products.html', context)
    