import os
import django
from django.core.files.base import ContentFile
import urllib.request
import textwrap

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jkr.settings')
django.setup()

from products.models import Category, Product, ProductSKU, ProductImage
from pages.models import AboutUs, MissionVision, Service, Counter, WhyUsCard, GalleryItem
from sliders.models import HeroSlider

def populate():
    print("Clearing old data...")
    Category.objects.all().delete()
    AboutUs.objects.all().delete()
    MissionVision.objects.all().delete()
    Service.objects.all().delete()
    HeroSlider.objects.all().delete()

    print("Creating Categories...")
    cats = [
        "Compression Stockings", "Exercise Therapy", "Homecare", 
        "Hospital Equipment & Furniture", "Orthopedic Products", 
        "Physiotherapy & Rehabilitation", "Prosthetics & Orthotics",
        "Seating & Positioning System", "Walking & Standing Aids", "Wheelchairs"
    ]
    
    cat_objs = {}
    for c in cats:
        cat_objs[c] = Category.objects.create(
            name=c,
            meta_title=f"{c} - JKR International",
            meta_description=f"Best {c} in UAE with top quality."
        )

    print("Creating Products...")
    products_data = [
        ("medi Armschlinge", "Orthopedic Products", "Comfortable arm sling for injury recovery.", 45.00),
        ("duomed® smooth", "Compression Stockings", "Smooth and effective compression stockings for daily use.", 120.00),
        ("iCHAIR MC1 LIGHT 1.610", "Wheelchairs", "Advanced lightweight electric wheelchair.", 2500.00),
        ("Flash 1.135", "Wheelchairs", "Dynamic and rapid mobility wheelchair.", 1800.00),
        ("Sissel Tour- Cushion", "Seating & Positioning System", "Cushion specifically designed for car seats.", 75.00),
        ("SISSEL® Spiky-Ball", "Exercise Therapy", "Textured ball for deep tissue massage and therapy.", 15.00),
        ("Euro Chair 2.750", "Wheelchairs", "Classic, reliable manual wheelchair from MEYRA.", 850.00),
        ("CarePump Move8", "Physiotherapy & Rehabilitation", "High-tech rehabilitation pump system.", 3200.00),
        ("Celta ST Manual Steel Chair", "Wheelchairs", "Sturdy manual steel chair for daily use.", 500.00),
        ("Apollo Patient Bed", "Hospital Equipment & Furniture", "Super low single panel patient bed.", 1100.00),
    ]

    for title, cat, desc, price in products_data:
        p = Product.objects.create(
            category=cat_objs[cat],
            name=title,
            overview=desc,
            is_active=True
        )
        ProductSKU.objects.create(
            product=p,
            sku_id=f"SKU-{title.split()[0].upper()}-001",
            price=price,
            quantity=15,
            unit="pcs",
            weight=1.5, length=10, width=10, height=10,
            shipping_charge=5.00,
            delivery_time="2-3 Days",
            shipping_status="available"
        )
    
    print("Creating CMS/Homepage Blocks...")
    HeroSlider.objects.create(
        title="Redefining Mobility Excellence",
        subtitle="Top-tier medical solutions to Hospitals, Pharmacies, and Healthcare facilities",
        button_text="Shop Now",
        button_link="/products/",
        is_active=True
    )

    AboutUs.objects.create(
        title="About Us",
        heading="We craft solutions that enhance and Simplify Lives.",
        content="<p>JKR International is a trusted Medical Equipment Supplier in UAE, providing high-quality wheelchairs, rehabilitation products, and expert guidance. Joy, Knowledge, Responsibility are our core values.</p>",
    )

    MissionVision.objects.create(
        section_type='mission',
        title="Our Mission",
        content="To be the Company of Choice that provides quality medical devices, designed to enable, enhance and enrich the lives of our people."
    )

    Service.objects.create(title="High-Quality Products", description="Our innovative mobility products of the highest industry standards.")
    Service.objects.create(title="Customer Satisfaction", description="Attendant personally and professionally to deliver the best mobility solutions.")
    Service.objects.create(title="After Sales Support", description="A team of qualified engineers and technicians available on call.")

    Counter.objects.create(title="Partnerships", value="100+")
    Counter.objects.create(title="Products Delivered", value="1500+")

    WhyUsCard.objects.create(
        title="Expert Advice",
        description="We offer expert guidance to help our clients adapt to the rising costs of quality healthcare.",
        icon_svg='<svg fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a8 8 0 100 16 8 8 0 000-16zM9 9a1 1 0 012 0v4a1 1 0 11-2 0V9zm1-5a1.5 1.5 0 110 3 1.5 1.5 0 010-3z"></path></svg>'
    )

    print("Success! Database populated with JKR site mock data.")

if __name__ == '__main__':
    populate()
