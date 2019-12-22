from django.shortcuts import render, get_object_or_404

from text_query.models import Query

# Create your views here.
def Dashboard(request):
    queries = Query.objects
    return render(request, 'dashboard.html', {'queries':queries})

def detail(request, query_id):
    query_detail = get_object_or_404(Query, pk=query_id)
    return render(request, 'customer_relationship_management/detail.html', {'query':query_detail})
