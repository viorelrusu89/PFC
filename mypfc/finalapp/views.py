# Create your views here.
from django.http import HttpResponse
from finalapp.models import Tags
def home(request):
	html = "<html><body>home</body></html>"
	p = Tags(id=2, name="sori")
	p.save()
	return HttpResponse(html)

def users(request):
	html = "<html><body>users view goes here</body></html>"
	return HttpResponse(html)

def projects(request, project):
	html = "<html><body>projects view goes here</body></html>"
	return HttpResponse(html + " and project name is " + project)

def commits(request, user):
	html = "<html><body>commits view goes here</body></html>"
	return HttpResponse(html)

