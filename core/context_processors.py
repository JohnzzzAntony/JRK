from .models import SiteSettings, NavMenuItem

def site_settings(request):
    try:
        settings = SiteSettings.objects.first()
        nav_items = NavMenuItem.objects.all() # Or specifically active ones
    except:
        settings = None
        nav_items = []
        
    return {
        'site_settings': settings,
        'nav_menu': nav_items
    }
