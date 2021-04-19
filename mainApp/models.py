from django.db import models

class Articles(models.Model):
    # title = models.CharField('Название ',max_length=50)
    # anons = models.CharField('Анонс',max_length=250)
    # ful_text = models.TextField('Статья')
    # date = models.DateTimeField('Дата')
    ekbid = models.CharField('ЕКБИД',max_length=50)
    card = models.CharField('Карта',max_length=16)

    def __str__(self):
        return self.ekbid

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новость'