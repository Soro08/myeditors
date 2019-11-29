from django.shortcuts import render
####### Json responde
from django.http import JsonResponse
####### Parser
from bs4 import BeautifulSoup
from cssjson import toJSON, toCSS

import requests
import json


################# Models
from . import models


def home(request):
    code = models.Enonce.objects.all()[:1].get()

    data = {
        'code':code,
    }
    print(code)
    return render(request, 'index.html', data)


def compilehtml(request):

    html_doc = request.POST.get('code')
    css_doc = request.POST.get('css')
    codecss = toJSON(css_doc)

    url= "https://jsonformatter.org/service/validateHTML"
    donne = {
        'toolstype':'json',
        'data':html_doc
    }

    url_parse = requests.post(url, data=donne)
    print(url_parse.text)
    codevalid = json.loads(url_parse.text)
    if len(codevalid) == 0:
        codesuccess = True
    else:
        codesuccess = False
    
    if codesuccess:
    
        soup = BeautifulSoup(html_doc, 'lxml')

        validationhtml = models.ValidationHtml.objects.filter(enoncer__pk = 1)
        for valid in validationhtml:
            if valid.many:
                print("many")
            
            else:
                try:
                    testsoup = soup.find(valid.balise, attrs={ valid.attribue : valid.attribue_value })
                    print(testsoup.text)
                    correctehtml = True
                except:
                    print(valid.balise)
                    correctehtml = False

        try:
            h = soup.find('h1')
            h = h.text
        except:
            h = "h"

        try:
            p = soup.find('p', attrs={'class': 'nan'})
            p = p.text

        except:
            p = "p"

    data = {
        'status':codesuccess,
        # "css":codecss,
        "result":codevalid,
        'validehtml':correctehtml,
    }



    #stdout = StringIO.StringIO()
   
    return JsonResponse(data)