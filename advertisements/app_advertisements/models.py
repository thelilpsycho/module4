from django.db import models


class Advertisement(models.Model):

#чарфилд - небольшое текст поле
#заголовокчек
 title = models.CharField("Заголовок", max_length=128)

#описание
 description = models.TextField("Описание")

#цена
#децималфилд - число с фикс точкой
 price = models.DecimalField("Цена", max_digits=10,decimal_places=2)

#уместен ли торг
 auction = models.BooleanField("Торг", help_text="Уместен ли торг")

#дата создания
 created_at = models.DateTimeField(auto_now_add=True)

#дата изменения
 updated_at = models.DateTimeField(auto_now=True)

 class Meta:
  db_table='advertisements'
  
#изображение

#адрес

#отзывы о продавце

#контакты

#похожее

