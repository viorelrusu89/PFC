from django.http import HttpResponse
from django.shortcuts import render
from scm_query import buildSession
from datetime import datetime
import json
from django.shortcuts import redirect

db_local='mysql://root:toor@localhost/prodb'
db_remote='mysql://viorel:blue1love@db4free.net/vizgrimoire'

session = buildSession(database=db_local, echo=False)

def home(request):

    return redirect ('/static/index.html')

def users(request):
	html = "This should be home view.. I think this is not the way to do it in a SPA"
	return HttpResponse(html)

def ncommits(request):

    # Number of commits
    res = session.query().select_nscmlog(["commits",])
    ncommits = json.dumps({'ncommits': res.scalar()})
    return HttpResponse(ncommits)

def timeseries(request):

    res = session.query().select_nscmlog(["commits",]) \
    .group_by_period() \
    .filter_period(end=datetime(2014,1,1))
    ts = res.timeseries ()
    return HttpResponse(ts.json())