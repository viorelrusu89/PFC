from django.http import HttpResponse
from django.shortcuts import render
from scm_query import buildSession
from datetime import datetime
import json
from django.shortcuts import redirect

db_local='mysql://root:toor@localhost/vizgrimoire'
db_remote='mysql://viorel:blue1love@db4free.net/vizgrimoire'

def ncommits(request):

    session = buildSession(
    database=db_local,
    echo=False)

    # Number of commits
    res = session.query().select_nscmlog(["commits",]) \
        .filter_period(start=datetime(2012,9,1),
                       end=datetime(2014,1,1))
    ncommits = json.dumps({'ncommits': res.scalar()})

    return HttpResponse(ncommits)