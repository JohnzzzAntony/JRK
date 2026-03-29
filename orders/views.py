from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import QuoteEnquiry, QuoteItem
from django.contrib import messages

def enquiry_cart(request):
    cart = request.session.get('enquiry_cart', {})
    cart_items = []
    
    for product_id, item_data in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))
            cart_items.append({
                'product': product,
                'quantity': item_data['quantity'],
                'price': item_data.get('price', 0),
                'total_item': float(item_data.get('price', 0)) * int(item_data['quantity'])
            })
        except Product.DoesNotExist:
            continue
            
    return render(request, 'orders/enquiry_cart.html', {'cart_items': cart_items})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('enquiry_cart', {})
    
    price = float(product.sale_price if product.sale_price > 0 else product.regular_price)
    
    str_id = str(product_id)
    if str_id in cart:
        cart[str_id]['quantity'] += 1
    else:
        cart[str_id] = {
            'quantity': 1,
            'price': str(price)
        }
        
    request.session['enquiry_cart'] = cart
    messages.success(request, f"{product.name} added to your enquiry cart.")
    return redirect('enquiry_cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('enquiry_cart', {})
    str_id = str(product_id)
    if str_id in cart:
        del cart[str_id]
        request.session['enquiry_cart'] = cart
        messages.info(request, "Product removed from enquiry cart.")
        
    return redirect('enquiry_cart')

# New View for Image 3 Form Submission
def submit_enquiry(request):
    if request.method == 'POST':
        cart = request.session.get('enquiry_cart', {})
        if not cart:
            messages.warning(request, "Your enquiry cart is empty.")
            return redirect('enquiry_cart')
            
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        department = request.POST.get('department')
        country = request.POST.get('country')
        city = request.POST.get('city')
        street = request.POST.get('street')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        
        # Save Enquiry
        enquiry = QuoteEnquiry.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            department=department,
            country=country,
            city=city,
            street=street,
            phone=phone,
            comment=comment
        )
        
        # Save Quote Items
        for product_id, item_data in cart.items():
            product = get_object_or_404(Product, id=int(product_id))
            QuoteItem.objects.create(
                enquiry=enquiry,
                product=product,
                quantity=item_data['quantity']
            )
            
        # Clear Cart
        request.session['enquiry_cart'] = {}
        
        # Optionally send notification email here
        
        context = {
            'enquiry': enquiry,
        }
        return render(request, 'orders/success.html', context)
        
    return redirect('enquiry_cart')
