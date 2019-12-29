
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')



def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    uppercaps=request.POST.get('uppercaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for i in djtext:
            if i not in punctuations:
                analyzed = analyzed + i
        parms = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}


        return render(request, 'analyze.html', parms)
    elif(uppercaps=='on'):
        analyzed=""
        for i in djtext:
            analyzed=analyzed + i.upper()
        parms = {'purpose': 'UPPER CASE', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', parms)

    elif(newlineremover=='on'):
        analyzed=""
        for i in djtext:
            if i!="\n" and i!="\r":
                analyzed=analyzed+i
        parms = {'purpose': 'NEW LINE REMOVER', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', parms)

    elif(extraspaceremover=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index]==' ' and djtext[index+1]==' '):
                analyzed=analyzed+char
        parms = {'purpose': 'EXTRA SPACE REMOVER', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', parms)

    elif(charcount=='on'):
        analyzed=0
        for i in djtext:
            if(i>='a'and i<='z')or(i>='A'and i<='Z'):
                analyzed=analyzed+1
        parms = {'purpose': 'CHARACTER COUNT', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', parms)

    else:
        return HttpResponse("Error...!")
