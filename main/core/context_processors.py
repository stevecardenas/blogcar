from django.core.cache import cache
from .models import SocialMedia, SiteSettings, Navigation

def global_context_processor(request):
    """Context processor para hacer datos globales disponibles en todos los templates con caché"""
    
    # Cache social media for 5 minutes
    social_media = cache.get('social_media_active')
    if social_media is None:
        social_media = list(SocialMedia.objects.filter(is_active=True).order_by('order'))
        cache.set('social_media_active', social_media, 300)
    
    # Cache site settings for 5 minutes
    site_settings = cache.get('site_settings_active')
    if site_settings is None:
        site_settings = SiteSettings.get_active_settings()
        cache.set('site_settings_active', site_settings, 300)
    
    # Cache navigation for 5 minutes
    navigation = cache.get('navigation_active')
    if navigation is None:
        navigation = list(Navigation.get_active_navigation())
        cache.set('navigation_active', navigation, 300)
    
    return {
        'social_media': social_media,
        'site_settings': site_settings,
        'navigation': navigation,
    } 