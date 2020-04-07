from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
text2 = '''
	 cbawieufb vawub cavwbs
        
	'''
def index(request):
	text = '''
	 Using color to add meaning only provides a visual indication, 
		which will not be conveyed to users of assistive technologies – such as 
		screen readers. Ensure that information denoted by the color is either 
		obvious from the content itself , or is included through alternative means, 
		such as additional text hidden with th
        
	'''
	return render(request, 'myApp/index.html', {'text' : text, 'text2':text2})


def detail(request):
	text2 = '''
	 cbawieufb vawub cavwbs
        
	'''
	return render(request, 'myApp/detail.html', {'text2' : text2})


