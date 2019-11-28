from django.shortcuts import render

from django.http import JsonResponse

from bs4 import BeautifulSoup

from cssjson import toJSON, toCSS

def home(request):

    return render(request, 'index.html')


def compilehtml(request):

    html_doc = request.POST.get('code')
    css_doc = request.POST.get('css')

    codecss = toJSON(css_doc)

    soup = BeautifulSoup(html_doc, 'html.parser')

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
        'status':True,
        'soup':h,
        "p":p,
        "css":codecss
    }



    #stdout = StringIO.StringIO()
   
    return JsonResponse(data)