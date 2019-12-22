from django.shortcuts import render

from text_query.models import Query

# Create your views here.
def Dashboard(request):
    queries = Query.objects
    return render(request, 'dashboard.html', {'queries':queries})
