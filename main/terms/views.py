from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Terms, Privacy, Cookies

def terms_view(request):
    """Vista per i termini e condizioni"""
    try:
        terms = Terms.objects.filter(is_active=True).first()
        if not terms:
            raise Http404("Termini e condizioni non trovati")
        
        context = {
            'terms': terms,
            'page_title': 'Termini e Condizioni',
        }
        return render(request, 'terms/terms.html', context)
    except Exception as e:
        raise Http404("Errore nel caricamento dei termini e condizioni")

def privacy_view(request):
    """Vista per l'informativa sulla privacy"""
    try:
        privacy = Privacy.objects.filter(is_active=True).first()
        if not privacy:
            raise Http404("Informativa sulla privacy non trovata")
        
        context = {
            'privacy': privacy,
            'page_title': 'Informativa sulla Privacy',
        }
        return render(request, 'terms/privacy.html', context)
    except Exception as e:
        raise Http404("Errore nel caricamento dell'informativa sulla privacy")

def cookies_view(request):
    """Vista per l'informativa sui cookie"""
    try:
        cookies = Cookies.objects.filter(is_active=True).first()
        if not cookies:
            raise Http404("Informativa sui cookie non trovata")
        
        context = {
            'cookies': cookies,
            'page_title': 'Informativa sui Cookie',
        }
        return render(request, 'terms/cookies.html', context)
    except Exception as e:
        raise Http404("Errore nel caricamento dell'informativa sui cookie")
