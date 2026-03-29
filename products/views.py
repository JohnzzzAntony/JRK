from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category

def category_index(request):
    """Image 1: Shows all categories in a grid."""
    categories = Category.objects.all()
    return render(request, 'products/category_index.html', {
        'categories': categories
    })

def product_list(request):
    """Shows filtered/searched product list."""
    categories = Category.objects.all()
    products = Product.objects.all()
    
    # Handle Search
    query = request.GET.get('q')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(overview__icontains=query))
    
    return render(request, 'products/product_list.html', {
        'categories': categories,
        'products': products
    })

def category_detail(request, slug):
    """Shows products within a specific category."""
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all() # Needed for sidebar
    return render(request, 'products/product_list.html', {
        'current_category': category, 
        'products': products,
        'categories': categories
    })

def product_detail(request, slug):
    """Image 2: Product detail page with specs fetching by slug for SEO."""
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})
