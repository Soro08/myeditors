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
    description = HTMLField('Content')
    codesql_creation = models.TextField()
    quiz = models.ForeignKey(Quizz, on_delete=models.CASCADE, related_name="exoquiz")

    class Meta:
        """Meta definition for Exercices."""

        verbose_name = 'Exercices'
        verbose_name_plural = 'Exercicess'

    def __str__(self):
        """Unicode representation of Exercices."""
        return self.titre

class Questions(models.Model):
    """Model definition for Questions."""
    titre = models.CharField(max_length=250)
    enonce = models.TextField()
    codesql_depart = models.TextField()
    codesql_reponse = models.TextField()
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





