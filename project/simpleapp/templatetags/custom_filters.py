from django import template
from django.http import HttpResponse

register = template.Library()

CURRENCIES_SYMBOLS = {
   'rub': 'Р',
   'usd': '$',
}


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter(name='currency')
def currency(value, code='rub'):
   """
   value: значение, к которому нужно применить фильтр
   code: код валюты
   """
   postfix = CURRENCIES_SYMBOLS[code]

   # Возвращаемое функцией значение подставится в шаблон.
   return f'{value} {postfix}'
