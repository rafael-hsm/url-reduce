from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from devpro.shortener.models import UrlRedirect


def report_url(request, slug):
    return render(request, 'shortener/report.html')


def redirect_url(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    return redirect(url_redirect.destiny)
