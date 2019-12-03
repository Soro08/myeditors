from django.shortcuts import render
####### Json responde
from django.http import JsonResponse
####### Parser

import requests
import json
from jsondiff import diff


builde_url = "http://sqlfiddle.com/backend/createSchema?_action=create"

compile_url = "http://sqlfiddle.com/backend/executeQuery?_action=query"

def compilesql(request):

    message = ""

    codeuser = request.POST.get('code')
    id_table = "f63b3"
    data_compile = {
        "db_type_id": 9,
        "schema_short_code": id_table,
        "sql": codeuser,
        "statement_separator": ";",
    }

    req = requests.post(compile_url, json = data_compile)

    reponse = json.loads(req.text)

    status = reponse['sets'][0]['SUCCEEDED']
    if status:
        pass

    else:
        message = reponse['sets'][0]['ERRORMESSAGE']



    
    data = {
        'status':True,
        'message':message
    }
    return JsonResponse(data=data, safe=False)