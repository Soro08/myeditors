from django.db import models
from tinymce import HTMLField
# Create your models here.
class Quizz(models.Model):
    """Model definition for Quizz."""

    # TODO: Define fields here
    nom = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Quizz."""

        verbose_name = 'Quizz'
        verbose_name_plural = 'Quizzs'

    def __str__(self):
        """Unicode representation of Quizz."""
        return self.nom


class Exercices(models.Model):
    """Model definition for Exercices."""

    # TODO: Define fields here
    titre = models.CharField(max_length=250)
    minidescription = models.TextField(null=True)
    description = HTMLField('Content')
    codesql_creation = models.TextField()
    quiz = models.ForeignKey(Quizz, on_delete=models.CASCADE, related_name="exoquiz")
    
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Exercices."""

        verbose_name = 'Exercices'
        verbose_name_plural = 'Exercicess'

    def __str__(self):
        """Unicode representation of Exercices."""
        return self.titre

class Questions(models.Model):
    QUERY_TYPE = [
        (1, 'Query'),
        (2, 'Mutation'),
    ]
    """Model definition for Questions."""
    titre = models.CharField(max_length=250)
    enonce = models.TextField()
    codesql_depart = models.TextField()
    codesql_reponse = models.TextField()
    ###### SPECIFICATION ET MUTATION
    type_de_requete = models.IntegerField(choices=QUERY_TYPE, default=1, help_text='Ici on a deux type de reque: <br />Query pour les requete de type SELECT. <br />Mutation pour les requete de type UPDATE, ADD, DELETE')
    code_de_verification = models.TextField(null=True, blank=True, help_text='Ici on ajoute le code sql de verification.<br />Exemple: select * from table <br />Cela nous permet de voir si le candidat  a supprimer, modifier ou ajouté la colene  ')
    
    point = models.PositiveIntegerField()
    exercice = models.ForeignKey(Exercices, on_delete=models.CASCADE, related_name="questexo")
    # TODO: Define fields here

    class Meta:
        """Meta definition for Questions."""

        verbose_name = 'Questions'
        verbose_name_plural = 'Questionss'

    def __str__(self):
        """Unicode representation of Questions."""
        return self.titre   





