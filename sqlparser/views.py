from django.shortcuts import render, redirect
from . import models
from django.core import serializers
# Create your views here.

####### Json responde
from django.http import JsonResponse
####### Parser

import requests
import json


from jsondiff import diff


builde_url = "http://sqlfiddle.com/backend/createSchema?_action=create"

compile_url = "http://sqlfiddle.com/backend/executeQuery?_action=query"

def accueil(request):
    exo = models.Exercices.objects.filter(status = True)
    
    data = {
        'exos':exo
    }
    return render(request, 'home.html', data)

def compilesql(request):

    exoid = request.POST.get('exoid')
    exoids = request.POST.get('exoids')
    codeuserresult = None
    codeadminresult = None
    message = ""
    status = False
    compt = 0
    try:
        exoid = int(exoid) 
        exoids = int(exoids) 

        exo = models.Exercices.objects.get(pk = exoids)
        quests = models.Questions.objects.get(pk = exoid)
        


        ############ CODE USER ############
        codeuser = request.POST.get('code')

        ###### CREATE TABLE BEGIN
        code_sal_table = exo.codesql_creation
        data_create_table = {
            "db_type_id": 9,
            "ddl": code_sal_table,
            "statement_separator": ";"
        }

        req_create_table = requests.post(builde_url, json=data_create_table)
                
        reponse_create_table = json.loads(req_create_table.text)

        id_table_create = reponse_create_table['short_code']


    ############ TEST CODE ###############
        compt = 0


        codeuser_admin = quests.codesql_reponse

        ######## CRETE TABLE END
        print(id_table_create)

        ########### COMPILE RESULT USRT
        id_table = id_table_create
        data_compile = {
            "db_type_id": 9,
            "schema_short_code": id_table,
            "sql": codeuser,
            "statement_separator": ";",
        }

        req_user = requests.post(compile_url, json = data_compile)

        reponse_user = json.loads(req_user.text)

        ######## ADMIN COMPILE
        data_compile_nan = {
            "db_type_id": 9,
            "schema_short_code": id_table,
            "sql": codeuser_admin,
            "statement_separator": ";",
        }

        req_admin = requests.post(compile_url, json = data_compile_nan)

        reponse_admin = json.loads(req_admin.text)

        admin_resullt = reponse_admin['sets'][0]['RESULTS']
        codeadminresult = admin_resullt

        status = reponse_user['sets'][0]['SUCCEEDED']
        if status:
            user_result = reponse_user['sets'][0]['RESULTS']
            codeuserresult = user_result
            if len(diff(admin_resullt, user_result)) == 0:
                status = True
            else:
                status = False
                message = "La requeste saisie ne correspond pas"


        else:
            message = reponse_user['sets'][0]['ERRORMESSAGE']


    except:
        message = "Erreur de compilation"

    if status :
        message = "felicitation vous avez validé ce test"

    data = {
        'status':status,
        'message':message,
        'compt':compt,
        'codeuser':codeuserresult,
        'codeadmin':codeadminresult
    }
    return JsonResponse(data=data, safe=False)


def home(request, key):
    try:
        exercice = models.Exercices.objects.get(pk=key)
        question = models.Questions.objects.filter(exercice = exercice)
        data = {
            'question':question,
            'exercice':exercice,
            'exoid':key,
        }
        return render(request, 'sql.html', data)
    except:
        redirect('/')


def getexo(request):
    exoid = request.POST.get("exoid")
    question = models.Questions.objects.get(pk = exoid)
    questiondata = serializers.serialize('json', [question])
    data = json.loads(questiondata)

    return JsonResponse(data=data, safe=False)