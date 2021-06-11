from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # show my html file
    return render(request, 'index.html')


def removePunch(request):
    # get text of textarea
    djtext = request.GET.get('text','default')

    # get checkbuttons values
    removePunc = request.GET.get('removePunc','off')
    extraSpaceRemover = request.GET.get('extraSpaceRemover','off')
    newLineRemover = request.GET.get('newLineRemover','off')
    upperCase = request.GET.get('upperCase','off')
    charCounter = request.GET.get('charCounter','off')

    # checking values is on or not
    if removePunc == 'on':
        analyzed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        param = {'purpose': "Remove Punctuations",'analyzed_text': analyzed}
        djtext = analyzed

    if upperCase == 'on':
        analyzed = djtext.upper()
        param = {'purpose':'Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraSpaceRemover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index + 1] == ' '):
                analyzed = analyzed + char
        param = {'purpose':'Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if newLineRemover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char !='\r':
                analyzed = analyzed + char
            else:
                print("not working")
        param = {'purpose':'Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
    if charCounter == 'on':
        analyze = 0
        for char in djtext:
                analyze = analyze + 1
        param = {'purpose':'Space Remover', 'analyzed_text': analyze,'text':'there are ','text2':' characters in your text'}
    elif removePunc != 'on' and newLineRemover != 'on' and upperCase != 'on' and charCounter != 'on' and extraSpaceRemover != 'on':
        return HttpResponse('''<h1>404 Error</h1> ''')
    return  render(request, 'analyze.html', param)

