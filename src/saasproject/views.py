from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

def home_page_view(request, *args, **kwargs):
    my_title = "WELCOME TO SAAS PROJECT"
    query_set = PageVisit.objects.filter(path=request.path)
    my_context = {
        "page_title" : my_title,
        "query_set" : query_set,
        "page_visit_count" : query_set.count()
    }
    html_template = 'home_page_view.html'
    PageVisit.objects.create(path = request.path)
    return render(request, html_template, my_context )