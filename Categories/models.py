from django.db import models


class Category(models.Model):

    CAT_POLITICA = 'POL'
    CAT_ECONOMIA = 'ECO'
    CAT_SOCIEDAD = 'SOC'
    CAT_DEPORTE = 'DEP'
    CAT_CULTURA = 'CUL'
    CAT_CIENCIA = 'CIE'

    CATEGORIES = (
        (CAT_POLITICA, 'Política'),
        (CAT_ECONOMIA, 'Economía'),
        (CAT_SOCIEDAD, 'Sociedad'),
        (CAT_DEPORTE, 'Deporte'),
        (CAT_CULTURA, 'Cultura'),
        (CAT_CIENCIA, 'Ciencia')
    )


    tipo_categoria = models.CharField(max_length=3, choices=CATEGORIES, default=CAT_CULTURA)

    def __str__(self):  # category.__str__()
        return self.tipo_categoria
