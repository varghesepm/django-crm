from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_main(request,*args,**kwargs):
	print(request.user)
	print(args,kwargs)
	#return HttpResponse("<h1>Hello World</h>")
	return render(request, "home.html", {})

def contact_main(*args,**kwargs):
	return HttpResponse("<h1>Contact Page</h>")
	
def about_main(*args,**kwargs):
	return HttpResponse("<h1>About Page</h>")