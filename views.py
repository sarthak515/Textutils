from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

'''def about(request):
    return HttpResponse("hello srh bhai")'''
def analyze(request):
    #get text
    djtext=request.POST.get('text','default')
    #check checkbx value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')

    # chechk which checkbox is on
    if removepunc=="on":
        punctuations = '''!()-{}[];:'"\,<>./@#$%&*_'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'remove bhai puncutationss','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(fullcaps=="on"):
        analyzed=("")
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to capitalize', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(newlineremover=="on"):
        analyzed = ("")
        for char in djtext:
            if char !="]n":
                analyzed=analyzed+char
        params = {'purpose': 'remove new line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("error")


'''def capfirst(request):
    return  HttpResponse("capitalize first")
def newlineremove(request):
    return  HttpResponse("newline first")'''