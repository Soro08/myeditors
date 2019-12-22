# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class QuizzAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom')
    list_filter = ('id', 'nom')


class ExercicesAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'quiz')
    list_filter = (
        'quiz',
    )


class QuestionsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'enonce',
        'point',
        'type_de_requete',
        'exercice',
    )
    list_filter = (
        'exercice',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Quizz, QuizzAdmin)
_register(models.Exercices, ExercicesAdmin)
_register(models.Questions, QuestionsAdmin)
