from .models import SiteSettings

def site_settings(request):
    try:
        settings = SiteSettings.objects.first()
        if not settings:
            settings = SiteSettings.objects.create()
    except Exception:
        # In case DB is not migrated yet
        settings = None
    return {'site_settings': settings}
