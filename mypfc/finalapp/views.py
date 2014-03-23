# Create your views here.
from django.http import HttpResponse
from finalapp.models import *
from django.core.exceptions import ObjectDoesNotExist

def home(request):
	p = File_links.objects.get(pk=11)
	html = "<html><body>home</body></html>"
	return HttpResponse(p.file_path)

def users(request):
	html = ""
	users = People.objects.all()
	for user in users:
		html += "<p>" + user.name + "</p>"
	return HttpResponse(html)

def projects(request, project):
	html = "<html><body>projects view goes here</body></html>"
	return HttpResponse(html + " and project name is " + project)

def commits(request, user):
	try:
		user_id = People.objects.get(name=user).id
		commits = Scmlog.objects.filter(committer=user_id)
		html = ""
		for i in commits:
			html += "<p>" + i.message + "</p>"
		return HttpResponse(html)

	except ObjectDoesNotExist:
		return HttpResponse("user does not exist")
