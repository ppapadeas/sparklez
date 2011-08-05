from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.conf.urls.defaults import *


def base(request):
    return render_to_response('base.html')
    #return HttpResponseRedirect('/gallery/')
