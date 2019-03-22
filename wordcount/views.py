from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'home.html')
def contact(request):
    return HttpResponse('<h1>Contact<h1><br>This is contact')
def count(request):
    data=request.GET['fulltextarea']

    l=list(data.split())
    frequency={}
    for i in l:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1

    return render(request,'count.html',{'fulltext':data,'length':len(l),'freq':frequency.items()})
