from django.http import HttpResponse
from django.shortcuts import render
from scm_query import buildSession
from datetime import datetime
import json

def home(request):

	html = "<html><body>home</body></html>"
	return HttpResponse(html)

def users(request):
	html = "This should be home view.. I think this is not the way to do it in a SPA"
	return HttpResponse(html)

def ncommits(request):

    db_local='mysql://root:toor@localhost/vizgrimoire'
    db_remote='mysql://sql435278:tD2!rE6*@sql4.freemysqlhosting.net:3306/sql435278'

    session = buildSession(
    database=db_remote,
    echo=False)

    # Number of commits
    res = session.query().select_nscmlog(["commits",]) \
        .filter_period(start=datetime(2012,9,1),
                       end=datetime(2014,1,1))
    ncommits = json.dumps({'ncommits': res.scalar()})

    return HttpResponse(ncommits)