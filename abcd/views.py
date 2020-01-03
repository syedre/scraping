from django.shortcuts import render
from .models import Webd
import requests
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
	return render(request,'home.html')

def title(request):
	
	url = request.POST.get("name")
	#url = 'https://timesofindia.indiatimes.com/'
	z = requests.get(url)
	if z.status_code == 200:
		soup = BeautifulSoup(z.content, 'html.parser')
		title=soup.title.string
		Webd.objects.create(name=title)
		return render(request,'title.html', {'til':title})
	
