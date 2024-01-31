from django.contrib import admin
from .models import *


# Приложение с новостями
admin.site.register(Category)
admin.site.register(Post)
