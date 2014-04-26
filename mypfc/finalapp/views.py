from django.http import HttpResponse
from django.shortcuts import render
from scm_query import buildSession
from datetime import datetime
import json

db_local='mysql://root:toor@localhost/vizgrimoire'
db_remote='mysql://sql435278:tD2!rE6*@sql4.freemysqlhosting.net:3306/sql435278'


def home(request):

	html = "<html><body><a href='/static/index.html'>SPA here</a></body></html>"
	return HttpResponse(html)

def users(request):
	html = "This should be home view.. I think this is not the way to do it in a SPA"
	return HttpResponse(html)

def ncommits(request):

    session = buildSession(
    database=db_remote,
    echo=False)

    # Number of commits
    res = session.query().select_nscmlog(["commits",]) \
        .filter_period(start=datetime(2012,9,1),
                       end=datetime(2014,1,1))
    ncommits = json.dumps({'ncommits': res.scalar()})

    return HttpResponse(ncommits)

def timeseries(request):

    session = buildSession(
    database=db_local,
    echo=False)

    res = session.query().select_nscmlog(["commits",]) \
    .group_by_period() \
    .filter_period(end=datetime(2014,1,1))
    ts = res.timeseries ()

    return HttpResponse(ts.json())