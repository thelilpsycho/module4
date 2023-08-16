from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User=get_user_model()

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
 updated_at = models.DateTimeField(auto_now_add=True)

 @admin.display(description='Дата изменения')
 def updated_date(self):
   from django.utils import timezone

   if self.updated_at.date()==timezone.now().date():
     updated_time=self.updated_at.strftime("%H:%M:%S")
     return format_html("<span style='color:green; font-weight:bold;'> Сегодня в {}</span>", updated_time)

   return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
 
 def __str__(self):
  return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

#дата изменения
 created_at = models.DateTimeField(auto_now=True)

 @admin.display(description='Дата создания')
 def created_date(self):
  from django.utils import timezone

  if self.created_at.date()==timezone.now().date():
   created_time=self.created_at.strftime("%H:%M:%S")
   return format_html("<span style='color:green; font-weight:bold;'> Сегодня в {}</span>", created_time)

  return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
 
 def __str__(self):
  return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

 class Meta:
  db_table='advertisements'

 @admin.display(description='фото')
 def get_html_image(self):
  if self.image:
    return format_html(
    '<img src="{}" style="max-height:80px; max-width:80px">',
    self.image.url
   )
 
#автор 
 user=models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
#изображение
 image=models.ImageField('изображение', upload_to='advertisements/')

 class Meta:
    db_table='advertisements'



#адрес

#отзывы о продавце

#контакты

#похожее

