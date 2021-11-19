from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import render, redirect

# Create your views here.
from devpro.shortener.models import UrlRedirect, UrlLog


def report_url(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    url_reduce = request.build_absolute_uri(f'/{slug}')
    redirect_for_data = list(
        UrlRedirect.objects.filter(
            slug=slug
        ).annotate(
            data=TruncDate('logs__created_in')
        ).annotate(
            clicks=Count('data')
        ).order_by('data')
    )
    contexto = {
        'reduce': url_redirect,
        'url_reduce': url_reduce,
        'redirect_for_data': redirect_for_data,
        'total_clicks': sum(r.clicks for r in redirect_for_data)
    }
    return render(request, 'shortener/report.html', contexto)


def redirect_url(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    UrlLog.objects.create(
        origin=request.META.get('HTTP_REFERER'),
        user_agent=request.META.get('HTTP_USER_AGENT'),
        host=request.META.get('HTTP_HOST'),
        ip=request.META.get('REMOTE_ADDR'),
        url_redirect=url_redirect
    )
    return redirect(url_redirect.destiny)
