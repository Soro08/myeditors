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

def valid(element, html):
    resultat = BeautifulSoup(html, 'html.parser')
    if element.many:
        try:
            resultat = resultat.findAll(element.balise, attrs={ element.attribue : element.attribue_value })
            print(resultat[0].text)
            correctehtml = len(resultat) == element.nombre
        except:
            print(valid.balise)
            correctehtml = False
    else:
        try:
            resultat = resultat.find(element.balise, attrs={ element.attribue : element.attribue_value })
            print(resultat.text)
            correctehtml = True
        except:
            print(valid.balise)
            correctehtml = False
    return (resultat, correctehtml)

# def compile(html, list_element, index):
#     element = list_element[index]
#     resultat, correcthmtl = valid(element, html)
#     index +=1
#     if 
#     :
#         while index < len(list_element):
#             if (list_element[index].niveau >= element.niveau):
#                 break
#             else:
#                 compile(resultat, list_element, index)
#     return co

def home(request, id):
    code = models.Enonce.objects.get(pk=id)

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

    correctehtml = False
    url_parse = requests.post(url, data=donne)
    print(url_parse.text)
    codevalid = json.loads(url_parse.text)
    if len(codevalid) == 0:
        codesuccess = True
    else:
        codesuccess = False
    
    if codesuccess:
    
        soup = BeautifulSoup(html_doc, 'html.parser')

        validationhtml = models.ValidationHtml.objects.filter(enoncer__pk = 3)
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

    data = {
        'status':codesuccess,
        # "css":codecss,
        "result":codevalid,
        'validehtml':correctehtml,
    }



    #stdout = StringIO.StringIO()
   
    return JsonResponse(data)