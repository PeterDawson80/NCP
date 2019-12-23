from django.http import HttpResponse
from django.shortcuts import render
import operator

# Create your views here.
def Home(request):
    return render(request, 'home.html')

def Contact(request):
    return render(request, 'contact.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext, 'wordcount':len(wordlist), 'sortedwords': sortedwords})
