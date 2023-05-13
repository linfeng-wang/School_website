from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'info/home.html')

def education(request):
	return render(request, 'info/education.html')

def committee(request):
	return render(request, 'info/committee.html')

def compage(request):
	return render(request, 'info/committee/compage.html')

def chen(request):
	return render(request, 'info/committee/chen.html')

def liu(request):
	return render(request, 'info/committee/liu.html')

def xu(request):
	return render(request, 'info/committee/xu.html')

def contact(request):
	return render(request, 'info/contact.html')

def camppage(request):
	return render(request, 'info/camp/camppage.html')

def tarif(request):
	return render(request, 'info/tarif.html')