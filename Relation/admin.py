from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)