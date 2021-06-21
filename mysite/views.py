# this file created later

from django.http import HttpResponse
from django.shortcuts import render
from . import log

def home(request):
    return render(request, 'textUtils.html')


def Analyze(request):
    x = request.GET.get('text')
    log.writeLog('./Log/log.txt', '--- Text Received --- '+'\n'+x+'\n', 'a+')


    # what tasks are needed to be performed
    if request.GET.get('RemovePuncutation') == 'on' :
        # taking punchuations as a set to make serch less costly
        punc, updated_x = set("""!"#$%&'()*+,-./:;?@[\]^_`{|}~"""), ''
        for i in x:
            if i not in punc :
                updated_x+=i
        x = updated_x
        print('After removing punchuation-', x)


    if request.GET.get('Capitalize') == 'on':
        x=x.upper()
        print('Upper Case -', x)



    if request.GET.get('newlineremover') == 'on':
        while '\n' in x :
            x = x.replace('\n' , ' ')
        print('After new lines ', x)



    if request.GET.get('extraspaceremover') == 'on':
        updated, i = '', 0
        while i < len(x):
            try:
                if x[i] == ' ':
                    while x[i] == ' ' and i < len(x):
                        i = i + 1
                    updated = updated + ' '
                else:
                    updated = updated + x[i]
                    i = i + 1
            except Exception as e:
                print('Exception Occured - ', e)

        x = updated
        print('updated - ', updated)

    return render(request, 'AnalyzedText.html', {'text':x})