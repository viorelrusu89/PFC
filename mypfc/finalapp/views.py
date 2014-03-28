from django.http import HttpResponse
from scm_query import buildSession
from datetime import datetime

def home(request):

	html = "<html><body>home</body></html>"
	return HttpResponse(html)

def users(request):
	html = ""
	return HttpResponse(html)

def projects(request, project):
	html = "<html><body>projects view goes here</body></html>"
	return HttpResponse(html + " and project name is " + project)

def ncommits(request):

    session = buildSession(
    database='mysql://root:toor@localhost/vizgrimoire',
    echo=False)

    # Number of commits
    res = session.query().select_nscmlog(["commits",]) \
        .filter_period(start=datetime(2012,9,1),
                       end=datetime(2014,1,1))

    return HttpResponse(res.scalar())
