from django.shortcuts import render, render_to_response, RequestContext

from vv.forms import PieceModelForm

def home_page():
    pass

from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

