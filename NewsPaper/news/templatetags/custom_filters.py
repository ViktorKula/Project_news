# from django import template
#
# register = template.Library()
#
#
# # Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# # что это именно фильтр для шаблонов, а не простая функция.
# @register.filter()
#
# def cenzor(value):
#
#     badwords = ["искусственный"]
#     splitwords = value.split()
#
#     for i in range(len(splitwords)):
#         if splitwords[i] in badwords:
#             firstletter = splitwords[i][0]
#             newvalue=firstletter +"*"*(len(splitwords[i])-1)
#             splitwords[i] = newvalue
#     result = " ".join(splitwords)
#     return f'{result}'