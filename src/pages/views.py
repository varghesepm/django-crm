from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_main(request,*args,**kwargs):
	print(request.user)
	print(args,kwargs)
	#return HttpResponse("<h1>Hello World</h>")
	return render(request, "home.html", {})

def contact_main(*args,**kwargs):
	return render(request, "contact.html", {})

def about_main(request,*args,**kwargs):
	my_context = {
			"my_tittle": "About Us",
			"my_number": 123456
	}
	return render(request, "about.html", my_context )