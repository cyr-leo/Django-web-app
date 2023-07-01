from django.shortcuts import render
from  django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from  listings.models import Listing


def hello(request):
    bands = Band.objects.all()
    return render (request,'listings/hello.html',{'bands': bands})
def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def list(request):
    listings = Listing.objects.all()
    return render (request, 'listings/listings.html' , {'listings' : listings})

