from django.db import models

# Create your models here.

class Enonce(models.Model):
    """Model definition for Enonce."""

    # TODO: Define fields here
    titre = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        """Meta definition for Enonce."""

        verbose_name = 'Enonce'
        verbose_name_plural = 'Enonces'

    def __str__(self):
        """Unicode representation of Enonce."""
        return self.titre


class ValidationHtml(models.Model):
    """Model definition for ValidationHtml."""

    # TODO: Define fields here
    enoncer = models.ForeignKey(Enonce, on_delete=models.CASCADE, related_name ='valideenoncer', null=True)
    balise = models.CharField(max_length=250, help_text="Ex : p, h1, div, a, img, ... ") 
    attribue = models.CharField(max_length=250, help_text="Ex : class, id, href, src, target, ... ") 
    attribue_value = models.CharField(max_length=250, help_text="Ex : contenaire, app, http://nan.ci, __blank, ... ") 
    niveau = models.PositiveIntegerField(default=1, help_text="Ex: 1 si la verification se fait au premier niveau <br />2 Si la verification se fait au niveau 2, ") 
    many = models.BooleanField(default=False, help_text="Ex: Cocher si l'element se propose plusieur fois")
    nombre = models.PositiveIntegerField(default=1, help_text="Le nombre de fois que l'element s'affiche")


    class Meta:
        """Meta definition for ValidationHtml."""

        verbose_name = 'ValidationHtml'
        verbose_name_plural = 'ValidationHtmls'

    def __str__(self):
        """Unicode representation of ValidationHtml."""
        return self.balise
